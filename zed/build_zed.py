# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 The Gruvbox Cove contributors
"""Builds themes/gruvbox-cove.json for Zed. Same palette and syntax roles as the VS Code and Neovim themes.
Run: python build_zed.py"""
import json, pathlib

P = dict(bg_h="#1d2021", bg0="#282828", bg0_s="#32302f", bg1="#3c3836", bg2="#504945", bg3="#665c54", bg4="#7c6f64",
         fg0="#fbf1c7", fg="#ebdbb2", fg2="#d5c4a1", fg3="#bdae93", fg4="#a89984", gray="#928374",
         red="#fb4934", green="#b8bb26", yellow="#fabd2f", blue="#83a598", purple="#d3869b", aqua="#8ec07c", orange="#fe8019",
         red_d="#cc241d", green_d="#98971a", yellow_d="#d79921", blue_d="#458588", purple_d="#b16286", aqua_d="#689d6a", orange_d="#d65d0e")
A = P["green"]                       # the accent
a = lambda c, alpha: c + alpha       # hex + alpha byte

def st(color, style=None, weight=None):
    return {"color": color, "font_style": style, "font_weight": weight}

def status(fg, bgdark):
    return {"": fg, ".background": bgdark, ".border": fg + "66"}

ui = {
    # surfaces: chrome on bg0_h, editor on bg0 (same as VS Code)
    "background": P["bg_h"], "surface.background": P["bg_h"], "elevated_surface.background": P["bg_h"],
    "panel.background": P["bg_h"], "status_bar.background": P["bg_h"], "title_bar.background": P["bg_h"],
    "title_bar.inactive_background": P["bg_h"], "toolbar.background": P["bg0"],
    "tab_bar.background": P["bg_h"], "tab.inactive_background": P["bg_h"], "tab.active_background": P["bg0"],
    "editor.background": P["bg0"], "editor.gutter.background": P["bg0"], "editor.foreground": P["fg"],
    "editor.subheader.background": P["bg1"],
    "editor.active_line.background": P["bg0_s"], "editor.highlighted_line.background": P["bg1"],
    "editor.line_number": P["bg4"], "editor.active_line_number": A, "editor.hover_line_number": P["fg4"],
    "editor.invisible": P["bg3"], "editor.wrap_guide": P["bg1"], "editor.active_wrap_guide": P["bg2"],
    "editor.indent_guide": P["bg1"], "editor.indent_guide_active": P["bg3"],
    "editor.document_highlight.read_background": a(P["blue"], "26"),
    "editor.document_highlight.write_background": a(P["gray"], "55"),
    "editor.document_highlight.bracket_background": a(A, "33"),
    "panel.indent_guide": P["bg1"], "panel.indent_guide_active": P["bg3"], "panel.indent_guide_hover": P["bg4"],
    # borders: green marks focus
    "border": P["bg1"], "border.variant": P["bg1"], "border.focused": a(A, "99"), "border.selected": A,
    "border.transparent": "#00000000", "border.disabled": P["bg2"],
    "panel.focused_border": A, "pane.focused_border": a(A, "99"), "pane_group.border": P["bg1"],
    # elements
    "element.background": P["bg1"], "element.hover": P["bg1"], "element.active": P["bg2"],
    "element.selected": P["bg1"], "element.disabled": P["bg_h"],
    "ghost_element.background": "#00000000", "ghost_element.hover": a(P["bg1"], "cc"), "ghost_element.active": P["bg2"],
    "ghost_element.selected": P["bg1"], "ghost_element.disabled": "#00000000",
    "drop_target.background": a(A, "33"),
    # text and icons
    "text": P["fg"], "text.muted": P["fg4"], "text.placeholder": P["gray"], "text.disabled": P["bg4"], "text.accent": A,
    "icon": P["fg2"], "icon.muted": P["fg4"], "icon.disabled": P["bg4"], "icon.placeholder": P["gray"], "icon.accent": A,
    "link_text.hover": A,
    # search, scrollbar
    "search.match_background": a(A, "40"), "search.active_match_background": a(P["orange"], "66"),
    "scrollbar.thumb.background": a(P["bg3"], "99"), "scrollbar.thumb.hover_background": P["bg3"],
    "scrollbar.thumb.active_background": P["bg4"], "scrollbar.thumb.border": "#00000000",
    "scrollbar.track.background": "#00000000", "scrollbar.track.border": "#00000000",
    # git
    "version_control.added": P["green"], "version_control.modified": P["blue"], "version_control.deleted": P["red"],
    "version_control.conflict": P["orange"], "version_control.ignored": P["bg4"], "version_control.renamed": P["aqua"],
    # terminal (same as Windows Terminal scheme)
    "terminal.background": P["bg0"], "terminal.ansi.background": P["bg0"], "terminal.foreground": P["fg"],
    "terminal.bright_foreground": P["fg0"], "terminal.dim_foreground": P["fg4"],
}
for name, (n, b) in dict(black=(P["bg1"], P["gray"]), red=(P["red_d"], P["red"]), green=(P["green_d"], P["green"]),
                         yellow=(P["yellow_d"], P["yellow"]), blue=(P["blue_d"], P["blue"]), magenta=(P["purple_d"], P["purple"]),
                         cyan=(P["aqua_d"], P["aqua"]), white=(P["fg4"], P["fg"])).items():
    ui[f"terminal.ansi.{name}"], ui[f"terminal.ansi.bright_{name}"], ui[f"terminal.ansi.dim_{name}"] = n, b, n + "aa"

