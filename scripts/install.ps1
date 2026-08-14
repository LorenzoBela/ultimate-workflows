# Ultimate Workflows - Windows PowerShell Installer
# Usage:
#   .\scripts\install.ps1 -Target cursor
#   .\scripts\install.ps1 -Target claude
#   .\scripts\install.ps1 -Target agy
#   .\scripts\install.ps1 -Target windsurf
#   .\scripts\install.ps1 -Target cline
#   .\scripts\install.ps1 -Target copilot
#   .\scripts\install.ps1 -Target all

param (
    [string]$Target = "all"
)

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Split-Path -Parent $ScriptDir
$UniversalDir = Join-Path $RootDir "universal"
$DestDir = Get-Location

Write-Host "`n⚡ Installing Ultimate Workflows to target: [$Target] in $DestDir" -ForegroundColor Cyan

$mdFiles = Get-ChildItem -Path $UniversalDir -Filter "*.md" | Where-Object { $_.Name -ne "README.md" }

function Install-Cursor {
    Write-Host "📦 Installing Cursor rules (.cursor/rules/)..." -ForegroundColor Yellow
    $dest = Join-Path $DestDir ".cursor\rules"
    if (!(Test-Path $dest)) { New-Item -ItemType Directory -Path $dest -Force | Out-Null }
    
    foreach ($file in $mdFiles) {
        $base = $file.BaseName
        $content = Get-Content $file.FullName -Raw
        $body = $content -replace '^---[\s\S]*?---\r?\n', ''
        $header = "---`ndescription: $base`nglobs: *`nalwaysApply: false`n---`n`n"
        Set-Content -Path (Join-Path $dest "$base.mdc") -Value ($header + $body) -Encoding UTF8
    }
    Write-Host "✓ Cursor rules installed ($($mdFiles.Count) rules)." -ForegroundColor Green
}

function Install-Claude {
    Write-Host "📦 Installing Claude Code skills (.claude/skills/)..." -ForegroundColor Yellow
    $dest = Join-Path $DestDir ".claude\skills"
    if (!(Test-Path $dest)) { New-Item -ItemType Directory -Path $dest -Force | Out-Null }
    Copy-Item "$UniversalDir\*.md" -Destination $dest -Force
    if (Test-Path "$dest\README.md") { Remove-Item "$dest\README.md" -Force }
    Write-Host "✓ Claude Code skills installed ($($mdFiles.Count) skills)." -ForegroundColor Green
}

function Install-AGY {
    Write-Host "📦 Installing Antigravity workflows (.agent/workflows/)..." -ForegroundColor Yellow
    $dest = Join-Path $DestDir ".agent\workflows"
    if (!(Test-Path $dest)) { New-Item -ItemType Directory -Path $dest -Force | Out-Null }
    Copy-Item "$UniversalDir\*.md" -Destination $dest -Force
    if (Test-Path "$dest\README.md") { Remove-Item "$dest\README.md" -Force }
    Write-Host "✓ Antigravity workflows installed ($($mdFiles.Count) workflows)." -ForegroundColor Green
}

function Install-Windsurf {
    Write-Host "📦 Installing Windsurf rulebook (.windsurfrules)..." -ForegroundColor Yellow
    $dest = Join-Path $DestDir ".windsurfrules"
    $combined = "# Windsurf Global Rulebook (Ultimate Workflows)`n`n"
    foreach ($file in $mdFiles) {
        $text = Get-Content $file.FullName -Raw
        $combined += "`n<!-- Workflow: $($file.Name) -->`n$text`n`n---`n"
    }
    Set-Content -Path $dest -Value $combined -Encoding UTF8
    Write-Host "✓ Windsurf rulebook generated." -ForegroundColor Green
}

function Install-Cline {
    Write-Host "📦 Installing Cline rules (.clinerules)..." -ForegroundColor Yellow
    $dest = Join-Path $DestDir ".clinerules"
    $combined = "# Cline Master Workflows (Ultimate Workflows)`n`n"
    foreach ($file in $mdFiles) {
        $text = Get-Content $file.FullName -Raw
        $combined += "`n<!-- Workflow: $($file.Name) -->`n$text`n`n---`n"
    }
    Set-Content -Path $dest -Value $combined -Encoding UTF8
    Write-Host "✓ Cline rules generated." -ForegroundColor Green
}

function Install-Copilot {
    Write-Host "📦 Installing GitHub Copilot instructions (.github/copilot-instructions.md)..." -ForegroundColor Yellow
    $destFolder = Join-Path $DestDir ".github"
    if (!(Test-Path $destFolder)) { New-Item -ItemType Directory -Path $destFolder -Force | Out-Null }
    $dest = Join-Path $destFolder "copilot-instructions.md"
    $combined = "# GitHub Copilot Custom Instructions (Ultimate Workflows)`n`n"
    foreach ($file in $mdFiles) {
        $text = Get-Content $file.FullName -Raw
        $combined += "`n<!-- Workflow: $($file.Name) -->`n$text`n`n---`n"
    }
    Set-Content -Path $dest -Value $combined -Encoding UTF8
    Write-Host "✓ GitHub Copilot instructions generated." -ForegroundColor Green
}

switch ($Target.ToLower()) {
    "cursor" { Install-Cursor }
    "claude" { Install-Claude }
    "cc" { Install-Claude }
    "agy" { Install-AGY }
    "antigravity" { Install-AGY }
    "windsurf" { Install-Windsurf }
    "cascade" { Install-Windsurf }
    "cline" { Install-Cline }
    "roo" { Install-Cline }
    "copilot" { Install-Copilot }
    "vscode" { Install-Copilot }
    "all" {
        Install-Cursor
        Install-Claude
        Install-AGY
        Install-Windsurf
        Install-Cline
        Install-Copilot
    }
    Default {
        Write-Host "Unknown target: $Target" -ForegroundColor Red
        Write-Host "Valid targets: cursor, claude, agy, windsurf, cline, copilot, all"
    }
}

Write-Host "`n✅ Done! Happy coding with Ultimate Workflows.`n" -ForegroundColor Cyan
