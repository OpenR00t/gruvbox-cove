-- SPDX-License-Identifier: AGPL-3.0-or-later
-- Copyright (C) 2026 The Gruvbox Cove contributors
-- Gruvbox Cove — Neovim colorscheme
-- Gruvbox dark: green is the primary accent (cursor line number,
-- selection borders, search), yellow only for warnings and types.
-- Matches the reddit, Wikipedia, Obsidian, VS Code and terminal themes.
-- Use: :colorscheme gruvbox-cove   (font comes from the terminal / GUI)

vim.cmd("highlight clear")
if vim.fn.exists("syntax_on") == 1 then vim.cmd("syntax reset") end
vim.o.background = "dark"
vim.o.termguicolors = true
vim.g.colors_name = "gruvbox-cove"

local p = {
  bg_h = "#1d2021", bg0 = "#282828", bg0_s = "#32302f", bg1 = "#3c3836", bg2 = "#504945", bg3 = "#665c54", bg4 = "#7c6f64",
  fg0 = "#fbf1c7", fg = "#ebdbb2", fg2 = "#d5c4a1", fg3 = "#bdae93", fg4 = "#a89984", gray = "#928374",
  red = "#fb4934", green = "#b8bb26", yellow = "#fabd2f", blue = "#83a598", purple = "#d3869b", aqua = "#8ec07c", orange = "#fe8019",
  red_d = "#cc241d", green_d = "#98971a", yellow_d = "#d79921", blue_d = "#458588", purple_d = "#b16286", aqua_d = "#689d6a", orange_d = "#d65d0e",
  none = "NONE",
}

local function hl(group, opts) vim.api.nvim_set_hl(0, group, opts) end
local function link(group, to) vim.api.nvim_set_hl(0, group, { link = to }) end

-- ---------- Editor UI ----------
hl("Normal",        { fg = p.fg, bg = p.bg0 })
hl("NormalNC",      { fg = p.fg, bg = p.bg0 })
hl("NormalFloat",   { fg = p.fg, bg = p.bg_h })
hl("FloatBorder",   { fg = p.bg3, bg = p.bg_h })
hl("FloatTitle",    { fg = p.green, bg = p.bg_h, bold = true })
hl("Cursor",        { fg = p.bg0, bg = p.green })
link("lCursor", "Cursor"); link("TermCursor", "Cursor")
hl("CursorLine",    { bg = p.bg0_s })
hl("CursorColumn",  { bg = p.bg0_s })
hl("ColorColumn",   { bg = p.bg0_s })
hl("CursorLineNr",  { fg = p.green, bg = p.bg0_s, bold = true })
hl("LineNr",        { fg = p.bg4 })
hl("SignColumn",    { bg = p.bg0 })
hl("FoldColumn",    { fg = p.bg4, bg = p.bg0 })
hl("Folded",        { fg = p.gray, bg = p.bg1, italic = true })
hl("WinSeparator",  { fg = p.bg1 })
link("VertSplit", "WinSeparator")
hl("StatusLine",    { fg = p.fg3, bg = p.bg_h })
hl("StatusLineNC",  { fg = p.bg4, bg = p.bg_h })
hl("WinBar",        { fg = p.fg3, bg = p.bg0 })
hl("WinBarNC",      { fg = p.bg4, bg = p.bg0 })
hl("TabLine",       { fg = p.gray, bg = p.bg_h })
hl("TabLineFill",   { bg = p.bg_h })
hl("TabLineSel",    { fg = p.fg0, bg = p.bg0, bold = true, underline = true, sp = p.green })
hl("Pmenu",         { fg = p.fg, bg = p.bg_h })
hl("PmenuSel",      { fg = p.fg0, bg = p.bg2, bold = true })
hl("PmenuSbar",     { bg = p.bg1 })
hl("PmenuThumb",    { bg = p.bg3 })
hl("PmenuMatch",    { fg = p.green, bold = true })
hl("PmenuMatchSel", { fg = p.green, bg = p.bg2, bold = true })
hl("Visual",        { bg = p.bg2 })
hl("VisualNOS",     { bg = p.bg2 })
hl("Search",        { fg = p.bg0, bg = p.green_d })
hl("CurSearch",     { fg = p.bg0, bg = p.green, bold = true })
hl("IncSearch",     { fg = p.bg0, bg = p.green, bold = true })
link("Substitute", "IncSearch")
hl("MatchParen",    { bg = p.bg2, bold = true, underline = true, sp = p.green })
hl("NonText",       { fg = p.bg2 })
hl("Whitespace",    { fg = p.bg2 })
hl("SpecialKey",    { fg = p.bg3 })
hl("EndOfBuffer",   { fg = p.bg0 })
hl("Conceal",       { fg = p.gray })
hl("Directory",     { fg = p.blue, bold = true })
hl("Title",         { fg = p.green, bold = true })
hl("ErrorMsg",      { fg = p.red, bold = true })
hl("WarningMsg",    { fg = p.yellow, bold = true })
hl("MoreMsg",       { fg = p.green, bold = true })
hl("ModeMsg",       { fg = p.green, bold = true })
hl("Question",      { fg = p.aqua, bold = true })
hl("QuickFixLine",  { bg = p.bg1, bold = true })
hl("WildMenu",      { fg = p.fg0, bg = p.bg2 })
hl("SpellBad",      { undercurl = true, sp = p.red })
hl("SpellCap",      { undercurl = true, sp = p.blue })
hl("SpellLocal",    { undercurl = true, sp = p.aqua })
hl("SpellRare",     { undercurl = true, sp = p.purple })
hl("DiffAdd",       { bg = "#32361a" })
hl("DiffChange",    { bg = "#2c3534" })
hl("DiffDelete",    { fg = p.red, bg = "#3c1f1e" })
hl("DiffText",      { bg = "#3a4a46", bold = true })
link("Added", "DiffAdd"); hl("Removed", { fg = p.red }); hl("Changed", { fg = p.blue })

