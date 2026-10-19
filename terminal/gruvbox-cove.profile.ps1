# Gruvbox Cove — PowerShell colors and prompt
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 The Gruvbox Cove contributors
# Dot-source from your profile:   . "<path to this repo>\terminal\gruvbox-cove.profile.ps1"
# (open your profile with:  notepad $PROFILE)
# Works in Windows PowerShell 5.1 and PowerShell 7. Font: CaskaydiaCove Nerd Font Mono.

$global:GC = @{
  bg_h='#1d2021'; bg0='#282828'; bg1='#3c3836'; bg2='#504945'; bg4='#7c6f64'
  fg0='#fbf1c7'; fg='#ebdbb2'; fg2='#d5c4a1'; fg3='#bdae93'; gray='#928374'
  red='#fb4934'; green='#b8bb26'; yellow='#fabd2f'; blue='#83a598'; purple='#d3869b'; aqua='#8ec07c'; orange='#fe8019'
}
function global:GcFg([string]$hex) {
  $h = $hex.TrimStart('#')
  $r = [Convert]::ToByte($h.Substring(0,2),16); $g = [Convert]::ToByte($h.Substring(2,2),16); $b = [Convert]::ToByte($h.Substring(4,2),16)
  "$([char]27)[38;2;$r;$g;${b}m"
}
function global:GcBg([string]$hex) { (GcFg $hex) -replace '\[38;', '[48;' }

# ---------- Syntax colors while typing (PSReadLine) ----------
if (Get-Module -ListAvailable PSReadLine) {
  $colors = @{
    Command   = GcFg $GC.aqua
    Parameter = GcFg $GC.blue
    Operator  = GcFg $GC.orange
    Variable  = GcFg $GC.purple
    String    = GcFg $GC.green
    Number    = GcFg $GC.purple
    Type      = GcFg $GC.yellow
    Member    = GcFg $GC.fg2
    Keyword   = GcFg $GC.red
    Comment   = GcFg $GC.gray
    Default   = GcFg $GC.fg
    Emphasis  = GcFg $GC.green
    Error     = GcFg $GC.red
    Selection = (GcBg $GC.bg2) + (GcFg $GC.fg0)
    ContinuationPrompt = GcFg $GC.bg4
  }
  $psrl = (Get-Module PSReadLine).Version
  if (-not $psrl) { $psrl = (Get-Module -ListAvailable PSReadLine | Sort-Object Version -Descending | Select-Object -First 1).Version }
  if ($psrl -ge [version]'2.1.0') {
    $colors.InlinePrediction = GcFg $GC.bg4
  }
  if ($psrl -ge [version]'2.2.0') {
    $colors.ListPrediction         = GcFg $GC.aqua
    $colors.ListPredictionSelected = GcBg $GC.bg1
  }
  Set-PSReadLineOption -Colors $colors
}

# ---------- Output formatting (PowerShell 7.2+) ----------
if ($PSVersionTable.PSVersion -ge [version]'7.2' -and $PSStyle) {
  $PSStyle.Formatting.TableHeader   = (GcFg $GC.green) + $PSStyle.Bold
  $PSStyle.Formatting.FormatAccent  = GcFg $GC.green
  $PSStyle.Formatting.ErrorAccent   = GcFg $GC.red
  $PSStyle.Formatting.Error         = GcFg $GC.red
  $PSStyle.Formatting.Warning       = GcFg $GC.yellow
  $PSStyle.Formatting.Verbose       = GcFg $GC.blue
  $PSStyle.Formatting.Debug         = GcFg $GC.aqua
  $PSStyle.Formatting.CustomTableHeaderLabel = (GcFg $GC.aqua) + $PSStyle.Italic
  $PSStyle.Progress.Style           = GcFg $GC.green
  $PSStyle.FileInfo.Directory       = (GcFg $GC.blue) + $PSStyle.Bold
  $PSStyle.FileInfo.SymbolicLink    = GcFg $GC.aqua
  $PSStyle.FileInfo.Executable      = GcFg $GC.green
  foreach ($ext in '.zip','.7z','.tar','.gz','.rar') { $PSStyle.FileInfo.Extension[$ext] = GcFg $GC.orange }
  foreach ($ext in '.ps1','.psm1','.psd1','.bat','.cmd') { $PSStyle.FileInfo.Extension[$ext] = GcFg $GC.green }
}

# ---------- Prompt ----------
#   ~\Projects\Themeing  main  ❯      (arrow green, red after a failed command)
function global:prompt {
  $ok = $?
  $esc = [char]27
  $reset = "$esc[0m"
  $path = $executionContext.SessionState.Path.CurrentLocation.Path
  if ($path.StartsWith($HOME, [StringComparison]::OrdinalIgnoreCase)) { $path = '~' + $path.Substring($HOME.Length) }
  $branch = ''
  if (Get-Command git -ErrorAction SilentlyContinue) {
    $b = git rev-parse --abbrev-ref HEAD 2>$null
    if ($LASTEXITCODE -eq 0 -and $b) { $branch = " $(GcFg $GC.purple)$([char]0xE0A0) $b$reset" }
  }
  $arrow = if ($ok) { GcFg $GC.green } else { GcFg $GC.red }
  "$(GcFg $GC.blue)$([char]0xF07B) $path$reset$branch $arrow$([char]0x276F)$reset "
}
