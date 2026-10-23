"""Isolated local regression fixtures, not live agent/provider evaluations."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parents[1] / "original/resources/ultimate-quality/casebook.py"
spec = importlib.util.spec_from_file_location("casebook_fixture", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Casebook, Invalid, Blocked = module.Casebook, module.Invalid, module.Blocked


class CasebookTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ultimate-casebook-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Casebook Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        (self.repo / "spec.md").write_text("Requirement: code is good\n")
        (self.repo / "code.txt").write_text("bad")
        self.git("add", "spec.md", "code.txt")
        self.git("commit", "-m", "fixture baseline")
        (self.repo / "user-untracked.txt").write_text("preserve user work")
        self.run = self.root / "run"
        Casebook.init(self.run, self.repo, "run-1", "repair fixture", "local fixture only",
                      ["spec.md", "code.txt"])
        self.book = Casebook(self.run)

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.repo), *args], check=True,
                              capture_output=True, text=True).stdout.strip()

    def generation(self):
        return self.book.validate()["generation"]

    def put(self, key, kind, data, links=None):
        return self.book.put({"id": key, "type": kind, "data": data, "links": links or []}, self.generation())

    def setup_plan(self):
        self.check_data = {"argv": [sys.executable, "-c", "from pathlib import Path; assert Path('code.txt').read_text() == 'good'"],
                           "inputs": ["code.txt"], "cwd": ".", "mandatory": True}
        self.put("check.behavior", "check", self.check_data)
        self.task_data = {"owner": "builder", "recovery": "Preserve fixture diff and restore only owned code",
                          "paths": ["code.txt"], "checks": ["check.behavior"], "dependencies": []}
        self.put("task.fix", "task", self.task_data)
        self.requirement_data = {"text": "code has good content", "hard": True,
                                 "tasks": ["task.fix"], "checks": ["check.behavior"]}
        self.put("requirement.good", "requirement", self.requirement_data)

    def review(self, key="plan.ready", mode="plan", verdict="ready", actor="reviewer", evidence=None):
        return self.book.review(key, mode, actor, verdict, self.generation(), evidence)

    def task(self, action, key="task.fix", actor="builder", evidence=None):
        return self.book.task(key, action, actor, self.generation(), evidence)

    def check(self, key="check.behavior"):
        return self.book.record_check(key, "checker", self.generation())["receipt"]

    def complete_task(self):
        self.task("dispatch")
        (self.repo / "code.txt").write_text("good")
        receipt = self.check()
        self.task("complete", evidence=[receipt["id"]])
        return receipt

    def test_end_to_end_real_failure_repair_final_and_user_work(self):
        self.setup_plan()
        self.review()
        self.task("dispatch")
        failed = self.check()
        self.assertEqual(failed["status"], "failed")
        self.task("fail")
        self.task("repair")
        (self.repo / "code.txt").write_text("good")
        self.git("add", "code.txt")
        self.git("commit", "-m", "fixture repair")
        receipt = self.check()
        self.task("complete", evidence=[receipt["id"]])
        self.review("final.review", "code", evidence=[receipt["id"]])
        self.assertEqual(self.book.report()["status"], "complete")
        self.assertEqual((self.repo / "user-untracked.txt").read_text(), "preserve user work")
        self.assertTrue((self.run / "checks" / (receipt["id"] + ".stdout")).exists())

    def test_plan_and_code_fingerprints_have_different_scope(self):
        self.setup_plan()
        baseline = self.book.validate()["plan"]
        self.review()
        receipt = self.complete_task()
        self.review("final.review", "code", evidence=[receipt["id"]])
        (self.repo / "unrelated.txt").write_text("unrelated")
        self.git("add", "unrelated.txt")
        self.git("commit", "-m", "unrelated change")
        self.assertEqual(self.book.validate()["plan"], baseline)
        self.assertEqual(self.book.report()["status"], "incomplete")
        receipt = self.check()
        self.task("complete", evidence=[receipt["id"]])
        self.review("new.final", "code", evidence=[receipt["id"]])
        self.assertEqual(self.book.report()["status"], "complete")
        (self.repo / "spec.md").write_text("changed consequential requirement")
        with self.assertRaises(Blocked):
            self.task("complete", evidence=[receipt["id"]])

    def test_changed_plan_and_current_ready_gate(self):
        self.setup_plan()
        with self.assertRaises(Blocked):
            self.task("dispatch")
        self.review()
        self.requirement_data["text"] = "changed requirement"
        self.put("requirement.good", "requirement", self.requirement_data)
        with self.assertRaises(Blocked):
            self.task("dispatch")
        self.review("plan.updated")
        self.task("dispatch")

    def test_latest_review_uses_sequence_not_alphabetic_id(self):
        self.setup_plan()
        self.review("z.ready")
        self.review("a.needs", verdict="needs_revision")
        with self.assertRaises(Blocked):
            self.task("dispatch")
        self.review("b.ready")
        self.task("dispatch")

    def test_linked_claim_can_change_but_stales_plan_until_relinked(self):
        self.setup_plan()
        self.put("claim.api", "claim", {"text": "version one"})
        self.put("requirement.good", "requirement", self.requirement_data,
                 [{"id": "claim.api", "revision": 1}])
        self.review()
        baseline = self.book.validate()["plan"]
        self.put("claim.unrelated", "claim", {"text": "irrelevant"})
        self.assertEqual(baseline, self.book.validate()["plan"])
        self.put("claim.api", "claim", {"text": "version two"})
        self.assertNotEqual(baseline, self.book.validate()["plan"])
        self.assertEqual(self.book._load()["history"]["claim.api"][0]["data"]["text"], "version one")
        with self.assertRaises(Blocked):
            self.review("bad.ready")
        self.put("requirement.good", "requirement", self.requirement_data,
                 [{"id": "claim.api", "revision": 2}])
        self.review("fresh.ready")
        self.task("dispatch")

    def test_consequential_assumptions_need_supported_or_bounded_decision(self):
        self.setup_plan()
        self.put("assumption.capability", "assumption", {"consequential": True, "status": "unknown"})
        with self.assertRaises(Blocked):
            self.review()
        self.put("decision.limit", "decision", {"text": "bounded fallback"})
        self.put("assumption.capability", "assumption", {"consequential": True, "status": "accepted-bounded",
                 "decision": "decision.limit", "mitigation": "Explicit bounded fallback", "consequence": "Delayed completion"})
        self.review()

    def test_no_false_pass_from_output_and_argv_has_no_shell(self):
        self.put("check.false", "check", {"argv": [sys.executable, "-c", "import sys;print('PASSED password success');sys.exit(7)"], "inputs": []})
        result = self.check("check.false")
        self.assertEqual((result["status"], result["exit_code"]), ("failed", 7))
        self.put("check.literal", "check", {"argv": [sys.executable, "-c", "import sys; print(sys.argv[1])", "$(touch forbidden)"], "inputs": []})
        result = self.check("check.literal")
        self.assertEqual(result["status"], "passed")
        self.assertIn("$(touch forbidden)", (self.run / result["stdout"]["path"]).read_text())
        self.assertFalse((self.repo / "forbidden").exists())

    def test_timeout_output_limit_and_missing_executable(self):
        cases = [("timeout", [sys.executable, "-c", "import time; time.sleep(3)"], {"timeout_seconds": .05}),
                 ("output_limit", [sys.executable, "-c", "print('x'*100000)"], {"max_output_bytes": 32}),
                 ("failed_to_start", [str(self.root / "absent-executable")], {})]
        for expected, argv, extra in cases:
            key = "check." + expected
            self.put(key, "check", {"argv": argv, "inputs": [], **extra})
            result = self.check(key)
            self.assertEqual(result["status"], expected)
            if expected == "output_limit":
                self.assertLessEqual(sum((self.run / result[name]["path"]).stat().st_size for name in ("stdout", "stderr")), 32)

    def test_evidence_is_stale_if_command_changes_its_inputs(self):
        self.setup_plan()
        self.check_data["argv"] = [sys.executable, "-c", "from pathlib import Path; Path('code.txt').write_text('good')"]
        self.put("check.behavior", "check", self.check_data)
        self.review()
        self.task("dispatch")
        receipt = self.check()
        self.assertEqual(receipt["status"], "passed")
        with self.assertRaises(Blocked):
            self.task("complete", evidence=[receipt["id"]])

    def test_missing_references_cycles_and_duplicate_ids_preserve_state(self):
        self.setup_plan()
        before = self.book.path.read_bytes()
        with self.assertRaises(Invalid):
            self.put("bad.task", "task", {**self.task_data, "dependencies": ["missing"]})
        self.assertEqual(self.book.path.read_bytes(), before)
        self.put("task.second", "task", {**self.task_data, "dependencies": ["task.fix"]})
        before = self.book.path.read_bytes()
        with self.assertRaises(Invalid):
            self.put("task.fix", "task", {**self.task_data, "dependencies": ["task.second"]})
        with self.assertRaises(Invalid):
            self.put("task.fix", "claim", {"text": "identity collision"})
        with self.assertRaises(Invalid):
            self.put("task.fix", "task", {**self.task_data, "checks": ["check.behavior", "check.behavior"]})
        self.assertEqual(self.book.path.read_bytes(), before)

    def test_failed_dependency_blocks_dispatch_and_task_completion_needs_receipt(self):
        self.setup_plan()
        self.put("task.second", "task", {**self.task_data, "dependencies": ["task.fix"]})
        self.review()
        self.task("dispatch")
        with self.assertRaises(Blocked):
            self.task("complete", evidence=[])
        self.task("fail")
        with self.assertRaises(Blocked):
            self.task("dispatch", key="task.second")
        self.assertEqual(self.book.report()["status"], "incomplete")

    def test_independent_current_evidence_required_to_close_findings(self):
        self.setup_plan()
        self.review()
        old_receipt = self.complete_task()
        self.put("finding.defect", "finding", {"mode": "code", "severity": "P1", "reason": "reachable content defect",
                 "task": "task.fix", "checks": ["check.behavior"], "paths": ["code.txt"]})
        self.book.finding("finding.defect", "resolved-unverified", "builder", self.generation())
        with self.assertRaises(Blocked):
            self.book.finding("finding.defect", "verified-fixed", "builder", self.generation(), [old_receipt["id"]])
        (self.repo / "code.txt").write_text("changed")
        with self.assertRaises(Blocked):
            self.book.finding("finding.defect", "verified-fixed", "reviewer", self.generation(), [old_receipt["id"]])
        (self.repo / "code.txt").write_text("good")
        self.git("add", "code.txt")
        self.git("commit", "-m", "integrated fix")
        receipt = self.check()
        self.book.finding("finding.defect", "verified-fixed", "reviewer", self.generation(), [receipt["id"]])
        self.task("complete", evidence=[receipt["id"]])
        with self.assertRaises(Blocked):
            self.review("builder.final", "code", actor="builder", evidence=[receipt["id"]])
        self.review("reviewer.final", "code", evidence=[receipt["id"]])
        self.assertEqual(self.book.report()["status"], "complete")
        (self.repo / "code.txt").write_text("regression")
        self.assertTrue(self.book.report()["findings"]["finding.defect"]["open"])

    def test_three_repair_attempts_and_initial_plus_three_review_repair_rounds(self):
        self.setup_plan()
        self.review()
        self.complete_task()
        self.review("final.initial", "code", verdict="needs_revision")
        for index in range(3):
            self.task("repair")
            receipt = self.check()
            self.task("complete", evidence=[receipt["id"]])
            self.review("final.round" + str(index), "code", verdict="needs_revision" if index < 2 else "ready", evidence=[receipt["id"]])
        self.assertEqual(self.book.report()["status"], "complete")
        self.assertEqual(self.book._load()["final_rounds"], 3)
        before = self.book.path.read_bytes()
        with self.assertRaises(Blocked):
            self.task("repair")
        self.assertEqual(self.book.path.read_bytes(), before)
        self.task("block")
        with self.assertRaises(Blocked):
            self.task("dispatch")
        with self.assertRaises(Blocked):
            self.task("repair")

    def test_stale_generation_lock_and_concurrent_external_edit(self):
        self.setup_plan()
        before = self.book.path.read_bytes()
        with self.assertRaises(Invalid):
            self.book.put({"id": "claim.new", "type": "claim", "data": {}}, 0)
        self.book.lock.write_text("fixture lock")
        with self.assertRaises(Invalid):
            self.put("claim.new", "claim", {})
        self.book.lock.unlink()
        self.assertEqual(self.book.path.read_bytes(), before)
        # An explicit concurrent writer during the mutator must not be overwritten.
        def mutate(state):
            self.book.path.write_bytes(before + b" ")
        with self.assertRaises(Invalid):
            self.book._update(self.generation(), "interference", mutate)
        self.assertEqual(self.book.path.read_bytes(), before + b" ")

    def test_corrupt_artifacts_or_checkpoint_not_silently_repaired(self):
        self.setup_plan()
        receipt = self.check()
        (self.run / receipt["stderr"]["path"]).write_text("tampered")
        before = self.book.path.read_bytes()
        with self.assertRaises(Invalid):
            self.book.validate()
        self.assertEqual(self.book.path.read_bytes(), before)
        self.book.path.write_text('{"schema_version":1}')
        with self.assertRaises(Invalid):
            self.book.validate()
        with self.assertRaises(Invalid):
            Casebook.init(self.run, self.repo, "other", "other", "other")
        self.assertEqual(self.book.path.read_text(), '{"schema_version":1}')

    def test_paths_malformed_json_and_unsupported_fields(self):
        self.setup_plan()
        before = self.book.path.read_bytes()
        for bad in ("../outside", str(self.root / "outside")):
            with self.assertRaises(Invalid):
                self.put("task.bad", "task", {**self.task_data, "paths": [bad]})
        for text in ('{"id":"a","id":"b"}', '{"value":NaN}', '{'):
            file = self.root / "malformed.json"
            file.write_text(text)
            with self.assertRaises(Invalid):
                module.read_json(file)
        with self.assertRaises(Invalid):
            self.book.put({"id": "review.fake", "type": "review", "data": {}}, self.generation())
        self.assertEqual(self.book.path.read_bytes(), before)

    def test_symlink_input_rejected_when_platform_permits_creation(self):
        target = self.root / "outside.txt"
        target.write_text("outside")
        link = self.repo / "linked.txt"
        try:
            link.symlink_to(target)
        except OSError:
            self.skipTest("symlink creation unavailable on this host")
        with self.assertRaises(Invalid):
            Casebook.init(self.root / "linked-run", self.repo, "linked", "scope", "local", ["linked.txt"])

    def test_cli_result_exit_codes_and_duplicate_input(self):
        def cli(*args):
            result = subprocess.run([sys.executable, str(SOURCE), *args], capture_output=True, text=True)
            return result.returncode, json.loads(result.stdout)
        self.assertEqual(cli("validate", "--run-dir", str(self.run))[0], 0)
        self.assertEqual(cli("report", "--run-dir", str(self.run))[0], 2)
        record = self.root / "duplicate.json"
        record.write_text('{"id":"a","id":"b"}')
        code, value = cli("put", "--run-dir", str(self.run), "--record", str(record), "--expect-generation", "0")
        self.assertEqual((code, value["status"]), (1, "invalid"))


if __name__ == "__main__":
    unittest.main()