-- ---------- Syntax (classic gruvbox mapping) ----------
hl("Comment",       { fg = p.gray, italic = true })
hl("Constant",      { fg = p.purple })
hl("String",        { fg = p.green })
hl("Character",     { fg = p.purple })
hl("Number",        { fg = p.purple })
hl("Boolean",       { fg = p.purple })
hl("Float",         { fg = p.purple })
hl("Identifier",    { fg = p.blue })
hl("Function",      { fg = p.green, bold = true })
hl("Statement",     { fg = p.red })
hl("Conditional",   { fg = p.red })
hl("Repeat",        { fg = p.red })
hl("Label",         { fg = p.red })
hl("Operator",      { fg = p.orange })
hl("Keyword",       { fg = p.red })
hl("Exception",     { fg = p.red })
hl("PreProc",       { fg = p.aqua })
hl("Include",       { fg = p.aqua })
hl("Define",        { fg = p.aqua })
hl("Macro",         { fg = p.aqua })
hl("PreCondit",     { fg = p.aqua })
hl("Type",          { fg = p.yellow })
hl("StorageClass",  { fg = p.orange })
hl("Structure",     { fg = p.aqua })
hl("Typedef",       { fg = p.yellow })
hl("Special",       { fg = p.orange })
hl("SpecialChar",   { fg = p.orange })
hl("Tag",           { fg = p.aqua })
hl("Delimiter",     { fg = p.fg4 })
hl("SpecialComment",{ fg = p.gray, bold = true })
hl("Debug",         { fg = p.red })
hl("Underlined",    { fg = p.blue, underline = true })
hl("Error",         { fg = p.red, bold = true })
hl("Todo",          { fg = p.bg0, bg = p.green_d, bold = true })

-- ---------- Diagnostics ----------
hl("DiagnosticError", { fg = p.red })
hl("DiagnosticWarn",  { fg = p.yellow })
hl("DiagnosticInfo",  { fg = p.blue })
hl("DiagnosticHint",  { fg = p.aqua })
hl("DiagnosticOk",    { fg = p.green })
hl("DiagnosticUnderlineError", { undercurl = true, sp = p.red })
hl("DiagnosticUnderlineWarn",  { undercurl = true, sp = p.yellow })
hl("DiagnosticUnderlineInfo",  { undercurl = true, sp = p.blue })
hl("DiagnosticUnderlineHint",  { undercurl = true, sp = p.aqua })
hl("DiagnosticVirtualTextError", { fg = p.red, bg = "#32201f", italic = true })
hl("DiagnosticVirtualTextWarn",  { fg = p.yellow, bg = "#332c1c", italic = true })
hl("DiagnosticVirtualTextInfo",  { fg = p.blue, bg = "#252d2c", italic = true })
hl("DiagnosticVirtualTextHint",  { fg = p.aqua, bg = "#262f26", italic = true })
hl("DiagnosticUnnecessary", { fg = p.gray })
hl("LspReferenceText",  { bg = p.bg1 })
hl("LspReferenceRead",  { bg = p.bg1 })
hl("LspReferenceWrite", { bg = p.bg2 })
hl("LspInlayHint",      { fg = p.gray, bg = p.bg0_s, italic = true })
hl("LspSignatureActiveParameter", { fg = p.green, bold = true, underline = true })
hl("LspCodeLens",       { fg = p.gray })

