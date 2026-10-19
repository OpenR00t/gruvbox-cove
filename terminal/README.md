# Gruvbox Cove for Windows Terminal + PowerShell

1. **Color scheme**: copy `gruvbox-cove.fragment.json` to
   `%LOCALAPPDATA%\Microsoft\Windows Terminal\Fragments\Gruvbox Cove\gruvbox-cove.json`
   (create the folders). Windows Terminal loads it on start; the scheme appears as "Gruvbox Cove".
2. **Window chrome + defaults**: merge `windows-terminal-settings-snippet.jsonc` into Windows Terminal's `settings.json`
   (tab bar bg0_h, active tab bg0, scheme as default for every profile).
3. **Font**: set **CaskaydiaCove Nerd Font Mono** yourself (Settings → Defaults → Appearance → Font face).
4. **PowerShell colors + prompt**: add to your profile (`notepad $PROFILE`):
   `. "<path to this repo>\terminal\gruvbox-cove.profile.ps1"`
   Typing colors (PSReadLine), output/table/file colors (PowerShell 7.2+), and a prompt: blue folder path, purple git branch, green ❯ (red after a failed command).

ANSI colors 0–15 match Neovim's `terminal_color_*` and VS Code's integrated terminal.
