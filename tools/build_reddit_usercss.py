# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 The Gruvbox Cove contributors
"""Wrap reddit/gruvbox-old-reddit.css as a Stylus style (reddit/gruvbox-old-reddit.user.css).

The .css file is the source (also usable as an RES snippet). Installed in Stylus from the repo, the style
updates itself; RES's URL loader doesn't reliably apply outside stylesheets on old reddit.
Bump VERSION when the stylesheet changes, then run: python tools/build_reddit_usercss.py"""
import pathlib
VERSION = "2.0.0"
ROOT = pathlib.Path(__file__).resolve().parents[1]
src = (ROOT / "reddit" / "gruvbox-old-reddit.css").read_text(encoding="utf-8")
body = "\n".join(("  " + l) if l.strip() else "" for l in src.splitlines())
out = f"""/* ==UserStyle==
@name         Gruvbox Cove — old reddit
@namespace    gruvbox-cove
@version      {VERSION}
@description  Gruvbox dark for old reddit with RES: green accent, CaskaydiaCove interface, Cove Sans SemiLight posts and comments. Turn on RES "Ignore subreddit styles".
@author       The Gruvbox Cove contributors
@license      AGPL-3.0-or-later
==/UserStyle== */
/* Built from reddit/gruvbox-old-reddit.css by tools/build_reddit_usercss.py; edit that file instead. */

@-moz-document domain("old.reddit.com"), domain("np.reddit.com") {{
{body}
}}
"""
(ROOT / "reddit" / "gruvbox-old-reddit.user.css").write_text(out, encoding="utf-8", newline="")
print("wrote reddit/gruvbox-old-reddit.user.css", VERSION)
