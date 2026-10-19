# Gruvbox Cove for Neovim

Copy into your Neovim config (`%LOCALAPPDATA%\nvim\`):
- `colors\gruvbox-cove.lua` → `%LOCALAPPDATA%\nvim\colors\`
- `lua\lualine\themes\gruvbox-cove.lua` → `%LOCALAPPDATA%\nvim\lua\lualine\themes\` (only if you use lualine)

Then in `init.lua`:
```lua
vim.cmd.colorscheme("gruvbox-cove")
-- lualine users:  require("lualine").setup({ options = { theme = "gruvbox-cove" } })
```

Font: Neovim in a terminal uses the terminal's font, so set **CaskaydiaCove Nerd Font Mono** in Windows Terminal. In Neovide, the colorscheme sets it.
Needs Neovim 0.9+ (`termguicolors`, treesitter `@` groups).
