# Gruvbox Cove for Zed

1. Copy `themes/gruvbox-cove.json` to `%APPDATA%\Zed\themes\` (create `themes` if missing). Zed picks it up live.
2. Merge `settings-snippet.jsonc` into Zed's `settings.json`, or pick it from the theme selector (Ctrl+K Ctrl+T).

Matches the VS Code theme: chrome on bg0_h, editor on bg0, current line bg0_s, green cursor, active line number,
focus borders, search matches and bracket highlight; same syntax roles (keywords red, strings green, functions green bold,
types yellow, properties blue, imports/tags aqua, numbers purple, comments gray italic). Terminal uses the Windows Terminal scheme.

Zed draws markdown preview in the UI font, so Cove Sans isn't used here.

## Rebuilding
`python build_zed.py` regenerates the theme from the palette at the top of the script.