# diagnostics / status: yellow only for warnings
for key, fg, bg in [("error", P["red"], "#3c1f1e"), ("warning", P["yellow"], "#3d3420"), ("info", P["blue"], "#283236"),
                    ("hint", P["aqua"], "#2b3328"), ("success", P["green"], "#32361a"), ("created", P["green"], "#32361a"),
                    ("deleted", P["red"], "#3c1f1e"), ("modified", P["blue"], "#283236"), ("renamed", P["aqua"], "#2b3328"),
                    ("conflict", P["orange"], "#3d2a1c"), ("predictive", P["bg4"], P["bg0_s"]),
                    ("hidden", P["gray"], P["bg_h"]), ("ignored", P["bg4"], P["bg_h"]), ("unreachable", P["gray"], P["bg_h"])]:
    for suf, v in status(fg, bg).items():
        ui[key + suf] = v

syntax = {
    "comment": st(P["gray"], "italic"), "comment.doc": st(P["gray"], "italic"),
    "string": st(P["green"]), "string.escape": st(P["orange"]), "string.regex": st(P["orange"]),
    "string.special": st(P["orange"]), "string.special.symbol": st(P["purple"]),
    "number": st(P["purple"]), "boolean": st(P["purple"]), "constant": st(P["purple"]),
    "keyword": st(P["red"]), "operator": st(P["orange"]), "preproc": st(P["aqua"]),
    "function": st(P["green"], None, 700), "function.builtin": st(P["green"], None, 700), "constructor": st(P["yellow"]),
    "type": st(P["yellow"]), "enum": st(P["yellow"]), "variant": st(P["purple"]), "namespace": st(P["aqua"]),
    "attribute": st(P["aqua"]), "label": st(P["aqua"]),
    "variable": st(P["fg"]), "variable.parameter": st(P["fg2"], "italic"), "variable.special": st(P["purple"], "italic"),
    "property": st(P["blue"]),
    "tag": st(P["aqua"]), "selector": st(P["aqua"]), "selector.pseudo": st(P["aqua"]),
    "punctuation": st(P["fg4"]), "punctuation.bracket": st(P["fg4"]), "punctuation.delimiter": st(P["fg4"]),
    "punctuation.special": st(P["orange"]), "punctuation.list_marker": st(P["aqua"]), "punctuation.markup": st(P["gray"]),
    "embedded": st(P["fg"]),
    # markdown
    "title": st(P["green"], None, 700), "emphasis": st(P["fg"], "italic"), "emphasis.strong": st(P["fg0"], None, 700),
    "text.literal": st(P["orange"]), "link_text": st(P["blue"]), "link_uri": st(P["blue"], "italic"),
    "primary": st(P["fg"]), "hint": st(P["gray"], "italic"), "predictive": st(P["bg4"], "italic"),
    "diff.plus": st(P["green"]), "diff.minus": st(P["red"]),
}

players = [{"cursor": A, "background": A, "selection": a(P["bg2"], "cc")}] + [
    {"cursor": c, "background": c, "selection": a(c, "33")} for c in (P["blue"], P["purple"], P["aqua"], P["orange"], P["yellow"], P["red"])]

style = {**ui, "accents": [P["green"], P["aqua"], P["blue"], P["purple"], P["orange"], P["yellow"], P["red"]],
         "players": players, "syntax": syntax}
style = {k: v for k, v in sorted(style.items(), key=lambda kv: kv[0] in ("accents", "players", "syntax"))}

theme = {"$schema": "https://zed.dev/schema/themes/v0.2.0.json", "name": "Gruvbox Cove", "author": "The Gruvbox Cove contributors",
         "themes": [{"name": "Gruvbox Cove", "appearance": "dark", "style": style}]}
out = pathlib.Path(__file__).with_name("themes") / "gruvbox-cove.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(theme, indent=2) + "\n", encoding="utf-8")
print("wrote", out, len(style), "keys")