-- ---------- Treesitter ----------
local ts = {
  ["@comment"] = "Comment", ["@comment.todo"] = "Todo", ["@comment.error"] = "DiagnosticError",
  ["@comment.warning"] = "DiagnosticWarn", ["@comment.note"] = "DiagnosticInfo",
  ["@string"] = "String", ["@string.escape"] = "SpecialChar", ["@string.regexp"] = "SpecialChar", ["@string.special"] = "Special",
  ["@character"] = "Character", ["@number"] = "Number", ["@number.float"] = "Float", ["@boolean"] = "Boolean",
  ["@constant"] = "Constant", ["@constant.builtin"] = "Constant", ["@constant.macro"] = "Macro",
  ["@function"] = "Function", ["@function.call"] = "Function", ["@function.method"] = "Function", ["@function.method.call"] = "Function",
  ["@function.macro"] = "Macro", ["@constructor"] = "Type",
  ["@keyword"] = "Keyword", ["@keyword.function"] = "Keyword", ["@keyword.return"] = "Keyword", ["@keyword.conditional"] = "Conditional",
  ["@keyword.repeat"] = "Repeat", ["@keyword.exception"] = "Exception", ["@keyword.import"] = "Include", ["@keyword.directive"] = "PreProc",
  ["@keyword.operator"] = "Operator", ["@operator"] = "Operator",
  ["@type"] = "Type", ["@type.builtin"] = "Type", ["@type.definition"] = "Typedef", ["@attribute"] = "PreProc", ["@module"] = "Structure",
  ["@property"] = "Identifier", ["@variable.member"] = "Identifier",
  ["@punctuation"] = "Delimiter", ["@punctuation.bracket"] = "Delimiter", ["@punctuation.delimiter"] = "Delimiter", ["@punctuation.special"] = "Special",
  ["@tag"] = "Tag", ["@tag.attribute"] = "Type", ["@tag.delimiter"] = "Delimiter",
  ["@markup.heading"] = "Title", ["@markup.link"] = "Underlined", ["@markup.link.url"] = "Underlined", ["@markup.raw"] = "Special",
  ["@markup.list"] = "PreProc", ["@diff.plus"] = "Added", ["@diff.minus"] = "Removed", ["@diff.delta"] = "Changed",
}
for k, v in pairs(ts) do link(k, v) end
hl("@variable",            { fg = p.fg })
hl("@variable.builtin",    { fg = p.purple, italic = true })
hl("@variable.parameter",  { fg = p.fg2, italic = true })
hl("@markup.strong",       { fg = p.fg0, bold = true })
hl("@markup.italic",       { italic = true })
hl("@markup.strikethrough",{ strikethrough = true })
hl("@markup.quote",        { fg = p.fg3, italic = true })
hl("@markup.heading.2",    { fg = p.green, bold = true })
hl("@markup.heading.3",    { fg = p.aqua, bold = true })
hl("@markup.heading.4",    { fg = p.blue, bold = true })
hl("@markup.heading.1",    { fg = p.fg0, bold = true })
-- LSP semantic tokens follow the same links
link("@lsp.type.function", "Function"); link("@lsp.type.method", "Function"); link("@lsp.type.type", "Type")
link("@lsp.type.class", "Type"); link("@lsp.type.enum", "Type"); link("@lsp.type.interface", "Type")
link("@lsp.type.namespace", "Structure"); link("@lsp.type.parameter", "@variable.parameter"); link("@lsp.type.property", "Identifier")
link("@lsp.type.variable", "@variable"); link("@lsp.type.enumMember", "Constant"); link("@lsp.type.macro", "Macro")

-- ---------- Common plugins ----------
hl("GitSignsAdd",    { fg = p.green })
hl("GitSignsChange", { fg = p.blue })
hl("GitSignsDelete", { fg = p.red })
hl("TelescopeNormal",       { fg = p.fg, bg = p.bg_h })
hl("TelescopeBorder",       { fg = p.bg3, bg = p.bg_h })
hl("TelescopePromptBorder", { fg = p.green, bg = p.bg_h })
hl("TelescopeTitle",        { fg = p.green, bold = true })
hl("TelescopeSelection",    { fg = p.fg0, bg = p.bg1, bold = true })
hl("TelescopeMatching",     { fg = p.green, bold = true })
hl("CmpItemAbbrMatch",      { fg = p.green, bold = true })
hl("CmpItemAbbrMatchFuzzy", { fg = p.green })
hl("CmpItemKind",           { fg = p.aqua })
hl("CmpItemMenu",           { fg = p.gray })
hl("NvimTreeNormal",        { fg = p.fg3, bg = p.bg_h })
hl("NvimTreeFolderName",    { fg = p.blue })
hl("NvimTreeOpenedFolderName", { fg = p.blue, bold = true })
hl("NeoTreeNormal",         { fg = p.fg3, bg = p.bg_h })
hl("NeoTreeNormalNC",       { fg = p.fg3, bg = p.bg_h })
hl("WhichKey",              { fg = p.green })
hl("WhichKeyGroup",         { fg = p.aqua })
hl("WhichKeyDesc",          { fg = p.fg })
hl("IblIndent",             { fg = p.bg1 })
hl("IblScope",              { fg = p.bg3 })

-- ---------- Terminal colors (match the Windows Terminal scheme) ----------
local term = { p.bg0, p.red_d, p.green_d, p.yellow_d, p.blue_d, p.purple_d, p.aqua_d, p.fg4,
               p.gray, p.red, p.green, p.yellow, p.blue, p.purple, p.aqua, p.fg }
for i, c in ipairs(term) do vim.g["terminal_color_" .. (i - 1)] = c end

-- Neovide (GUI) font: CaskaydiaCove Mono keeps Nerd icons in single cells
if vim.g.neovide then
  vim.o.guifont = "CaskaydiaCove Nerd Font Mono:h12"
end
