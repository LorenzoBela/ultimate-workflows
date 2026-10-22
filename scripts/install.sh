#!/usr/bin/env bash
# Bash entry point; requires Node.js 18+ and the full repository/package.
set -eu
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
command -v node >/dev/null 2>&1 || { echo "Node.js 18+ is required" >&2; exit 1; }
exec node "$SCRIPT_DIR/install.js" "${1:-all}"
