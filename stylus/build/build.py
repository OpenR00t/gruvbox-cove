# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 The Gruvbox Cove contributors
"""Rebuild gruvbox-cove-github / -youtube / -duckduckgo userstyles from Catppuccin's latest templates.
Needs: Python 3, Node (npx). Run from this folder:  python build.py
Writes ../gruvbox-cove-github.user.css and ../gruvbox-cove-youtube.user.css,
keeping the header and font-rule sections of the existing files.
"""
import re, subprocess, urllib.request, pathlib
HERE = pathlib.Path(__file__).parent
OUT = HERE.parent
SRC = "https://raw.githubusercontent.com/catppuccin/userstyles/main/styles/{}/catppuccin.user.less"
MAP = {'6e7681':'7c6f64','21262d':'3c3836','484f58':'665c54','848d97':'a89984','010409':'1d2021','dbab0a':'d79921','8b949e':'928374',
 '0d1117':'1d2021','161b22':'282828','f0f6fc':'ebdbb2','388bfd':'83a598','58a6ff':'8ec07c','4493f8':'83a598','fb331b':'fb4934',
 '051d4d':'3c3836','79c0ff':'83a598','292e36':'504945','666e79':'7c6f64','b1bac4':'a89984','e6edf3':'ebdbb2','0d419d':'458588',
 '04260f':'1d2021','1f6feb':'458588','da3633':'cc241d','490202':'cc241d','0c2d6b':'504945','2ea043':'98971a','a371f7':'d3869b',
 'db61a2':'d3869b','bd561d':'d65d0e'}

def remap(css):
    def rep(m):
        h = m.group(1).lower()
        return '#' + MAP[h] + (m.group(2) or '') if h in MAP else m.group(0)
    return re.sub(r'(?<!=")#([0-9a-fA-F]{6})([0-9a-fA-F]{2})?\b', rep, css)   # skip [fill="#..."] selectors

for site in ("github", "youtube", "duckduckgo", "twitch"):
    less = urllib.request.urlopen(SRC.format(site)).read().decode()
    less = re.sub(r'/\* ==UserStyle==.*?==/UserStyle== \*/', '', less, flags=re.S)
    less = re.sub(r'@import "https://userstyles\.catppuccin\.com/lib/[^"]*";', '', less)
    less = re.sub(r'@import url\("https://[^"]*"\);', '', less)   # external stylesheets (e.g. pygments colors) aren't used
    prep = HERE / f"{site}.prep.less"
    prep.write_text((HERE / "shim.less").read_text() + less)
    css = subprocess.run(f'npx --yes less@4.2.0 "{prep}"', capture_output=True, text=True, shell=True, check=True).stdout
    css = re.sub(r'[ \t]*/\*.*?\*/[ \t]*\n?', '', css, flags=re.S)   # drop upstream comments
    if site == "github":
        css = remap(css)
    target = OUT / f"gruvbox-cove-{site}.user.css"
    old = target.read_text()
    head = old[:old.index("*/", old.index("Built from Catppuccin")) + 3]          # metadata + attribution
    fonts = old[old.index("/* ---------- Gruvbox Cove font rule"):]
    target.write_text(head + css + "\n" + fonts)
    prep.unlink()
    print("rebuilt", target.name)
