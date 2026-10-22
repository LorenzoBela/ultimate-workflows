import re
from pathlib import Path
import subprocess
import sys
import tempfile
import types
import unittest

ROOT = Path(__file__).resolve().parents[1]


class InvokerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        text = (ROOT / "original/ultimate-multi-agent-invoker.md").read_text(encoding="utf-8")
        cls.module = types.ModuleType("invoker_fixture")
        sys.modules[cls.module.__name__] = cls.module
        for block in re.findall(r"```python\n(.*?)```", text, re.S):
            exec(block, cls.module.__dict__)

    def test_result_status_uses_exit_code_not_success_words(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.module.run_check([sys.executable, "-c", "print('0 passed, 2 failed');raise SystemExit(7)"], directory)
            self.assertEqual(result.status, "failed")
            self.assertEqual(self.module.summarize_check(result)["exit_code"], 7)
            self.assertIn("0 passed", result.stdout)
            result = self.module.run_check([sys.executable, "-c", "print('done')"], directory)
            self.assertEqual(result.status, "passed")

    def test_timeout_and_unavailable_executable_are_not_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.module.run_check([sys.executable, "-c", "import time;time.sleep(2)"], directory, .05)
            self.assertEqual(result.status, "timeout")
            result = self.module.run_check([str(Path(directory) / "missing-executable")], directory)
            self.assertEqual(result.status, "failed_to_start")

    def test_usage_is_aggregate_and_window_is_actually_rolling(self):
        now = [0]
        budget = self.module.UsageBudget(100, 150, 80, clock=lambda: now[0])
        self.assertTrue(budget.record("a", 40))
        now[0] = 30
        self.assertTrue(budget.record("b", 40))
        now[0] = 61
        self.assertTrue(budget.record("a", 20))
        self.assertFalse(budget.record("a", 51))
        self.assertTrue(budget.tripped)

    def test_worktree_cleanup_preserves_dirty_work_and_keeps_branch(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def git(*args):
                return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, text=True)
            git("init", "-q")
            git("config", "user.name", "Disposable Fixture")
            git("config", "user.email", "fixture@example.invalid")
            git("config", "commit.gpgsign", "false")
            git("config", "core.hooksPath", str(root / "no-hooks"))
            (root / "tracked").write_text("baseline")
            git("add", "tracked")
            git("commit", "-qm", "baseline")
            candidate = root / ".worktrees/owned"
            git("worktree", "add", "-qb", "fixture-worker", str(candidate))
            owned = {str(candidate.resolve()): "fixture-worker"}
            (candidate / "user-work").write_text("preserve me")
            with self.assertRaises(ValueError):
                self.module.remove_owned_integrated_worktree(root, candidate, owned)
            self.assertEqual((candidate / "user-work").read_text(), "preserve me")
            (candidate / "user-work").unlink()
            (candidate / "tracked").write_text("unfinished tracked work")
            with self.assertRaises(ValueError):
                self.module.remove_owned_integrated_worktree(root, candidate, owned)
            self.assertEqual((candidate / "tracked").read_text(), "unfinished tracked work")
            (candidate / "tracked").write_text("baseline")
            self.module.remove_owned_integrated_worktree(root, candidate, owned)
            self.assertFalse(candidate.exists())
            self.assertIn("fixture-worker", git("branch", "--list").stdout)
