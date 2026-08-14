#!/usr/bin/env bash

# Ultimate Workflows - Universal Bash Installer
# Usage:
#   ./scripts/install.sh [cursor | claude | agy | windsurf | cline | copilot | all]

TARGET="${1:-all}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
UNIVERSAL_DIR="$ROOT_DIR/universal"
DEST_DIR="$(pwd)"

echo "⚡ Installing Ultimate Workflows to target: [$TARGET] in $DEST_DIR"

install_cursor() {
  echo "📦 Installing Cursor rules (.cursor/rules/)..."
  mkdir -p "$DEST_DIR/.cursor/rules"
  for f in "$UNIVERSAL_DIR"/*.md; do
    filename=$(basename "$f" .md)
    if [ "$filename" != "README" ]; then
      cat <<EOF > "$DEST_DIR/.cursor/rules/${filename}.mdc"
---
description: ${filename}
globs: *
alwaysApply: false
---

$(tail -n +11 "$f")
EOF
    fi
  done
  echo "✓ Cursor rules installed."
}

install_claude() {
  echo "📦 Installing Claude Code skills (.claude/skills/)..."
  mkdir -p "$DEST_DIR/.claude/skills"
  cp "$UNIVERSAL_DIR"/*.md "$DEST_DIR/.claude/skills/"
  rm -f "$DEST_DIR/.claude/skills/README.md"
  echo "✓ Claude Code skills installed."
}

install_agy() {
  echo "📦 Installing Antigravity workflows (.agent/workflows/)..."
  mkdir -p "$DEST_DIR/.agent/workflows"
  cp "$UNIVERSAL_DIR"/*.md "$DEST_DIR/.agent/workflows/"
  rm -f "$DEST_DIR/.agent/workflows/README.md"
  echo "✓ Antigravity workflows installed."
}

install_windsurf() {
  echo "📦 Installing Windsurf rules (.windsurfrules)..."
  echo "# Windsurf Global Rulebook (Ultimate Workflows)" > "$DEST_DIR/.windsurfrules"
  for f in "$UNIVERSAL_DIR"/*.md; do
    filename=$(basename "$f")
    if [ "$filename" != "README.md" ]; then
      echo -e "\n\n<!-- Workflow: $filename -->\n" >> "$DEST_DIR/.windsurfrules"
      cat "$f" >> "$DEST_DIR/.windsurfrules"
    fi
  done
  echo "✓ Windsurf rulebook generated."
}

install_cline() {
  echo "📦 Installing Cline rules (.clinerules)..."
  echo "# Cline Master Workflows (Ultimate Workflows)" > "$DEST_DIR/.clinerules"
  for f in "$UNIVERSAL_DIR"/*.md; do
    filename=$(basename "$f")
    if [ "$filename" != "README.md" ]; then
      echo -e "\n\n<!-- Workflow: $filename -->\n" >> "$DEST_DIR/.clinerules"
      cat "$f" >> "$DEST_DIR/.clinerules"
    fi
  done
  echo "✓ Cline rules generated."
}

install_copilot() {
  echo "📦 Installing GitHub Copilot instructions (.github/copilot-instructions.md)..."
  mkdir -p "$DEST_DIR/.github"
  echo "# GitHub Copilot Instructions (Ultimate Workflows)" > "$DEST_DIR/.github/copilot-instructions.md"
  for f in "$UNIVERSAL_DIR"/*.md; do
    filename=$(basename "$f")
    if [ "$filename" != "README.md" ]; then
      echo -e "\n\n<!-- Workflow: $filename -->\n" >> "$DEST_DIR/.github/copilot-instructions.md"
      cat "$f" >> "$DEST_DIR/.github/copilot-instructions.md"
    fi
  done
  echo "✓ GitHub Copilot instructions generated."
}

case "$TARGET" in
  cursor)
    install_cursor
    ;;
  claude|cc)
    install_claude
    ;;
  agy|antigravity)
    install_agy
    ;;
  windsurf|cascade)
    install_windsurf
    ;;
  cline|roo)
    install_cline
    ;;
  copilot|vscode)
    install_copilot
    ;;
  all)
    install_cursor
    install_claude
    install_agy
    install_windsurf
    install_cline
    install_copilot
    ;;
  *)
    echo "Unknown target: $TARGET"
    echo "Available: cursor, claude, agy, windsurf, cline, copilot, all"
    exit 1
    ;;
esac

echo -e "\n✅ Installation Complete!"
