"""Real local code/check repair through the connected casebook; no provider calls."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("routine_casebook", ROOT / "original/resources/ultimate-quality/casebook.py")
cb = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cb)


class RoutineTests(unittest.TestCase):
    def test_actual_failure_repair_independent_closure_and_changed_code(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            repo = root / "repo"
            repo.mkdir()
            def git(*args):
                subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)
            git("init")
            git("config", "user.name", "Fixture")
            git("config", "user.email", "fixture@example.invalid")
            git("config", "commit.gpgsign", "false")
            git("config", "core.hooksPath", str(root / "no-hooks"))
            module = repo / "counter.py"
            module.write_text("def count(items):\n    return len(items) + 1\n")
            (repo / "verify.py").write_text("from counter import count\nassert count([]) == 0\nassert count([1, 2]) == 2\n")
            git("add", ".")
            git("commit", "-m", "fixture")
            book = cb.Casebook(root / "run")
            cb.Casebook.init(root / "run", repo, "routine", "Correct count", "Local fixture scope")
            def call(method, *args, **kwargs):
                return method(*args, expected_generation=book.validate()["generation"], **kwargs)
            def put(identifier, kind, data):
                return call(book.put, {"id": identifier, "type": kind, "data": data, "links": []})
            put("C", "check", {"argv": [sys.executable, "-B", "verify.py"], "inputs": ["counter.py", "verify.py"], "mandatory": True})
            put("T", "task", {"owner": "builder", "paths": ["counter.py"], "checks": ["C"], "recovery": "Restore fixture baseline"})
            put("R", "requirement", {"hard": True, "tasks": ["T"], "checks": ["C"], "behavior": "Count has no off by one"})
            call(book.review, "plan", "plan", "planner", "ready")
            call(book.task, "T", "dispatch", "builder")
            red = call(book.record_check, "C", "builder")["receipt"]
            self.assertEqual(red["status"], "failed")
            with self.assertRaises(cb.Blocked):
                call(book.task, "T", "complete", "builder", evidence=[red["id"]])
            call(book.task, "T", "fail", "builder")
            put("F", "finding", {"mode": "code", "severity": "P1", "task": "T", "checks": ["C"], "reason": "Empty collection reports one", "paths": ["counter.py"]})
            call(book.task, "T", "repair", "builder")
            module.write_text("def count(items):\n    return len(items)\n")
            green = call(book.record_check, "C", "verifier")["receipt"]
            self.assertEqual(green["status"], "passed")
            call(book.task, "T", "complete", "builder", evidence=[green["id"]])
            call(book.finding, "F", "resolved-unverified", "builder")
            with self.assertRaises(cb.Blocked):
                call(book.finding, "F", "verified-fixed", "builder", evidence=[green["id"]])
            call(book.finding, "F", "verified-fixed", "verifier", evidence=[green["id"]])
            call(book.review, "final", "code", "verifier", "ready", evidence=[green["id"]])
            self.assertEqual(book.report()["status"], "complete")
            module.write_text("def count(items):\n    return -1\n")
            self.assertEqual(book.report()["status"], "incomplete")


if __name__ == "__main__":
    unittest.main()
