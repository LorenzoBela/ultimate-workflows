const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const {spawnSync} = require('node:child_process');

const root = path.resolve(__dirname, '..');
const expected = fs.readdirSync(path.join(root, 'universal')).filter(f => /^ultimate-.*\.md$/.test(f));

function cleanup(directory) {
  assert.ok(path.resolve(directory).startsWith(path.resolve(os.tmpdir()) + path.sep));
  fs.rmSync(directory, {recursive: true, force: true});
}

function run(args, cwd, status = 0) {
  const result = spawnSync(process.execPath, [path.join(root, 'scripts/install.js'), ...args], {cwd, encoding: 'utf8'});
  assert.equal(result.status, status, result.stderr);
  return result;
}

test('Codex installs complete bundles and updates only owned files', t => {
  const cwd = fs.mkdtempSync(path.join(os.tmpdir(), 'ultimate bundle '));
  t.after(() => cleanup(cwd));
  const notes = path.join(cwd, '.agents/skills/ultimate-planning-workflow/custom-notes.md');
  fs.mkdirSync(path.dirname(notes), {recursive: true});
  fs.writeFileSync(notes, 'retain user notes');
  run(['codex'], cwd);
  run(['codex'], cwd);
  assert.equal(expected.length, 38);
  for (const file of expected) {
    const dir = path.join(cwd, '.agents/skills', file.slice(0, -3));
    assert.deepEqual(fs.readFileSync(path.join(dir, 'SKILL.md')), fs.readFileSync(path.join(root, 'universal', file)));
    assert.ok(fs.existsSync(path.join(dir, 'resources/ultimate-shared/execution-contract.md')));
  }
  assert.equal(fs.readFileSync(notes, 'utf8'), 'retain user notes');
  assert.ok(fs.existsSync(path.join(cwd, '.agents/skills/ultimate-research-workflow/resources/ultimate-research-workflow/research_state.py')));
  assert.ok(!fs.existsSync(path.join(cwd, '.cursor')));
});

test('all-target install retains resource links and uses discoverable Claude bundles', t => {
  const cwd = fs.mkdtempSync(path.join(os.tmpdir(), 'ultimate all '));
  t.after(() => cleanup(cwd));
  run(['all'], cwd);
  assert.equal(fs.readdirSync(path.join(cwd, '.claude/skills')).length, 38);
  for (const file of expected) {
    const name = file.slice(0, -3);
    assert.ok(fs.existsSync(path.join(cwd, '.claude/skills', name, 'SKILL.md')));
    for (const folder of ['.agent/workflows', '.cursor/rules']) {
      assert.ok(fs.existsSync(path.join(cwd, folder, 'resources/ultimate-shared/execution-contract.md')));
    }
  }
  for (const file of ['.windsurfrules', '.clinerules', '.github/copilot-instructions.md']) {
    assert.equal((fs.readFileSync(path.join(cwd, file), 'utf8').match(/<!-- Workflow:/g) || []).length, 38);
    assert.ok(fs.existsSync(path.join(cwd, path.dirname(file), 'resources/ultimate-shared/execution-contract.md')));
  }
});

test('unknown target fails without creating output', t => {
  const cwd = fs.mkdtempSync(path.join(os.tmpdir(), 'ultimate invalid '));
  t.after(() => cleanup(cwd));
  run(['unknown'], cwd, 1);
  assert.deepEqual(fs.readdirSync(cwd), []);
});

test('customized owned skill blocks the entire update without losing user work', t => {
  const cwd = fs.mkdtempSync(path.join(os.tmpdir(), 'ultimate protected '));
  t.after(() => cleanup(cwd));
  run(['codex'], cwd);
  const custom=path.join(cwd,'.agents/skills/ultimate-api-workflow/SKILL.md');
  fs.writeFileSync(custom,'user changes');
  const receipt=fs.readFileSync(path.join(cwd,'.ultimate-workflows-install.sha256'));
  run(['all'], cwd,1);
  assert.equal(fs.readFileSync(custom,'utf8'),'user changes');
  assert.deepEqual(fs.readFileSync(path.join(cwd,'.ultimate-workflows-install.sha256')),receipt);
  assert.ok(!fs.existsSync(path.join(cwd,'.cursor')));
});

test('unowned combined rule and directory destinations are rejected before writing', t => {
  for(const kind of ['combined','directory']) {
    const cwd = fs.mkdtempSync(path.join(os.tmpdir(), 'ultimate conflict '));
    t.after(() => cleanup(cwd));
    if(kind==='combined') fs.writeFileSync(path.join(cwd,'.windsurfrules'),'existing user rules');
    else fs.mkdirSync(path.join(cwd,'.agents/skills/ultimate-api-workflow/SKILL.md'),{recursive:true});
    run(['all'],cwd,1);
    assert.ok(!fs.existsSync(path.join(cwd,'.ultimate-workflows-install.sha256')));
    assert.ok(!fs.existsSync(path.join(cwd,'.cursor')));
    if(kind==='combined') assert.equal(fs.readFileSync(path.join(cwd,'.windsurfrules'),'utf8'),'existing user rules');
  }
});

test('local deletion of an owned skill is preserved for reconciliation', t => {
  const cwd=fs.mkdtempSync(path.join(os.tmpdir(),'ultimate deleted '));
  t.after(()=>cleanup(cwd));
  run(['codex'],cwd);
  const removed=path.join(cwd,'.agents/skills/ultimate-api-workflow/SKILL.md');
  fs.unlinkSync(removed);
  run(['codex'],cwd,1);
  assert.ok(!fs.existsSync(removed));
});
