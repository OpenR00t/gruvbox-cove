# Copies the Gruvbox Cove colors and fonts into Millennium's Material-Theme folder.
# Run again after Millennium updates Material-Theme (an update restores its own color files).
#   powershell -ExecutionPolicy Bypass -File <path to this repo>\steam\install.ps1
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 The Gruvbox Cove contributors
$steam = (Get-ItemProperty 'HKCU:\Software\Valve\Steam' -ErrorAction SilentlyContinue).SteamPath
if (-not $steam) { $steam = 'C:\Program Files (x86)\Steam' }
$candidates = @("$steam\millennium\themes\Material-Theme", "$steam\steamui\skins\Material-Theme")
$theme = $candidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $theme) { Write-Error "Material-Theme not found. Install it from Millennium first (Steam > Millennium > Themes)."; exit 1 }
# Green slot = static CSS, applies to the client and store pages alike. Matugen slot too, in case it's picked.
Copy-Item "$PSScriptRoot\colors.css" "$theme\css\main\colors\green.css" -Force
Copy-Item "$PSScriptRoot\colors.css" "$theme\css\main\colors\matugen.css" -Force
Copy-Item "$PSScriptRoot\customFont.css" "$theme\customFont.css" -Force
Write-Host "Gruvbox Cove copied into $theme"
Write-Host "In Steam: Millennium > Themes > Material > Color: Green, Font: Custom, Appearance: Dark. Restart Steam to apply."
