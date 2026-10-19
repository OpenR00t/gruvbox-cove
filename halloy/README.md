# Gruvbox Cove for Halloy (IRC)

1. Copy `gruvbox-cove.toml` to `%AppData%\halloy\themes\` (create `themes` if missing).
2. Merge `config-snippet.toml` into `%AppData%\halloy\config.toml` (`theme =` must sit above all `[sections]`).
3. Restart Halloy (font changes need a restart; themes reload live).

Roles: green = unread, focus and active borders; orange = mentions; aqua bold = nicks; gray = timestamps and joins/parts;
blue = links; orange = inline code. Nick colors come from a gruvbox palette. mIRC color codes map to gruvbox
(dark variants for the base colors, bright for the "light" ones).

Font: CaskaydiaCove Nerd Font Mono. Halloy uses one family for the whole chat, so Cove Sans isn't used here
(IRC lines are short and aligned, so mono reads best anyway).

Tweak live with Halloy's built-in theme editor (command bar → Theme editor), then save over this file.
