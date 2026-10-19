# Gruvbox Cove

One Gruvbox dark look across editors, terminals, apps and websites: the same palette everywhere, **green** as the
primary accent (yellow only for warnings and types), and one type family:

- **CaskaydiaCove Nerd Font** (Cascadia Code + Nerd Font icons) for interface, headings and code
- **Cove Sans** (a proportional re-spacing of CaskaydiaCove, in [`fonts/`](fonts/)) at SemiLight for prose

## Palette

| Role | Color | | Role | Color |
|---|---|---|---|---|
| Background (chrome) | `#1d2021` bg0_h | | Text | `#ebdbb2` fg1 |
| Background (content) | `#282828` bg0 | | Muted text | `#a89984` fg4 |
| Raised panels | `#3c3836` bg1 | | Accent | `#b8bb26` green |
| Borders, selection | `#504945` bg2 | | Secondary accent | `#8ec07c` aqua |
| Comments, dim | `#928374` gray | | Links | `#83a598` blue |
| Warnings | `#fabd2f` yellow | | Errors | `#fb4934` red |

## What's here

| Folder | What | Install |
|---|---|---|
| [`vscode/`](vscode/) | VS Code color theme, settings snippet, Markdown preview CSS | Package with `vsce package` and install the `.vsix` |
| [`neovim/`](neovim/) | Colorscheme + lualine theme | See [`neovim/README.md`](neovim/README.md) |
| [`zed/`](zed/) | Zed theme (`build_zed.py`) | See [`zed/README.md`](zed/README.md) |
| [`notepadpp/`](notepadpp/) | Notepad++ theme for every language, plus Dark Mode tone values | See [`notepadpp/README.md`](notepadpp/README.md) |
| [`terminal/`](terminal/) | Windows Terminal scheme, PowerShell colors and prompt | See [`terminal/README.md`](terminal/README.md) |
| [`obsidian/`](obsidian/) | Obsidian theme (reading view in Cove Sans) | Copy `Gruvbox Cove/` into `<vault>/.obsidian/themes/` |
| [`discord/`](discord/) | Vencord / Vesktop theme | See [`discord/README.md`](discord/README.md) |
| [`halloy/`](halloy/) | Halloy IRC theme + config snippet | See [`halloy/README.md`](halloy/README.md) |
| [`steam/`](steam/) | Steam palette and fonts for Millennium's Material theme | See [`steam/README.md`](steam/README.md) |
| [`stylus/`](stylus/) | GitHub, YouTube, DuckDuckGo styles and a global font style | Stylus → Write new style → paste |
| [`reddit/`](reddit/) | Old reddit theme for RES, auto-expand userscript | RES → Stylesheet Loader → Snippets; userscript manager |
| [`wikipedia/`](wikipedia/) | Wikipedia (Vector 2022) theme | Paste into `meta.wikimedia.org/wiki/Special:MyPage/global.css` |
| [`fonts/`](fonts/) | Cove Sans (12 styles) and its build scripts | Install the `.ttf` files |

The GitHub, YouTube, DuckDuckGo and Discord themes are built from [Catppuccin](https://github.com/catppuccin)'s
maintained themes with the gruvbox palette swapped in; their build scripts pull Catppuccin's latest when a site changes.

## License

Licensed under the GNU Affero General Public License v3.0 or later. See [LICENSE](LICENSE).

Exceptions, each marked with an SPDX header:
- **Catppuccin-based themes** (`stylus/gruvbox-cove-{github,youtube,duckduckgo}.user.css`, `stylus/build/shim.less`,
  `discord/`) stay under the MIT License of the Catppuccin projects they're built from
  ([`LICENSES/MIT-Catppuccin-userstyles.txt`](LICENSES/MIT-Catppuccin-userstyles.txt),
  [`LICENSES/MIT-Catppuccin-discord.txt`](LICENSES/MIT-Catppuccin-discord.txt)).
- **Cove Sans** (`fonts/cove-sans/`) is under the SIL Open Font License 1.1, as is Cascadia Code, which it is derived from
  ([`fonts/cove-sans/LICENSE.txt`](fonts/cove-sans/LICENSE.txt)).
