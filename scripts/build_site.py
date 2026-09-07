#!/usr/bin/env python3
"""Embed the verified catalogue into a single self contained page."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
import re
cat = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))
ar = json.loads((ROOT / "data" / "notes.ar.json").read_text(encoding="utf-8"))

# Each language mode must be complete on its own terms, so a missing or impure
# note fails the build rather than surfacing as English inside the Arabic page.
arabic_script = re.compile(r"[\u0600-\u06FF]")
latin_word = re.compile(r"[A-Za-z]{4,}")
faults = []
for tool in cat["tools"]:
    note = ar.get(tool["repo"], "")
    if not note:
        faults.append(f"{tool['repo']}: no Arabic note")
    elif latin_word.search(note):
        faults.append(f"{tool['repo']}: Latin words in the Arabic note")
    if arabic_script.search(tool["note"]):
        faults.append(f"{tool['repo']}: Arabic script in the English note")
    tool["noteAr"] = note
extra = set(ar) - {t["repo"] for t in cat["tools"]}
for e in sorted(extra):
    faults.append(f"{e}: Arabic note for a tool not in the catalogue")
if faults:
    print("Language check failed:", *faults, sep="\n  ", file=sys.stderr)
    sys.exit(1)
tpl = (ROOT / "src" / "index.template.html").read_text(encoding="utf-8")

html = tpl.replace("/*__CATALOG__*/null",
                   json.dumps(cat, ensure_ascii=False, separators=(",", ":")))
if "__CATALOG__" in html:
    print("payload placeholder not replaced", file=sys.stderr); sys.exit(1)

# The headline figures are written by hand in the template, so they can drift
# from the data. Check them rather than trust them.
s = cat["stats"]
for want, label in ((str(s["tools"]), "tools"),
                    (str(len(cat["roles"])), "roles"),
                    (str(s["languages"]), "languages")):
    if want not in tpl:
        print(f"headline figure for {label} ({want}) is not in the template", file=sys.stderr)
        sys.exit(1)

out = ROOT / "index.html"
out.write_text(html, encoding="utf-8")
print(f"index.html {out.stat().st_size // 1024} KB, {s['tools']} tools embedded")
