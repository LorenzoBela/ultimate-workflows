"""Disposable tests of the exact debugging Markdown Bash example; no production access."""
from pathlib import Path
import os
import re
import subprocess
import tempfile
import shutil
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASH = Path('C:/Program Files/Git/bin/bash.exe') if os.name == 'nt' else Path(shutil.which('bash') or '/missing-bash')

def call(args, cwd, env=None, check=True):
    return subprocess.run(args, cwd=cwd, env=env, text=True,
                          encoding='utf-8', errors='replace', capture_output=True,
                          check=check, timeout=45)

def main():
    source = (ROOT / 'original/ultimate-debugging-workflow.md').read_text(encoding='utf-8')
    script = re.search(r'```bash\n(#!/usr/bin/env bash\n.*?)\n```', source, re.S).group(1)
    if not BASH.exists():
        raise SystemExit('UNAVAILABLE: Git Bash required; no fixture result claimed')
    with tempfile.TemporaryDirectory(prefix='ultimate-bisect-fixture-') as owned:
        base = Path(owned).resolve()
        repo = base / 'repo'
        repo.mkdir()
        def git(*args, check=True):
            return call(['git', *args], repo, check=check)
        git('init', '-q', '-b', 'fixture-main')
        git('config', 'user.name', 'Disposable Fixture')
        git('config', 'user.email', 'fixture@example.invalid')
        git('config', 'commit.gpgsign', 'false')
        git('config', 'core.hooksPath', str(base / 'no-hooks'))
        commits = []
        # Midpoint revision U is untestable, isolated from first bad revision B.
        for i, state in enumerate(['G', 'G', 'G', 'G', 'U', 'G', 'B', 'B', 'B']):
            (repo / 'state').write_text(state, encoding='utf-8')
            (repo / 'revision').write_text(str(i), encoding='utf-8')
            git('add', 'state', 'revision')
            git('commit', '-q', '-m', f'fixture {i}')
            commits.append(git('rev-parse', 'HEAD').stdout.strip())
        orchestrator = base / 'bisect.sh'
        orchestrator.write_text(script, encoding='utf-8', newline='\n')
        log = base / 'runner.log'
        runner = base / 'repro.sh'
        runner.write_text('#!/usr/bin/env bash\nset -eu\nstate=$(cat state)\nprintf "%s\\n" "$state" >> "$FIXTURE_LOG"\ncase "$state" in G) exit 0;; B) exit 1;; U) exit 125;; *) exit 200;; esac\n', encoding='utf-8', newline='\n')
        call([str(BASH), '-c', 'chmod +x "$1"', 'fixture', runner.as_posix()], repo)
        env = dict(os.environ, GOOD_SHA=commits[0], BAD_SHA=commits[-1],
                   REPRO_RUNNER=runner.as_posix(), FIXTURE_LOG=log.as_posix())
        result = call([str(BASH), orchestrator.as_posix()], repo, env)
        assert commits[6] in result.stdout, result.stdout + result.stderr
        assert 'U' in log.read_text().splitlines(), 'Untestable revision was not exercised'
        assert git('rev-parse', 'HEAD').stdout.strip() == commits[-1]
        assert git('branch', '--show-current').stdout.strip() == 'fixture-main'
        assert not (repo / '.git/BISECT_START').exists()
        print('PASS: known bad SHA found; untestable revision skipped; HEAD/branch restored')
        runner.write_text('#!/usr/bin/env bash\nexit 200\n', encoding='utf-8', newline='\n')
        result = call([str(BASH), orchestrator.as_posix()], repo, env, check=False)
        assert result.returncode != 0, 'Infrastructure failure incorrectly passed'
        assert git('rev-parse', 'HEAD').stdout.strip() == commits[-1]
        assert git('branch', '--show-current').stdout.strip() == 'fixture-main'
        assert not (repo / '.git/BISECT_START').exists()
        print('PASS: infrastructure error aborts and restores HEAD/branch')
        dirty = repo / 'unrelated-user-work.txt'
        dirty.write_text('preserve me', encoding='utf-8')
        result = call([str(BASH), orchestrator.as_posix()], repo, env, check=False)
        assert result.returncode != 0
        assert dirty.read_text() == 'preserve me'
        assert git('rev-parse', 'HEAD').stdout.strip() == commits[-1]
        print('PASS: dirty checkout rejected without modifying unrelated work')
    print('UNRUN: real Prisma/Postgres concurrency; C11 target/compiler/ISR queue; OTA/HIL; rendered document pages; assistive-technology/browser UX')

class BisectTests(unittest.TestCase):
    def test_exact_example_finds_regression_and_preserves_work(self):
        if not BASH.exists():
            self.skipTest('Native Bash unavailable')
        main()

if __name__ == '__main__':
    unittest.main()
