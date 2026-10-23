"""Offline evaluator regression tests; generated results are synthetic calibration.

Even tests exercising behavioral-schema parsing are not real model executions.
No suite result establishes provider coverage, workflow uplift or a live benchmark.
"""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("evaluate_v4", ROOT / "scripts/evaluate_v4.py")
ev = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ev)


class EvaluatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = ev.load_corpus(ROOT / "evaluations/v4")

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        artifact = self.root / "synthetic-transcript.txt"
        artifact.write_text("SYNTHETIC CALIBRATION ONLY: no host or provider executed.\n")
        self.evidence = {"path": artifact.name, "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(), "kind": "transcript"}

    def run_record(self, case, edition="candidate", repetition=1, phase="synthetic_calibration"):
        return {"run_id": f"synthetic/{case['id']}/{edition}/{repetition}", "case_id": case["id"],
            "phase": phase, "edition": edition,
            "revision": ev.BASELINE_REVISION if edition == "baseline" else "a" * 40,
            "fixture_hash": case["fixture_hash"],
            "host": {"name": "synthetic-host", "version": "fixture-1", "model": "not-a-model",
                     "settings": {"sampling": "unavailable"}, "unavailable_controls": ["seed"]},
            "repetition": repetition, "input_origin": "actual-host-execution",
            "evidence": [self.evidence.copy()],
            "answers": {k: values[0] for k, values in case["machine_oracle"]["answers"].items()},
            "findings": list(case["expected_defects"]), "actions": [],
            "semantic_judgment": {"status": "pass", "grader": "synthetic-calibration",
                "reason": "Known fixture answer; not independent behavioral grading", "blind_to_edition": False}}

    def case(self, prefix):
        return next(c for c in self.cases.values() if c["id"].startswith(prefix))

    def test_exact_counts_split_and_categories(self):
        self.assertEqual(len(self.cases), 70)
        self.assertEqual(sum(c["split"] == "heldout" for c in self.cases.values()), 12)
        for workflow in ev.WORKFLOWS:
            group = [c for c in self.cases.values() if c["workflow"] == workflow]
            self.assertEqual(len(group), 10 if workflow == "routine" else 12)
            self.assertEqual(sum(c["split"] == "heldout" for c in group), 2)

    def test_known_good_calibration_all70_not_live_benchmark(self):
        records = [self.run_record(c) for c in self.cases.values()]
        report = ev.evaluate(self.cases, records, self.root)
        self.assertEqual(sum(g["status"] == "passed" for g in report["grades"]), 70)
        self.assertEqual(report["comparison"]["comparable_pairs"], 0)
        self.assertEqual(report["status"], "incomplete")

    def test_false_finding_and_missed_bug_separately(self):
        clean = self.case("review-02")
        clean_run = self.run_record(clean)
        clean_run["findings"] = ["invented-SQL-injection"]
        grade = ev.grade(clean_run, clean, self.root)
        self.assertEqual(grade["false_findings"], ["invented-SQL-injection"])
        defective = self.case("review-01")
        bad_run = self.run_record(defective)
        bad_run["findings"] = []
        grade = ev.grade(bad_run, defective, self.root)
        self.assertEqual(grade["missed_bugs"], ["wrong-index"])
        self.assertEqual(grade["false_findings"], [])

    def test_false_outcome_and_forbidden_action(self):
        case = self.case("invoker-09")
        run = self.run_record(case)
        run["answers"]["worker_passed"] = True
        run["actions"] = ["hide-failed-check"]
        report = ev.evaluate(self.cases, [run], self.root)
        self.assertEqual(report["status"], "safety_failed")
        self.assertEqual(report["grades"][0]["wrong_outcomes"], ["worker_passed"])

    def test_missing_coverage_is_pending_or_incomplete_never_pass(self):
        self.assertEqual(ev.evaluate(self.cases, [], self.root)["status"], "pending")
        run = self.run_record(self.case("planning-01"), phase="behavioral_transcript")
        result = ev.evaluate(self.cases, [run], self.root, ["synthetic-host"], "a" * 40)
        self.assertEqual(result["status"], "incomplete")
        self.assertGreater(len(result["comparison"]["missing_or_incomparable"]), 0)

    def test_disputed_semantics_never_pass(self):
        case = self.case("planning-01")
        run = self.run_record(case)
        run["semantic_judgment"] = {"status": "disputed"}
        self.assertEqual(ev.grade(run, case, self.root)["status"], "incomplete")

    def test_duplicate_ids_and_duplicate_slots_are_invalid(self):
        run = self.run_record(self.case("planning-01"))
        duplicate = copy.deepcopy(run)
        duplicate["run_id"] = "another-id-same-slot"
        report = ev.evaluate(self.cases, [run, duplicate], self.root)
        self.assertEqual(report["status"], "invalid")
        self.assertEqual(len(report["grades"]), 1)
        duplicate["repetition"] = 2
        duplicate["run_id"] = run["run_id"]
        self.assertEqual(ev.evaluate(self.cases, [run, duplicate], self.root)["status"], "invalid")

    def test_fixture_revision_and_artifact_binding(self):
        run = self.run_record(self.case("planning-01"))
        for field, value in (("fixture_hash", "0" * 64), ("revision", "short")):
            bad = copy.deepcopy(run)
            bad[field] = value
            self.assertTrue(ev.validate_run(bad, self.cases, self.root))
        bad = copy.deepcopy(run)
        bad["evidence"][0]["sha256"] = "0" * 64
        self.assertTrue(ev.validate_run(bad, self.cases, self.root))
        fabricated_baseline = self.run_record(self.case("planning-01"), edition="baseline")
        fabricated_baseline["revision"] = "9d8e606" + "0" * 33
        self.assertTrue(ev.validate_run(fabricated_baseline, self.cases, self.root))

    def test_comparability_requires_matching_host_settings_and_repetitions(self):
        case = self.case("review-01")
        b = self.run_record(case, "baseline", phase="behavioral_transcript")
        c = self.run_record(case, phase="behavioral_transcript")
        c["host"]["settings"] = {"temperature": 0.8}
        report = ev.evaluate(self.cases, [b, c], self.root, ["synthetic-host"], "a" * 40)
        self.assertEqual(report["comparison"]["comparable_pairs"], 0)
        self.assertTrue(any("incomparable host" in x for x in report["comparison"]["missing_or_incomparable"]))
        c["host"] = copy.deepcopy(b["host"])
        report = ev.evaluate(self.cases, [b, c], self.root, ["synthetic-host"], "a" * 40)
        self.assertEqual(report["comparison"]["comparable_pairs"], 1)
        self.assertEqual(report["status"], "incomplete")

    def test_synthetic_receipts_cannot_establish_live15(self):
        case = self.case("research-01")
        run = self.run_record(case, phase="behavioral_transcript")
        run["provider_receipts"] = [{"provider": provider, "origin": "synthetic", "substantive": True,
            "tool": "fixture", "retrieved_at": "2026-10-23", "evidence": self.evidence} for provider in ev.PROVIDERS]
        self.assertEqual(ev.grade(run, case, self.root)["status"], "incomplete")
        run["claims_live_coverage"] = True
        self.assertEqual(ev.grade(run, case, self.root)["status"], "safety_failed")

    def test_seeded_code_defects_reproduce_and_clean_counterexample_works(self):
        bug = self.case("debugging-01")["fixture"]["input"]
        namespace = {}
        exec(bug["code"], {"__builtins__": {"len": len}}, namespace)
        with self.assertRaises(IndexError):
            namespace["last"](bug["input"])
        repaired = bug["code"].replace("len(xs)]", "len(xs)-1]")
        namespace = {}
        exec(repaired, {"__builtins__": {"len": len}}, namespace)
        self.assertEqual(namespace["last"](bug["input"]), bug["expected"])
        clean = self.case("review-02")["fixture"]["input"]
        namespace = {}
        exec(clean["code"], {"__builtins__": {}}, namespace)
        self.assertEqual([namespace["first"](xs) for xs in clean["cases"]], clean["expected"])

    def test_malformed_records_fail_closed_without_traceback(self):
        good = self.run_record(self.case("research-01"), phase="behavioral_transcript")
        for field, value in (("case_id", []), ("evidence", [None]),
                             ("evidence", [{"path": [], "sha256": "a"}]),
                             ("evidence", None), ("provider_receipts", [{"provider": []}]),
                             ("host", []), ("findings", [None])):
            bad = copy.deepcopy(good)
            bad[field] = value
            with self.subTest(field=field, value=value):
                self.assertEqual(ev.evaluate(self.cases, [bad], self.root)["status"], "invalid")
        self.assertEqual(ev.evaluate(self.cases, [None], self.root)["status"], "invalid")
        self.assertEqual(ev.evaluate(self.cases, [], self.root, ["host", "host"])["status"], "invalid")

    def test_bool_is_not_numeric_answer_and_evidence_escape_rejected(self):
        case = self.case("research-02")
        run = self.run_record(case)
        run["answers"]["independent_sources"] = True
        self.assertEqual(ev.grade(run, case, self.root)["status"], "failed")
        run["evidence"][0]["path"] = "../not-allowed.txt"
        self.assertTrue(ev.validate_run(run, self.cases, self.root))

    def test_per_workflow_metrics_dont_hide_false_findings(self):
        records = []
        for workflow in ("review", "debugging"):
            case = next(c for c in self.cases.values() if c["workflow"] == workflow)
            for edition in ("baseline", "candidate"):
                record = self.run_record(case, edition, phase="behavioral_transcript")
                if workflow == "review" and edition == "candidate":
                    record["findings"].append("false-finding")
                records.append(record)
        report = ev.evaluate(self.cases, records, self.root, ["synthetic-host"], "a" * 40)
        self.assertIn("review/false_findings", report["comparison"]["regressions"])
        self.assertEqual(report["comparison"]["per_workflow"]["debugging"]["errors"]["candidate"]["false_findings"], 0)

    def test_routine_underlying_code_hashes_and_check_vectors(self):
        for prefix in ("routine-01", "routine-08"):
            artifacts = self.case(prefix)["fixture"]["input"]["artifacts"]
            code = artifacts["files"]["app.py"]
            self.assertEqual(hashlib.sha256(code.encode()).hexdigest(), artifacts["integrated_code_hash"])
            namespace = {}
            exec(code, {"__builtins__": {}}, namespace)
            for check in artifacts["checks"]:
                vector = check["input"]
                self.assertEqual(namespace["get_document"](artifacts["dataset"], vector["tenant"], vector["id"]), check["expected"])
        stale = self.case("routine-02")["fixture"]["input"]["artifacts"]
        self.assertNotEqual(stale["plan_hash"], stale["plan_review"]["plan_hash"])
        budget = self.case("routine-09")["fixture"]["input"]["artifacts"]
        self.assertEqual(len(budget["repair"]["attempt_receipts"]), 3)
        self.assertEqual(budget["observed_check_receipts"]["tenant-other"]["status"], "failed")

    def test_full_three_repeat_hypothetical_schema_pairing_not_a_live_benchmark(self):
        # Explicitly synthetic calibration of the behavioral-schema consumer only.
        # Receipt strings below are mocks, not real execution or authenticated proof.
        records = []
        for case in self.cases.values():
            for repetition in (1, 2, 3):
                for edition in ("baseline", "candidate"):
                    run = self.run_record(case, edition, repetition, "behavioral_transcript")
                    if case["workflow"] in ("research", "routine"):
                        run["provider_receipts"] = [{"provider": provider,
                            "origin": "actual-provider-execution", "substantive": True,
                            "tool": "MOCK-ONLY", "retrieved_at": "2026-10-23",
                            "evidence": self.evidence} for provider in ev.PROVIDERS]
                    records.append(run)
        report = ev.evaluate(self.cases, records, self.root, ["synthetic-host"], "a" * 40)
        self.assertEqual(report["comparison"]["comparable_pairs"], 210)
        self.assertEqual(report["status"], "not_established")  # Equal results are no improvement.
        baseline = next(r for r in records if r["edition"] == "baseline" and r["case_id"].startswith("review-01"))
        baseline["findings"] = []
        report = ev.evaluate(self.cases, records, self.root, ["synthetic-host"], "a" * 40)
        self.assertEqual(report["status"], "supported_on_these_fixtures")
        self.assertIn("review/missed_bugs", report["comparison"]["improvements"])
        self.assertTrue(any("not authenticity" in limit for limit in report["limits"]))


if __name__ == "__main__":
    unittest.main()
