-- SPDX-License-Identifier: AGPL-3.0-or-later
-- Copyright (C) 2026 The Gruvbox Cove contributors
-- lualine theme for Gruvbox Cove: mode colors use the palette, normal = green
local p = { bg_h = "#1d2021", bg0 = "#282828", bg1 = "#3c3836", bg2 = "#504945", fg = "#ebdbb2", fg3 = "#bdae93", gray = "#928374",
  green = "#b8bb26", blue = "#83a598", purple = "#d3869b", aqua = "#8ec07c", orange = "#fe8019", red = "#fb4934" }
local function mode(c)
  return { a = { fg = p.bg_h, bg = c, gui = "bold" }, b = { fg = p.fg, bg = p.bg2 }, c = { fg = p.fg3, bg = p.bg_h } }
end
return {
  normal = mode(p.green), insert = mode(p.blue), visual = mode(p.purple), replace = mode(p.red),
  command = mode(p.aqua), terminal = mode(p.orange),
  inactive = { a = { fg = p.gray, bg = p.bg_h }, b = { fg = p.gray, bg = p.bg_h }, c = { fg = p.gray, bg = p.bg_h } },
}
