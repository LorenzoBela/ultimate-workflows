#!/usr/bin/env node
/** Guarded bundle installer. All entry points use the same ownership checks. */
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const root = path.resolve(__dirname, '..');
const source = path.join(root, 'universal');
const cwd = fs.realpathSync(process.cwd());
const aliases = {cc:'claude', antigravity:'agy', cascade:'windsurf', roo:'cline', vscode:'copilot'};
const input = (process.argv[2] || 'all').toLowerCase().replace(/^--/, '');
const target = aliases[input] || input;
const targets = ['codex','claude','cursor','agy','windsurf','cline','copilot'];
const hash = data => crypto.createHash('sha256').update(data).digest('hex');
const files = fs.readdirSync(source).filter(f => /^ultimate-.*\.md$/.test(f)).sort();
const manifest = JSON.parse(fs.readFileSync(path.join(root,'workflow-manifest.json'),'utf8'));
const outputs = new Map();
const receiptPath = path.join(cwd, '.ultimate-workflows-install.sha256');
function add(relative, content) { outputs.set(relative.replaceAll('\\','/'), Buffer.from(content)); }
function resources(destination, name) {
  const names=name?[name]:files.map(f=>f.slice(0,-3));
  for(const skill of names) for(const relative of Object.keys(manifest.workflows[skill].files))
    if(relative!=='SKILL.md') add(path.join(destination,relative),fs.readFileSync(path.join(source,relative)));
}
function plan(kind) {
  if (kind==='codex' || kind==='claude') {
    const dest = kind==='codex' ? '.agents/skills' : '.claude/skills';
    for (const file of files) {
      const name=file.slice(0,-3), folder=path.join(dest,name);
      add(path.join(folder,'SKILL.md'),fs.readFileSync(path.join(source,file)));
      resources(folder,name);
    }
  } else if (kind==='cursor' || kind==='agy') {
    const dest=kind==='cursor'?'.cursor/rules':'.agent/workflows';
    for (const file of files) {
      const text=fs.readFileSync(path.join(source,file),'utf8');
      add(path.join(dest,kind==='cursor'?file.slice(0,-3)+'.mdc':file), kind==='cursor'
        ? `---\ndescription: ${file.slice(0,-3)}\nglobs: '*'\nalwaysApply: false\n---\n\n${text.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n*/,'')}`:text);
    }
    resources(dest);
  } else {
    const output={windsurf:'.windsurfrules',cline:'.clinerules',copilot:'.github/copilot-instructions.md'}[kind];
    let combined='# Ultimate Workflows\n\n';
    for (const file of files) combined+=`\n<!-- Workflow: ${file} -->\n${fs.readFileSync(path.join(source,file),'utf8')}\n`;
    add(output,combined); resources(path.dirname(output));
  }
}
function guard(relative) {
  const absolute=path.resolve(cwd,relative);
  if (!absolute.startsWith(cwd+path.sep)) throw new Error('Destination escapes project');
  let current=absolute;
  while (current!==cwd) {
    if (fs.existsSync(current) || (()=>{try{return fs.lstatSync(current).isSymbolicLink();}catch{return false;}})()) {
      if (fs.lstatSync(current).isSymbolicLink()) throw new Error(`Symlink destination refused: ${relative}`);
      if (current!==absolute && !fs.statSync(current).isDirectory()) throw new Error(`Parent is not a directory: ${relative}`);
    }
    current=path.dirname(current);
  }
  return absolute;
}
function currentFile(relative) {
  const absolute=guard(relative);
  if (!fs.existsSync(absolute)) return null;
  if (!fs.statSync(absolute).isFile()) throw new Error(`Destination is not a regular file: ${relative}`);
  return fs.readFileSync(absolute);
}
function atomic(relative,data) {
  const absolute=guard(relative);
  fs.mkdirSync(path.dirname(absolute),{recursive:true});
  const temporary=absolute+'.tmp-'+crypto.randomUUID();
  try { fs.writeFileSync(temporary,data,{flag:'wx'}); fs.renameSync(temporary,absolute); }
  finally { if(fs.existsSync(temporary)) fs.unlinkSync(temporary); }
}
try {
  if (!targets.includes(target) && target!=='all') throw new Error(`Unknown target: ${input}`);
  if (files.length!==38) throw new Error('Package must contain 38 workflows');
  if (Object.keys(manifest.workflows).length!==38) throw new Error('Incomplete bundle manifest');
  for(const file of files) {
    const name=file.slice(0,-3);
    if(!manifest.workflows[name]) throw new Error(`Missing bundle manifest: ${name}`);
    for(const [relative,expected] of Object.entries(manifest.workflows[name].files)) {
      const entry=path.resolve(source,relative==='SKILL.md'?file:relative);
      if(!entry.startsWith(source+path.sep) || fs.realpathSync(entry)!==entry)
        throw new Error('Package resource escapes source or is a symlink');
      if(hash(fs.readFileSync(entry))!==expected) throw new Error(`Package hash mismatch: ${name}/${relative}`);
    }
  }
  for (const kind of target==='all'?targets:[target]) plan(kind);
  const receipt=currentFile('.ultimate-workflows-install.sha256');
  const owned=new Map();
  if(receipt) for(const line of receipt.toString('utf8').split('\n').filter(Boolean)) {
    const match=/^([a-f0-9]{64})\t([^\t\r\n]+)$/.exec(line);
    if(!match) throw new Error('Invalid installation receipt');
    guard(match[2]); owned.set(match[2],match[1]);
  }
  const changes=[];
  for(const [relative,data] of outputs) {
    const old=currentFile(relative);
    if(old===null && owned.has(relative)) throw new Error(`Previously installed file was removed: ${relative}. Reconcile the deletion before updating.`);
    if(old && !old.equals(data) && owned.get(relative)!==hash(old))
      throw new Error(`Local customization or unowned output: ${relative}. Back up and reconcile before updating.`);
    if(!old || !old.equals(data)) changes.push({relative,data,old});
    owned.set(relative,hash(data));
  }
  const nextReceipt=Buffer.from([...owned].sort(([a],[b])=>a.localeCompare(b)).map(([f,d])=>d+'\t'+f).join('\n')+'\n');
  changes.push({relative:'.ultimate-workflows-install.sha256',data:nextReceipt,old:receipt});
  const written=[];
  try {
    for(const change of changes) {
      const now=currentFile(change.relative);
      if((now===null)!==(change.old===null) || (now && !now.equals(change.old))) throw new Error('Destination changed after preflight');
      atomic(change.relative,change.data); written.push(change);
    }
  } catch(error) {
    for(const change of written.reverse()) {
      const now=currentFile(change.relative);
      if(now && now.equals(change.data)) {
        if(change.old===null) fs.unlinkSync(guard(change.relative)); else atomic(change.relative,change.old);
      }
    }
    throw error;
  }
  console.log(`Installed ${files.length} ${target} workflow bundles. Owned files recorded; unrelated files preserved.`);
} catch(error) { console.error(error.message); process.exitCode=1; }
