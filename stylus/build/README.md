# Rebuilding the Catppuccin-based styles

GitHub, YouTube and DuckDuckGo change their markup often. These three styles reuse Catppuccin's maintained userstyles
(MIT, see `LICENSES/MIT-Catppuccin-userstyles.txt` at the repo root) and swap in the gruvbox palette through `shim.less`.

When something stops being themed:
1. `python build.py` (needs Python and Node). It downloads Catppuccin's latest templates, compiles them with the shim,
   maps GitHub's leftover default colors to gruvbox, and rewrites the `.user.css` files, keeping their headers and
   font-rule sections.
2. Bump `@version` in the changed file and reinstall it in Stylus.

`shim.less` holds the role mapping (Catppuccin name → gruvbox color, accent = green).

`build_fonts.py` writes `../gruvbox-cove-fonts.user.css` from `themed-sites.txt`; see the comment at its top.
