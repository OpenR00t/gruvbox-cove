# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 The Gruvbox Cove contributors
"""Writes colors.css: the gruvbox palette as Material 3 color roles for kuska1's Material-Theme (Millennium).
install.ps1 copies it over the theme's green.css (Color: Green, static CSS: works in the client AND on store/community pages)
and matugen.css (Color: Matugen, client only: its fetch doesn't reach store pages).
Run: python build_steam.py"""
import pathlib

ROLES = {  # Material 3 role -> gruvbox (dark). Green is primary (the accent), aqua secondary, blue tertiary.
    "primary": "#b8bb26", "on-primary": "#1d2021", "primary-container": "#4a4d1a", "on-primary-container": "#ebdbb2",
    "primary-fixed": "#b8bb26", "primary-fixed-dim": "#98971a", "on-primary-fixed": "#1d2021", "on-primary-fixed-variant": "#3c3836",
    "inverse-primary": "#79740e", "surface-tint": "#b8bb26",
    "secondary": "#8ec07c", "on-secondary": "#1d2021", "secondary-container": "#504945", "on-secondary-container": "#ebdbb2",
    "secondary-fixed": "#8ec07c", "secondary-fixed-dim": "#689d6a", "on-secondary-fixed": "#1d2021", "on-secondary-fixed-variant": "#3c3836",
    "tertiary": "#83a598", "on-tertiary": "#1d2021", "tertiary-container": "#2e3b3b", "on-tertiary-container": "#ebdbb2",
    "tertiary-fixed": "#83a598", "tertiary-fixed-dim": "#458588", "on-tertiary-fixed": "#1d2021", "on-tertiary-fixed-variant": "#3c3836",
    "error": "#fb4934", "on-error": "#1d2021", "error-container": "#4a1f1b", "on-error-container": "#fbf1c7",
    # surfaces: chrome bg0_h, content bg0, then up the bg ramp
    "background": "#282828", "on-background": "#ebdbb2",
    "surface": "#282828", "on-surface": "#ebdbb2", "surface-variant": "#3c3836", "on-surface-variant": "#bdae93",
    "surface-dim": "#1d2021", "surface-bright": "#504945",
    "surface-container-lowest": "#1d2021", "surface-container-low": "#1d2021", "surface-container": "#282828",
    "surface-container-high": "#32302f", "surface-container-highest": "#3c3836",
    "inverse-surface": "#ebdbb2", "inverse-on-surface": "#282828",
    "outline": "#7c6f64", "outline-variant": "#504945", "shadow": "#000000", "scrim": "#000000",
}
rgb = lambda h: "rgb({}, {}, {})".format(*(int(h[i:i + 2], 16) for i in (1, 3, 5)))
lines = [f"    --md-sys-color-{k}: {rgb(v)};" for k, v in ROLES.items()]
css = (":root {\n    --theme-color: \"Gruvbox Cove\";\n    --hue-rotate: 270deg;\n\n"
       "    /* Gruvbox Cove palette for Material-Theme. Built by build_steam.py; edit the role table there. */\n    /* SPDX-License-Identifier: AGPL-3.0-or-later. Copyright (C) 2026 The Gruvbox Cove contributors */\n"
       + "\n".join(lines) + "\n}\n")
out = pathlib.Path(__file__).with_name("colors.css")
out.write_text(css, encoding="utf-8")
print("wrote", out, len(ROLES), "roles")
