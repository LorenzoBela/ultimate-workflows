"""Synthetic local records test state/evidence contracts, not live search quality."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HELPER = Path(__file__).resolve().parents[1] / "original/resources/ultimate-research-workflow/research_state.py"
spec = importlib.util.spec_from_file_location("research_state", HELPER)
state = importlib.util.module_from_spec(spec)
spec.loader.exec_module(state)


class ResearchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.registry = {name: {"tool": f"fixture_{name}", "query": " ".join(["context"] * 200)}
                         for name in state.PROVIDERS}
        state.initialize(self.directory, "Synthetic checkpoint contract fixture", self.registry)

    def result(self, url="https://example.org/evidence?utm_source=fixture"):
        return {"status": "received", "observed_at": "2026-10-22T12:00:00+08:00",
                "artifact": "synthetic-fixture.json", "summary": "Synthetic test input, not a live provider result",
                "sources": [{"url": url, "evidence": "Fixture claim evidence"}]}

    def receive_all(self):
        for name in state.PROVIDERS:
            state.record(self.directory, name, self.result())

    def claims(self):
        return [{"id": "c1", "text": "Synthetic fixture claim",
                 "positions": {name: {"stance": "support", "rationale": "Fixture evidence",
                                      "sources": ["https://example.org/evidence"]}
                               for name in state.PROVIDERS},
                 "review": {"conclusion": "Fixture only", "reasoning": "All inputs inspected"}}]

    def test_fourteen_inputs_cannot_complete(self):
        for name in state.PROVIDERS[:-1]:
            state.record(self.directory, name, self.result())
        report = state.summarize(self.directory, self.claims())
        self.assertEqual(report["received_count"], 14)
        self.assertFalse(report["consensus_complete"])
        self.assertEqual(report["missing"], ["brave"])

    def test_failed_or_empty_provider_does_not_count(self):
        self.receive_all()
        for status in ["empty", "failed", "unavailable", "cancelled"]:
            result = {"status": status, "reason": "Synthetic failure",
                      "observed_at": "2026-10-22T12:00:00Z", "artifact": "fixture.json"}
            state.record(self.directory, "brave", result)
            self.assertFalse(state.summarize(self.directory, self.claims())["consensus_complete"])
        state.record(self.directory, "brave", self.result())
        self.assertTrue(state.summarize(self.directory, self.claims())["consensus_complete"])
        self.assertEqual(len(state.read_json(self.directory / "brave.json")["attempts"]), 6)

    def test_fifteen_requires_reviewed_matrix(self):
        self.receive_all()
        self.assertFalse(state.summarize(self.directory)["consensus_complete"])
        self.assertTrue(state.summarize(self.directory, self.claims())["consensus_complete"])

    def test_deduplicates_urls_and_exact_content_across_providers(self):
        self.receive_all()
        self.assertEqual(state.summarize(self.directory)["unique_source_identities"], 1)
        for name, url in [("you", "https://example.org/evidence"), ("exa", "https://mirror.example/copy")]:
            result = self.result(url)
            result["sources"][0]["content_sha256"] = "a" * 64
            state.record(self.directory, name, result)
        self.assertEqual(state.summarize(self.directory)["unique_source_identities"], 1)

    def test_contradiction_requires_explicit_review_and_keeps_uncertainty(self):
        self.receive_all()
        claims = self.claims()
        claims[0]["positions"]["brave"]["stance"] = "contradict"
        self.assertFalse(state.summarize(self.directory, claims)["consensus_complete"])
        claims[0]["review"]["disagreement"] = "unresolved"
        report = state.summarize(self.directory, claims)
        self.assertTrue(report["consensus_complete"])
        self.assertEqual(report["unresolved_claims"], ["c1"])

    def test_unknown_sources_and_partial_matrix_are_rejected(self):
        self.receive_all()
        claims = self.claims()
        claims[0]["positions"]["you"]["sources"] = ["https://invented.example/"]
        self.assertFalse(state.summarize(self.directory, claims)["consensus_complete"])
        del claims[0]["positions"]["you"]
        self.assertFalse(state.summarize(self.directory, claims)["consensus_complete"])

    def test_scope_cannot_be_silently_reinitialized(self):
        with self.assertRaises(FileExistsError):
            state.initialize(self.directory, "Different scope", self.registry)

    def test_stale_provider_and_concurrent_same_provider_lock_are_rejected(self):
        state.record(self.directory, "you", self.result())
        path = self.directory / "you.json"
        content = state.read_json(path)
        content["scope_sha256"] = "other"
        state.write_json(path, content)
        with self.assertRaises(ValueError):
            state.summarize(self.directory)
        (self.directory / "brave.lock").write_text("owned by another writer")
        with self.assertRaises(FileExistsError):
            state.record(self.directory, "brave", self.result())

    def test_missing_provider_and_short_rich_queries_are_rejected(self):
        for change in ["missing", "short"]:
            registry = copy.deepcopy(self.registry)
            if change == "missing": del registry["brave"]
            else: registry["you"]["query"] = "short query"
            with self.assertRaises(ValueError):
                state.initialize(self.directory / change, "Fixture", registry)

    def test_received_needs_evidence_and_timestamp(self):
        for change in ["sources", "observed_at", "artifact"]:
            result = self.result()
            result[change] = [] if change == "sources" else ""
            with self.assertRaises(ValueError):
                state.record(self.directory, "you", result)

    def test_report_cli_returns_incomplete_status(self):
        result = subprocess.run([sys.executable, str(HELPER), "report", "--run-dir", str(self.directory)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertFalse(json.loads(result.stdout)["consensus_complete"])

    def test_changed_scope_and_malformed_source_are_rejected(self):
        result = self.result()
        result["sources"] = ["not an evidence object"]
        with self.assertRaises(ValueError):
            state.record(self.directory, "you", result)
        config = state.read_json(self.directory / "run.json")
        config["question"] = "Silently altered scope"
        state.write_json(self.directory / "run.json", config)
        with self.assertRaises(ValueError):
            state.summarize(self.directory)

    def coverage(self, claims):
        return {"scope_sha256": state.load_config(self.directory)["scope_sha256"],
                "evidence_sha256": state.summarize(self.directory)["evidence_sha256"],
                "claims_sha256": state.claims_digest(claims),
                "questions": [{"id": "q1", "required": True, "status": "answered",
                    "claims": ["c1"], "freshness": {"status": "current", "rationale": "Fixture version matches"},
                    "disconfirmation": {"query": "Find contrary evidence", "outcome": "Fixture inspected",
                                         "sources": ["https://example.org/evidence"]}}],
                "decisions": [{"id": "d1", "questions": ["q1"], "rationale": "Fixture decision"}]}

    def test_legacy_consensus_does_not_imply_readiness(self):
        self.receive_all()
        report = state.summarize(self.directory, self.claims())
        self.assertTrue(report["consensus_complete"])
        self.assertFalse(report["decision_ready"])
        self.assertEqual(report["readiness_status"], "not_assessed")

    def test_bound_coverage_can_be_structurally_ready(self):
        self.receive_all()
        claims = self.claims()
        self.assertTrue(state.summarize(self.directory, claims, self.coverage(claims))["decision_ready"])

    def test_missing_or_stale_required_evidence_cannot_pass(self):
        self.receive_all()
        claims = self.claims()
        for field, value in [("status", "unknown"), ("status", "contested"), ("claims", [])]:
            coverage = self.coverage(claims)
            coverage["questions"][0][field] = value
            report = state.summarize(self.directory, claims, coverage)
            self.assertFalse(report["decision_ready"])
            if value == "unknown": self.assertEqual(report["readiness_status"], "blocked")
        coverage = self.coverage(claims)
        coverage["questions"][0]["freshness"]["status"] = "stale"
        self.assertFalse(state.summarize(self.directory, claims, coverage)["decision_ready"])

    def test_changed_claims_or_scope_invalidates_coverage(self):
        self.receive_all()
        claims = self.claims()
        coverage = self.coverage(claims)
        claims[0]["text"] = "Changed conclusion"
        self.assertFalse(state.summarize(self.directory, claims, coverage)["decision_ready"])
        coverage = self.coverage(claims)
        coverage["scope_sha256"] = "other"
        self.assertFalse(state.summarize(self.directory, claims, coverage)["decision_ready"])

    def test_new_provider_evidence_at_same_url_invalidates_coverage(self):
        self.receive_all()
        claims = self.claims()
        coverage = self.coverage(claims)
        changed = self.result()
        changed["sources"][0]["evidence"] = "New version contradicts the old evidence"
        state.record(self.directory, "brave", changed)
        report = state.summarize(self.directory, claims, coverage)
        self.assertTrue(report["consensus_complete"])
        self.assertFalse(report["decision_ready"])
        self.assertIn("coverage provider evidence digest is stale", report["coverage_errors"])

    def test_unresolved_or_all_insufficient_claims_cannot_support_decisions(self):
        self.receive_all()
        claims = self.claims()
        claims[0]["positions"]["brave"]["stance"] = "contradict"
        claims[0]["review"]["disagreement"] = "unresolved"
        self.assertFalse(state.summarize(self.directory, claims, self.coverage(claims))["decision_ready"])
        for position in claims[0]["positions"].values(): position["stance"] = "insufficient"
        self.assertFalse(state.summarize(self.directory, claims, self.coverage(claims))["decision_ready"])

    def test_coverage_requires_real_references_and_disconfirmation(self):
        self.receive_all()
        claims = self.claims()
        for modify in [lambda c: c["questions"][0].update(claims=["invented"]),
                       lambda c: c["decisions"][0].update(questions=["invented"]),
                       lambda c: c["questions"][0]["disconfirmation"].update(sources=[]),
                       lambda c: c["questions"][0]["disconfirmation"].update(sources=["https://fake.example/"])]:
            coverage = self.coverage(claims)
            modify(coverage)
            self.assertFalse(state.summarize(self.directory, claims, coverage)["decision_ready"])

    def test_require_ready_cli_does_not_pass_legacy_checkpoint(self):
        self.receive_all()
        path = self.directory / "claims.json"
        path.write_text(json.dumps(self.claims()))
        result = subprocess.run([sys.executable, str(HELPER), "report", "--run-dir", str(self.directory),
                                 "--claims", str(path), "--require-ready"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
