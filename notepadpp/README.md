# Gruvbox Cove for Notepad++

## 1. Editor theme (colors + font)
1. Copy `Gruvbox Cove.xml` to `%APPDATA%\Notepad++\themes\` (create `themes` if missing).
   Portable install: the `themes` folder next to `notepad++.exe` instead.
2. Restart Notepad++ → **Settings → Style Configurator → Select theme: Gruvbox Cove** → Save & Close.

Covers all 93 languages and every global style (caret green, current line `#32302f`, selection `#504945`,
active tab indicator green, find marks dark green, line numbers `#7c6f64`). Font: **CaskaydiaCove Nerd Font 11**,
set in Global Styles → Default Style; change the size there if you want.

## 2. Menus, tabs and toolbars (Dark Mode)
The theme file can't color Notepad++'s window. Set it once:
**Settings → Preferences → Dark Mode → Enable dark mode → Customized tone**, then click each swatch and enter:

The swatches open the Windows color dialog, which takes **Red / Green / Blue** numbers, not hex:

| Swatch | Red | Green | Blue | Hex | Gruvbox |
|---|---|---|---|---|---|
| Top | 29 | 32 | 33 | `#1D2021` | bg0_h |
| Menu hot track | 60 | 56 | 54 | `#3C3836` | bg1 |
| Active | 40 | 40 | 40 | `#282828` | bg0 |
| Main | 29 | 32 | 33 | `#1D2021` | bg0_h |
| Error | 251 | 73 | 52 | `#FB4934` | red |
| Text | 235 | 219 | 178 | `#EBDBB2` | fg1 |
| Darker text | 168 | 153 | 132 | `#A89984` | fg4 |
| Disabled text | 102 | 92 | 84 | `#665C54` | bg3 |
| Link | 131 | 165 | 152 | `#83A598` | blue |
| Edge | 60 | 56 | 54 | `#3C3836` | bg1 |
| Hot edge | 184 | 187 | 38 | `#B8BB26` | green |
| Disabled edge | 80 | 73 | 69 | `#504945` | bg2 |

Notepad++ remembers a theme per mode: after turning on Dark Mode, re-select **Gruvbox Cove** in the Style Configurator.

## 3. Optional
- Ligatures: Settings → Preferences → MISC. → **Use DirectWrite** (restart), then Cascadia's ligatures render.

## Rebuilding
`build_npp.py` regenerates the theme from Notepad++'s `stylers.model.xml` (newer versions add languages):
```
python build_npp.py stylers.model.xml "Gruvbox Cove.xml"
```
Get `stylers.model.xml` from the Notepad++ install folder or the notepad-plus-plus GitHub repo (`PowerEditor/src/`).
Styles are colored by name (comment, string, keyword, type, function…), matching the VS Code and Neovim themes.
