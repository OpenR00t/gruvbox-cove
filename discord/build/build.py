# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 The Gruvbox Cove contributors
"""Rebuild ../gruvbox-cove.theme.css from Catppuccin's latest Discord theme.
Needs: git, Node (npx/npm), Python 3. Run from this folder:  python build.py
"""
import pathlib, re, shutil, subprocess, tempfile
HERE = pathlib.Path(__file__).parent
OUT = HERE.parent / "gruvbox-cove.theme.css"
run = lambda cmd, cwd: subprocess.run(cmd, cwd=cwd, shell=True, check=True)

with tempfile.TemporaryDirectory() as tmp:
    repo = pathlib.Path(tmp) / "discord"
    run("git clone -q --depth 1 https://github.com/catppuccin/discord.git discord", tmp)
    shutil.copy(HERE / "_gruvbox.scss", repo / "src")
    shutil.copy(HERE / "gruvbox-cove.theme.scss", repo / "src")
    run("npm install --silent --ignore-scripts", repo)
    run("npx sass -I node_modules --no-charset --no-source-map src/gruvbox-cove.theme.scss out.css", repo)
    css = (repo / "out.css").read_text(encoding="utf-8")

old = OUT.read_text(encoding="utf-8")
head = old[:old.index("*/", old.index("Built from catppuccin/discord")) + 3]   # Vencord meta + attribution
extras = re.sub(r"\A/\* SPDX.*?\*/\s*", "", (HERE / "extras.css").read_text(encoding="utf-8"), flags=re.S)   # license header stays at the top of the output
OUT.write_text(head + "\n" + css + extras, encoding="utf-8")
print("rebuilt", OUT.name)
