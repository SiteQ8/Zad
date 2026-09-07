#!/usr/bin/env python3
"""Resolve every catalogue entry against GitHub and record what is actually true.

A curated list is only worth reading if its entries are alive. This build asks
GitHub about each repository and records stars, licence, language, archive
status and the date of the last push, then classifies maintenance from the last
push rather than from the compiler's impression.

An entry that cannot be resolved is not published. A renamed repository is
followed and the new name recorded, so the catalogue corrects itself rather than
rotting.

Usage:
    GITHUB_TOKEN=... python3 scripts/build.py
    GITHUB_TOKEN=... python3 scripts/build.py --strict   fail on any unresolved entry
"""

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "data"))
from seed import CATEGORIES, ROLES, TOOLS  # noqa: E402

OUT = ROOT / "data" / "catalog.json"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

# Months since the last push before a project stops looking maintained. These
# are deliberately generous: a stable tool with no open problems does not need
# monthly commits, and calling it abandoned would be wrong.
ACTIVE_DAYS = 180
SLOW_DAYS = 730


def api(path):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={"Accept": "application/vnd.github+json",
                 **({"Authorization": f"token {TOKEN}"} if TOKEN else {})},
    )
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        return e.code, None


def upkeep(pushed_at, archived):
    if archived:
        return "archived"
    age = (datetime.now(timezone.utc) - datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))).days
    if age <= ACTIVE_DAYS:
        return "active"
    if age <= SLOW_DAYS:
        return "slow"
    return "dormant"


def main():
    strict = "--strict" in sys.argv
    entries, failed, renamed = [], [], []

    for i, entry in enumerate(TOOLS, 1):
        repo, cat, roles, note = entry[:4]
        supersede = entry[4] if len(entry) > 4 else ""
        status, data = api(f"/repos/{repo}")
        if status != 200 or not data:
            failed.append((repo, status))
            print(f"  [{i:3}/{len(TOOLS)}] UNRESOLVED {status}  {repo}", file=sys.stderr)
            continue

        actual = data["full_name"]
        if actual.lower() != repo.lower():
            renamed.append((repo, actual))

        entries.append({
            "repo": actual,
            "name": data["name"],
            "owner": data["owner"]["login"],
            "category": cat,
            "roles": roles,
            "note": note,
            "description": (data["description"] or "").strip(),
            "language": data["language"] or "",
            "stars": data["stargazers_count"],
            "licence": ((data.get("license") or {}).get("spdx_id") or "")
                       if data.get("license") else "",
            "archived": data["archived"],
            "pushed": data["pushed_at"][:10],
            "upkeep": upkeep(data["pushed_at"], data["archived"]),
            "url": data["html_url"],
            "homepage": (data["homepage"] or "").strip(),
            "topics": data.get("topics") or [],
            "supersede": supersede,
        })
        print(f"  [{i:3}/{len(TOOLS)}] {entries[-1]['upkeep']:8} {actual}")

    if failed:
        print(f"\n{len(failed)} entries could not be resolved:", file=sys.stderr)
        for repo, code in failed:
            print(f"  {repo}  HTTP {code}", file=sys.stderr)
        if strict:
            sys.exit(1)

    if renamed:
        print("\nfollowed renames:")
        for old, new in renamed:
            print(f"  {old} -> {new}")

    counts = {}
    for e in entries:
        counts[e["upkeep"]] = counts.get(e["upkeep"], 0) + 1
    per_role = {r[0]: sum(1 for e in entries if r[0] in e["roles"]) for r in ROLES}

    catalog = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "roles": [{"id": r[0], "en": r[1], "ar": r[2], "enD": r[3], "arD": r[4]} for r in ROLES],
        "categories": {k: {"en": v[0], "ar": v[1]} for k, v in CATEGORIES.items()},
        "stats": {
            "tools": len(entries),
            "unresolved": len(failed),
            "stars": sum(e["stars"] for e in entries),
            "upkeep": counts,
            "per_role": per_role,
            "languages": len({e["language"] for e in entries if e["language"]}),
        },
        "tools": sorted(entries, key=lambda e: -e["stars"]),
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"\ncatalogue: {len(entries)} tools, {len(failed)} unresolved")
    print(f"  upkeep {counts}")
    print(f"  combined stars {catalog['stats']['stars']:,}")


if __name__ == "__main__":
    main()
