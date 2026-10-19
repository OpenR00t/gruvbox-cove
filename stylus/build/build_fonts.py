# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 The Gruvbox Cove contributors
"""Write the global fonts style with the list of sites it must skip.

Sites come from themed-sites.txt (published) and, if present, ../../private/themed-sites.txt (local only).
  ../gruvbox-cove-fonts.user.css          published sites only
  ../../private/stylus/gruvbox-cove-fonts.user.css   published + private sites (install this one)
Run: python build_fonts.py
"""
import pathlib, re
HERE = pathlib.Path(__file__).parent
PUBLIC = HERE.parent / "gruvbox-cove-fonts.user.css"
PRIVATE_LIST = HERE.parent.parent / "private" / "themed-sites.txt"
PRIVATE_OUT = HERE.parent.parent / "private" / "stylus" / "gruvbox-cove-fonts.user.css"

def sites(path):
    if not path.exists(): return []
    return [l.strip() for l in path.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]

def regexp(domains):
    alts = "|".join(r"([^/]*\\.)?" + re.escape(d).replace(r"\.", r"\\.") for d in domains)
    return '@-moz-document regexp("^https?://(?!' + alts + r')[^/]+(/.*)?$") {'

template = PUBLIC.read_text(encoding="utf-8")
line = re.compile(r'^@-moz-document regexp\(.*\{$', re.M)
public = sites(HERE / "themed-sites.txt")
PUBLIC.write_text(line.sub(lambda m: regexp(public), template, count=1), encoding="utf-8", newline="")
print("wrote", PUBLIC.name, len(public), "sites")
private = sites(PRIVATE_LIST)
if private:
    PRIVATE_OUT.parent.mkdir(parents=True, exist_ok=True)
    PRIVATE_OUT.write_text(line.sub(lambda m: regexp(public + private), template, count=1), encoding="utf-8", newline="")
    print("wrote private copy with", len(public) + len(private), "sites")
