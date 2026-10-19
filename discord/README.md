# Gruvbox Cove for Discord (Vencord / Vesktop)

`gruvbox-cove.theme.css` — Gruvbox dark, green accent, CaskaydiaCove interface, Cove Sans SemiLight messages,
gruvbox syntax colors in code blocks. Works with every Discord appearance setting (dark, light, darker, midnight).

## Install
1. Vencord: Settings → **Vencord → Themes → Open Themes Folder** (`%APPDATA%\Vencord\themes`;
   Vesktop: `%APPDATA%\vesktop\themes`).
2. Copy `gruvbox-cove.theme.css` there.
3. Back in **Themes**, tick **Gruvbox Cove**.

Client mods are against Discord's terms; enforcement has been rare. Your call.

## Rebuilding
Discord changes its markup often. `build\build.py` clones Catppuccin's latest Discord theme, compiles it with
`build\_gruvbox.scss` (Catppuccin role names → gruvbox colors, same mapping as the Stylus builds) and
`build\gruvbox-cove.theme.scss` (brand = green, all appearance modes), then re-adds the header and `build\extras.css`
(fonts + code colors). Needs git and Node.

Built from catppuccin/discord, MIT License, Copyright (c) 2022 Catppuccin.
