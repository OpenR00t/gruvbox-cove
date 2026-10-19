# Cove Sans

A proportional version of **CaskaydiaCove Nerd Font** (Cascadia Code + Nerd Fonts) for long-form reading. Same letters,
re-spaced; Nerd Font icons kept.

12 styles: ExtraLight, Light, SemiLight, Regular, SemiBold, Bold, each with an Italic (cursive italics, as in Cascadia).

## Install (Windows)
Select all 12 `.ttf` files → right-click → **Install for all users**. Restart the browser.

## Changes from CaskaydiaCove
- Every outline glyph re-spaced with FontForge auto-width (~12% em side bearings); space ~26% em. Nerd icons, box
  drawing and braille keep their widths; combining marks stay zero-width. Composite glyphs are flattened first so
  accents and quotes move with their letters.
- Programming ligatures (`calt`) removed: they assume mono cells. `->`, `!=`, `==` stay separate characters.
- Kerning added, tightening only (AV, To, Te, Ty, Wa, Yo…), never more than 5% em, and never before letters with a tall
  left edge (i j l b h k f t).
- Hinted with ttfautohint (Windows compatibility).
- Renamed to "Cove Sans": "Cascadia Code" is a Reserved Font Name under the OFL.

## Build
```
python build_cove.py <CaskaydiaCoveNerdFont-Style.ttf> <outdir>      # FontForge's Python
ttfautohint --windows-compatibility <outdir>/CoveSans-Style.raw.ttf CoveSans-Style.ttf
```

## License
SIL Open Font License 1.1, like the source font ([LICENSE.txt](LICENSE.txt)). Cascadia Code is Copyright (c) 2019 -
Present, Microsoft Corporation, with Reserved Font Name Cascadia Code. Modifications Copyright 2026 The Gruvbox Cove contributors.
The Nerd Font icon glyphs come from the Nerd Fonts project and keep their own licenses; see
<https://github.com/ryanoasis/nerd-fonts/blob/master/license-audit.md>.
