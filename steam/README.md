# Gruvbox Cove for Steam

Steam is themed through **Millennium** (steambrew.app) with kuska1's **Material-Theme**, which is actively maintained
and picks its colors from palette files in its folder. We overwrite its Green palette with gruvbox (`colors.css`)
instead of forking the theme, so Material-Theme's own updates keep Steam's ever-changing class names covered.

## Install
1. Install Millennium from steambrew.app, start Steam.
2. Steam → Millennium → Themes → install **Material** (Material-Theme by kuska1), click **Use**.
3. Run `install.ps1` (copies `colors.css` over the theme's `green.css` and `matugen.css`, and adds `customFont.css`).
4. In the theme's settings: **Appearance: Dark**, **Color: Green**, **Font: Custom**. Restart Steam once.

Use **Green**, not Matugen: Matugen loads its colors with a script that doesn't reach store and community pages,
so those stay stock Material while the library is gruvbox. Green is plain CSS and applies everywhere.

When Millennium updates Material-Theme, its own color files come back: run `install.ps1` again.

## Roles
Primary green `#b8bb26` (selection, buttons, progress), secondary aqua, tertiary blue, error red. Surfaces: bg0_h for
chrome, bg0 for content, bg0_s/bg1 for raised panels; text fg1, muted fg3; outlines bg4.

`python build_steam.py` regenerates `colors.css` from the role table.
