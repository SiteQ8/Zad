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
from seed import CATEGORIES, PATHS, ROLES, TOOLS  # noqa: E402
from web import KINDS, WEB  # noqa: E402
sys.path.insert(0, str(ROOT / "scripts"))
from webcheck import check_all  # noqa: E402

OUT = ROOT / "data" / "catalog.json"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

# Months since the last push before a project stops looking maintained. These
# are deliberately generous: a stable tool with no open problems does not need
# monthly commits, and calling it abandoned would be wrong.
ACTIVE_DAYS = 180
SLOW_DAYS = 730


DASHES = {0x2012: "-", 0x2013: "-", 0x2014: "-", 0x2015: "-"}


def clean(text):
    """Upstream descriptions carry Unicode dashes. Normalise at ingest so they
    cannot reach the published page."""
    return (text or "").translate(DASHES).strip()


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
            "description": clean(data["description"]),
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

    # ---- The open web half. Verified by fetching, not by an API, because the
    # web does not have one. Only dead and unreachable are failures: a site that
    # refuses a script is not a site that has closed.
    print(f"\nfetching {len(WEB)} web resources")
    results = check_all([w[0] for w in WEB], workers=10)
    sites, site_faults, site_moves = [], [], []
    for url, kind, roles, note in WEB:
        r = results[url]
        if r["state"] in ("dead", "unreachable"):
            site_faults.append(f"{url}  {r['state']} {r.get('status') or r.get('error','')}")
            continue
        if r["state"] == "moved":
            site_moves.append((url, r["final"]))
        sites.append({
            "url": r["final"], "requested": url, "kind": kind, "roles": roles,
            "note": note, "state": r["state"], "status": r["status"],
            "host": r["final"].split("/")[2] if "//" in r["final"] else url,
        })

    if site_faults:
        print(f"\n{len(site_faults)} web resources failed:", file=sys.stderr)
        for f in site_faults:
            print(f"  {f}", file=sys.stderr)
        if strict:
            sys.exit(1)
    if site_moves:
        print("\nfollowed web redirects:")
        for old, new in site_moves:
            print(f"  {old} -> {new}")
    st = {}
    for s in sites:
        st[s["state"]] = st.get(s["state"], 0) + 1
    print(f"web: {len(sites)} live, {len(site_faults)} failed, states {st}")

    counts = {}
    for e in entries:
        counts[e["upkeep"]] = counts.get(e["upkeep"], 0) + 1


    # The starting path is advice, so it must not send a beginner at something
    # that has stopped. An unresolved or archived step fails the build.
    have = {e["repo"]: e for e in entries}
    lower = {k.lower(): v for k, v in have.items()}
    path_faults, paths = [], []
    for en, ar, enD, arD, steps in PATHS:
        resolved = []
        for step in steps:
            hit = lower.get(step.lower())
            if hit is None:
                path_faults.append(f"path step {step} is not in the catalogue")
                continue
            if hit["upkeep"] in ("archived", "dormant"):
                path_faults.append(
                    f"path step {hit['repo']} is {hit['upkeep']}, the starting path must not recommend it")
            resolved.append(hit["repo"])
        paths.append({"en": en, "ar": ar, "enD": enD, "arD": arD, "steps": resolved})
    if path_faults:
        print("\nStarting path check failed:", *path_faults, sep="\n  ", file=sys.stderr)
        sys.exit(1)

    catalog = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "roles": [{"id": r[0], "en": r[1], "ar": r[2], "enD": r[3], "arD": r[4]} for r in ROLES],
        "categories": {k: {"en": v[0], "ar": v[1]} for k, v in CATEGORIES.items()},
        "kinds": {k: {"en": v[0], "ar": v[1]} for k, v in KINDS.items()},
        "paths": paths,
        "stats": {
            "tools": len(entries),
            "sites": len(sites),
            "site_states": st,
            "unresolved": len(failed),
            "stars": sum(e["stars"] for e in entries),
            "upkeep": counts,
            "per_role": {r[0]: (sum(1 for e in entries if r[0] in e["roles"]) +
                            sum(1 for s in sites if r[0] in s["roles"])) for r in ROLES},
            "languages": len({e["language"] for e in entries if e["language"]}),
        },
        "tools": sorted(entries, key=lambda e: -e["stars"]),
        "sites": sites,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(catalog, indent=2, ensure_ascii=False) + "\n"
    stray = [c for c in payload if 0x2012 <= ord(c) <= 0x2015]
    if stray:
        print(f"\n{len(stray)} Unicode dashes survived normalisation", file=sys.stderr)
        sys.exit(1)
    OUT.write_text(payload, encoding="utf-8")

    print(f"\ncatalogue: {len(entries)} tools, {len(failed)} unresolved")
    print(f"  upkeep {counts}")
    print(f"  combined stars {catalog['stats']['stars']:,}")


if __name__ == "__main__":
    main()
