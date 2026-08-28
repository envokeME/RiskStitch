param(
  [Parameter(Position = 0)]
  [string]$Target = $env:RISKSTITCH_FABRIC_PATTERNS_DIR,
  [switch]$Force
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Target)) {
  throw "Usage: ./scripts/install.ps1 -Target <fabric-custom-patterns-directory> [-Force]"
}

$RepoDir = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$TargetFull = [System.IO.Path]::GetFullPath($Target)
$HomeFull = [System.IO.Path]::GetFullPath($HOME)

if ($TargetFull -eq [System.IO.Path]::GetPathRoot($TargetFull) -or $TargetFull -eq $HomeFull -or $TargetFull -eq $RepoDir) {
  throw "Refusing unsafe target: $TargetFull"
}

New-Item -ItemType Directory -Path $TargetFull -Force | Out-Null
$Installed = 0
$Skipped = 0

Get-ChildItem (Join-Path $RepoDir "patterns") -Directory -Filter "grc_*" | ForEach-Object {
  $Destination = Join-Path $TargetFull $_.Name
  if ((Test-Path $Destination) -and -not $Force) {
    Write-Output "skip $($_.Name) (already exists; use -Force to replace system.md)"
    $Skipped++
  } else {
    New-Item -ItemType Directory -Path $Destination -Force | Out-Null
    Copy-Item (Join-Path $_.FullName "system.md") (Join-Path $Destination "system.md") -Force
    Write-Output "install $($_.Name)"
    $Installed++
  }
}

Write-Output "Installed: $Installed; skipped: $Skipped; target: $TargetFull"
