# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 The Gruvbox Cove contributors
"""Bump the patch version of every theme file a rebuild changed, so Stylus and Vencord see an update.

Looks at `git diff` for modified *.user.css and *.theme.css files and raises `@version x.y.z` to `x.y.(z+1)`,
unless the version line itself already changed. Prints one line per bumped file."""
import pathlib, re, subprocess

changed = subprocess.run(["git", "diff", "--name-only"], capture_output=True, text=True, check=True).stdout.split()
for name in changed:
    if not name.endswith((".user.css", ".theme.css")):
        continue
    diff = subprocess.run(["git", "diff", "-U0", "--", name], capture_output=True, text=True, check=True).stdout
    if re.search(r"^[+-].*@version", diff, re.M):
        continue
    path = pathlib.Path(name)
    text = path.read_text(encoding="utf-8")
    m = re.search(r"(@version\s+)(\d+)\.(\d+)\.(\d+)", text)
    if not m:
        continue
    new = f"{m.group(2)}.{m.group(3)}.{int(m.group(4)) + 1}"
    path.write_text(text[:m.start()] + m.group(1) + new + text[m.end():], encoding="utf-8", newline="")
    print(f"{name}: {m.group(2)}.{m.group(3)}.{m.group(4)} -> {new}")
