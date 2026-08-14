#!/usr/bin/env node

/**
 * Universal Installer for Ultimate Workflows
 * Supports: cursor, claude, agy, windsurf, cline, copilot, all
 */

const fs = require('fs');
const path = require('path');

const rootDir = path.resolve(__dirname, '..');
const universalDir = path.join(rootDir, 'universal');
const target = (process.argv[2] || 'all').toLowerCase().replace(/^--/, '');
const cwd = process.cwd();

const workflows = fs.readdirSync(universalDir).filter(f => f.endsWith('.md') && f !== 'README.md');

function copyWorkflows(destDir, transformFn, ext = '.md') {
  fs.mkdirSync(destDir, { recursive: true });
  let count = 0;
  workflows.forEach(file => {
    const srcPath = path.join(universalDir, file);
    const raw = fs.readFileSync(srcPath, 'utf-8');
    const outName = file.replace(/\.md$/, ext);
    const destPath = path.join(destDir, outName);
    const finalContent = transformFn ? transformFn(raw, file) : raw;
    fs.writeFileSync(destPath, finalContent, 'utf-8');
    count++;
  });
  return count;
}

console.log(`\n⚡ Installing Ultimate Workflows to [${target.toUpperCase()}] target in: ${cwd}\n`);

let installed = [];

// 1. Cursor IDE (.cursor/rules/*.mdc)
if (target === 'cursor' || target === 'all') {
  const dest = path.join(cwd, '.cursor', 'rules');
  const count = copyWorkflows(dest, (content, file) => {
    const name = file.replace(/\.md$/, '');
    // Convert to Cursor .mdc format
    return `---
description: ${name}
globs: *
alwaysApply: false
---

${content.replace(/^---[\s\S]*?---\n*/, '')}`;
  }, '.mdc');
  installed.push(`Cursor IDE (${count} rules in .cursor/rules/)`);
}

// 2. Claude Code (cc) (.claude/skills/ or ~/.claude/skills/)
if (target === 'claude' || target === 'cc' || target === 'all') {
  const dest = path.join(cwd, '.claude', 'skills');
  const count = copyWorkflows(dest);
  installed.push(`Claude Code (${count} skills in .claude/skills/)`);
}

// 3. Antigravity (AGY) (.agent/workflows/)
if (target === 'agy' || target === 'antigravity' || target === 'all') {
  const dest = path.join(cwd, '.agent', 'workflows');
  const count = copyWorkflows(dest);
  installed.push(`Antigravity / AGY (${count} workflows in .agent/workflows/)`);
}

// 4. Windsurf / Cascade (.windsurfrules)
if (target === 'windsurf' || target === 'cascade' || target === 'all') {
  const dest = path.join(cwd, '.windsurfrules');
  let combined = '# Windsurf Global Rulebook (Ultimate Workflows)\n\n';
  workflows.forEach(file => {
    const content = fs.readFileSync(path.join(universalDir, file), 'utf-8');
    combined += `\n<!-- Workflow: ${file} -->\n${content}\n\n---\n`;
  });
  fs.writeFileSync(dest, combined, 'utf-8');
  installed.push(`Windsurf (.windsurfrules generated)`);
}

// 5. Cline / Roo-Code (.clinerules)
if (target === 'cline' || target === 'roo' || target === 'all') {
  const dest = path.join(cwd, '.clinerules');
  let combined = '# Cline Master Workflows (Ultimate Workflows)\n\n';
  workflows.forEach(file => {
    const content = fs.readFileSync(path.join(universalDir, file), 'utf-8');
    combined += `\n<!-- Workflow: ${file} -->\n${content}\n\n---\n`;
  });
  fs.writeFileSync(dest, combined, 'utf-8');
  installed.push(`Cline / Roo-Code (.clinerules generated)`);
}

// 6. VS Code / GitHub Copilot (.github/copilot-instructions.md)
if (target === 'copilot' || target === 'vscode' || target === 'all') {
  const destDir = path.join(cwd, '.github');
  fs.mkdirSync(destDir, { recursive: true });
  const dest = path.join(destDir, 'copilot-instructions.md');
  let combined = '# GitHub Copilot Custom Instructions (Ultimate Workflows)\n\n';
  workflows.forEach(file => {
    const content = fs.readFileSync(path.join(universalDir, file), 'utf-8');
    combined += `\n<!-- Workflow: ${file} -->\n${content}\n\n---\n`;
  });
  fs.writeFileSync(dest, combined, 'utf-8');
  installed.push(`GitHub Copilot (.github/copilot-instructions.md generated)`);
}

console.log('✅ Installation Complete:');
installed.forEach(i => console.log(`   - ${i}`));
console.log('\nReady to build with Ultimate Workflows!\n');
