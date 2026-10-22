# PowerShell entry point; requires Node.js 18+ and the full repository/package.
param([string]$Target = "all")
$installer = Join-Path $PSScriptRoot "install.js"
$node = Get-Command node -ErrorAction Stop
& $node.Source $installer $Target
if ($LASTEXITCODE -ne 0) { throw "Workflow installation failed; see the conflict/error above." }
