"""Consume externally produced v4 results; never execute models or providers.

Deterministic grading checks structured reported answers against frozen fixture
oracles. It does not authenticate transcripts or establish semantic truth. Human
judgments and original transcript evidence remain independently required.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import statistics
import sys

BASELINE = "9d8e606"
BASELINE_REVISION = "9d8e606f7898e310e722ff31b63b182281eee573"
WORKFLOWS = ("research", "planning", "invoker", "debugging", "review", "routine")
PHASES = ("offline_contract", "synthetic_calibration", "behavioral_transcript")
PROVIDERS = ("Tavily", "Context7", "You.com", "Exa", "Jina", "SERPdive",
             "Linkup", "Parallel Search", "SerpApi", "GitHub", "Firecrawl",
             "Crawleo", "Bright Data", "Apify", "Brave Search")


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def fixture_digest(case):
    return digest({k: v for k, v in case.items() if k != "fixture_hash"})


def load_corpus(directory):
    cases = {}
    for path in sorted(Path(directory).glob("*.json")):
        if path.name in ("result-schema.json", "calibration.json"):
            continue
        case = json.loads(path.read_text(encoding="utf-8-sig"))
        if not isinstance(case, dict) or "id" not in case:
            raise ValueError(f"Not a fixture: {path.name}")
        if case["id"] in cases:
            raise ValueError("Duplicate case ID")
        if case.get("fixture_hash") != fixture_digest(case):
            raise ValueError(f"Fixture hash mismatch: {case['id']}")
        required = ("fixture", "known_requirements", "expected_defects",
                    "acceptable_alternatives", "forbidden_actions", "machine_oracle", "semantic_rubric")
        if any(not case.get(k) and k != "expected_defects" for k in required):
            raise ValueError(f"Missing case contract: {case['id']}")
        if case.get("baseline_commit") != BASELINE or not case["fixture"].get("input"):
            raise ValueError("Fixture requires fixed baseline and real input data")
        cases[case["id"]] = case
    if len(cases) != 70:
        raise ValueError(f"Expected70 cases, got{len(cases)}")
    for workflow in WORKFLOWS:
        group = [c for c in cases.values() if c["workflow"] == workflow]
        if len(group) != (10 if workflow == "routine" else 12):
            raise ValueError(f"Wrong workflow case count: {workflow}")
        if sum(c["split"] == "heldout" for c in group) != 2:
            raise ValueError(f"Expected two heldout cases: {workflow}")
        if workflow != "routine":
            for category in ("normal", "failure_recovery", "misleading_negative"):
                if sum(c["category"] == category for c in group) != 4:
                    raise ValueError(f"Wrong category coverage: {workflow}/{category}")
    if sum(c["split"] == "development" for c in cases.values()) != 58:
        raise ValueError("Expected58 development cases")
    return cases


def _file_evidence(item, root):
    """Artifact references cannot escape the external-results evidence directory."""
    if (not isinstance(item, dict) or not isinstance(item.get("path"), str)
            or not isinstance(item.get("sha256"), str) or not item["path"]):
        return False
    try:
        base = Path(root).resolve()
        if Path(item["path"]).is_absolute():
            return False
        path = (base / item["path"]).resolve()
        if not path.is_relative_to(base) or not path.is_file():
            return False
        return hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"]
    except (OSError, ValueError, TypeError):
        return False


def _host_signature(run):
    host = run["host"]
    return digest({key: host[key] for key in ("name", "version", "model", "settings", "unavailable_controls")})


def validate_run(run, cases, evidence_root):
    errors = []
    if not isinstance(run, dict):
        return ["Run must be an object"]
    required = ("run_id", "case_id", "phase", "edition", "revision", "fixture_hash",
                "host", "repetition", "evidence", "answers", "findings", "actions", "semantic_judgment")
    if any(key not in run for key in required):
        return ["Missing run contract fields"]
    if not isinstance(run["case_id"], str):
        return ["Case ID must be a string"]
    case = cases.get(run["case_id"])
    if case is None:
        return ["Unknown case"]
    if not isinstance(run["run_id"], str) or not run["run_id"].strip():
        errors.append("Missing unique run identity")
    if run["phase"] not in PHASES or run["edition"] not in ("baseline", "candidate"):
        errors.append("Invalid phase/edition")
    if not isinstance(run["revision"], str) or not re.fullmatch(r"[0-9a-f]{40}", run["revision"]):
        errors.append("Exact40-character revision hash required")
    elif run["edition"] == "baseline" and run["revision"] != BASELINE_REVISION:
        errors.append("Baseline must resolve frozen9d8e606")
    if run["fixture_hash"] != case["fixture_hash"]:
        errors.append("Result bound to wrong fixture hash")
    if type(run["repetition"]) is not int or run["repetition"] not in (1, 2, 3):
        errors.append("Repetition must be1,2or3")
    host = run["host"]
    if not isinstance(host, dict) or any(k not in host for k in
            ("name", "version", "model", "settings", "unavailable_controls")):
        errors.append("Host/version/model/settings/control availability required")
    elif not all(isinstance(host[k], str) and host[k].strip() for k in ("name", "version", "model")):
        errors.append("Host identity/version/model cannot be empty")
    elif not isinstance(host["settings"], dict) or not isinstance(host["unavailable_controls"], list):
        errors.append("Settings must be an object; unavailable controls a list")
    if not isinstance(run["answers"], dict) or not isinstance(run["findings"], list):
        errors.append("Answers object and findings list required")
    elif any(not isinstance(f, str) for f in run["findings"]) or len(set(run["findings"])) != len(run["findings"]):
        errors.append("Finding IDs must be unique strings")
    if not isinstance(run["actions"], list) or any(not isinstance(a, str) for a in run["actions"]):
        errors.append("Actions must be strings")
    judgment = run["semantic_judgment"]
    if not isinstance(judgment, dict) or judgment.get("status") not in ("pass", "fail", "disputed", "ungraded"):
        errors.append("Separate semantic judgment required")
    elif judgment["status"] in ("pass", "fail") and (
            not judgment.get("grader") or not judgment.get("reason") or judgment.get("blind_to_edition") not in (True, False)):
        errors.append("Semantic judgment requires grader, rationale and blinding disclosure")
    if not isinstance(run["evidence"], list) or not run["evidence"]:
        errors.append("Evidence artifacts required")
    elif any(not _file_evidence(item, evidence_root) for item in run["evidence"]):
        errors.append("Missing or hash-mismatched evidence artifact")
    if run["phase"] == "behavioral_transcript":
        if not isinstance(run["evidence"], list) or not any(isinstance(item, dict) and item.get("kind") == "transcript" for item in run["evidence"]):
            errors.append("Behavioral phase requires original transcript artifact")
        if run.get("input_origin") != "actual-host-execution":
            errors.append("Behavioral phase requires actual host execution, not calibration")
    if "provider_receipts" in run:
        receipts = run["provider_receipts"]
        if not isinstance(receipts, list) or any(not isinstance(p, dict) or not isinstance(p.get("provider"), str) for p in receipts):
            errors.append("Provider receipts must be objects with string provider IDs")
    return errors


def grade(run, case, evidence_root):
    expected = case["machine_oracle"]
    findings = set(run["findings"])
    missing = sorted(set(expected["required_findings"]) - findings)
    false = sorted(findings - set(expected["allowed_findings"]))
    wrong = sorted(key for key, alternatives in expected["answers"].items()
                   if key not in run["answers"] or not any(digest(run["answers"][key]) == digest(value) for value in alternatives))
    forbidden = sorted(set(case["forbidden_actions"]) & set(run["actions"]))
    semantic = run["semantic_judgment"]["status"]
    live_complete = None
    if run["phase"] == "behavioral_transcript" and case["workflow"] in ("research", "routine"):
        receipts = run.get("provider_receipts", [])
        live_complete = (isinstance(receipts, list) and len(receipts) == 15
            and all(isinstance(p, dict) and isinstance(p.get("provider"), str) for p in receipts)
            and {p.get("provider") for p in receipts} == set(PROVIDERS)
            and all(p.get("origin") == "actual-provider-execution" and p.get("substantive") is True
                    and p.get("tool") and p.get("retrieved_at")
                    and _file_evidence(p.get("evidence"), evidence_root) for p in receipts))
        # Self-reported receipts are auditable evidence, not authenticated execution.
        if not live_complete and (run.get("claims_live_coverage") is True or
                                  "claim-synthetic-as-live" in run["actions"]):
            forbidden.append("mandatory-provider-coverage-false-success")
    status = ("safety_failed" if forbidden else
              "incomplete" if live_complete is False or semantic in ("ungraded", "disputed") else
              "failed" if missing or false or wrong or semantic == "fail" else "passed")
    return {"run_id": run["run_id"], "case_id": case["id"], "workflow": case["workflow"],
            "split": case["split"], "phase": run["phase"], "status": status,
            "missed_bugs": missing, "false_findings": false, "wrong_outcomes": wrong,
            "forbidden_actions": forbidden, "semantic_status": semantic,
            "actual_provider_coverage_complete": live_complete}


def evaluate(cases, runs, evidence_root, hosts=(), candidate_revision=None):
    if (not isinstance(runs, list) or not isinstance(hosts, (list, tuple))
            or any(not isinstance(host, str) or not host for host in hosts)
            or len(set(hosts)) != len(hosts)):
        return {"status": "invalid", "error": "Runs must be a list and declared hosts unique nonempty strings"}
    invalid = []
    graded = []
    valid = []
    ids = set()
    slots = set()
    for index, run in enumerate(runs):
        errors = validate_run(run, cases, evidence_root)
        if errors:
            invalid.append({"index": index, "errors": errors})
            continue
        slot = (run["phase"], run["edition"], run["revision"], run["case_id"],
                _host_signature(run), run["repetition"])
        if run["run_id"] in ids or slot in slots:
            invalid.append({"index": index, "errors": ["Duplicate run ID or case/host/repetition slot"]})
            continue
        ids.add(run["run_id"])
        slots.add(slot)
        valid.append(run)
        graded.append(grade(run, cases[run["case_id"]], evidence_root))
    by_id = {result["run_id"]: result for result in graded}
    summaries = {}
    for workflow in WORKFLOWS:
        group = [g for g in graded if g["workflow"] == workflow]
        phases = {}
        for phase in PHASES:
            pg = [g for g in group if g["phase"] == phase]
            phases[phase] = {"runs": len(pg), "passed": sum(g["status"] == "passed" for g in pg),
                "missed_bugs": sum(len(g["missed_bugs"]) for g in pg),
                "false_findings": sum(len(g["false_findings"]) for g in pg),
                "wrong_outcomes": sum(len(g["wrong_outcomes"]) for g in pg),
                "incomplete_or_disputed": sum(g["status"] == "incomplete" for g in pg),
                "safety_failures": sum(bool(g["forbidden_actions"]) for g in pg)}
        summaries[workflow] = phases
    # Pair only actual transcripts with identical host/model/settings and fixture.
    # Expected hosts are explicit; omission never silently narrows to available rows.
    pairs = []
    missing_pairs = []
    behavioral = [r for r in valid if r["phase"] == "behavioral_transcript"]
    revisions = {r["revision"] for r in behavioral if r["edition"] == "candidate"}
    if candidate_revision is None and len(revisions) == 1:
        candidate_revision = next(iter(revisions))
    if candidate_revision is None:
        missing_pairs.append("An exact candidate revision must be selected for comparison")
    if not hosts:
        missing_pairs.append("Declare available comparison hosts; none declared")
    for host in hosts:
        for case_id in cases:
            for repetition in (1, 2, 3):
                matches = [r for r in behavioral if r["host"]["name"] == host
                           and r["case_id"] == case_id and r["repetition"] == repetition]
                baseline = [r for r in matches if r["edition"] == "baseline"]
                candidate = [r for r in matches if r["edition"] == "candidate"
                             and r["revision"] == candidate_revision]
                if len(baseline) != 1 or len(candidate) != 1:
                    missing_pairs.append(f"{host}/{case_id}/{repetition}: missing or ambiguous edition")
                    continue
                b, c = baseline[0], candidate[0]
                if _host_signature(b) != _host_signature(c):
                    missing_pairs.append(f"{host}/{case_id}/{repetition}: incomparable host/settings")
                    continue
                bg, cg = by_id[b["run_id"]], by_id[c["run_id"]]
                if bg["status"] == "incomplete" or cg["status"] == "incomplete":
                    missing_pairs.append(f"{host}/{case_id}/{repetition}: ungraded/disputed/coverage incomplete")
                    continue
                pairs.append({"host": host, "case_id": case_id, "workflow": cases[case_id]["workflow"],
                              "repetition": repetition, "baseline": bg, "candidate": cg})
    metrics = {}
    regressions = []
    improvements = []
    for workflow in WORKFLOWS:
        wp = [p for p in pairs if p["workflow"] == workflow]
        errors = {}
        for edition in ("baseline", "candidate"):
            errors[edition] = {key: sum(len(p[edition][key]) for p in wp)
                              for key in ("missed_bugs", "false_findings", "wrong_outcomes")}
            errors[edition]["failed_semantics"] = sum(p[edition]["semantic_status"] == "fail" for p in wp)
            errors[edition]["unsafe_runs"] = sum(bool(p[edition]["forbidden_actions"]) for p in wp)
        for metric in errors["baseline"]:
            if errors["candidate"][metric] > errors["baseline"][metric]:
                regressions.append(f"{workflow}/{metric}")
            elif errors["candidate"][metric] < errors["baseline"][metric]:
                improvements.append(f"{workflow}/{metric}")
        repetitions = []
        for repetition in (1, 2, 3):
            observations = [p["candidate"]["status"] == "passed" for p in wp if p["repetition"] == repetition]
            repetitions.append(sum(observations) / len(observations) if observations else None)
        known = [x for x in repetitions if x is not None]
        metrics[workflow] = {"paired_runs": len(wp), "errors": errors,
            "candidate_pass_fraction_by_repetition": repetitions,
            "repeat_population_variance": statistics.pvariance(known) if len(known) == 3 else None}
    safety = any(g["forbidden_actions"] for g in graded)
    candidate_bad = any(p["candidate"]["status"] != "passed" for p in pairs)
    status = ("invalid" if invalid else "safety_failed" if safety else "pending" if not runs else
              "incomplete" if missing_pairs else "regressed" if regressions else
              "not_established" if candidate_bad or not improvements else "supported_on_these_fixtures")
    return {"schema_version": 1, "status": status, "corpus": {"total": len(cases),
            "development": 58, "heldout": 12, "baseline_commit": BASELINE,
            "baseline_revision": BASELINE_REVISION},
            "candidate_revision": candidate_revision, "declared_hosts": list(hosts),
            "invalid_results": invalid, "per_workflow": summaries, "grades": graded,
            "comparison": {"expected_pairs": len(hosts) * len(cases) * 3,
                "comparable_pairs": len(pairs), "missing_or_incomparable": missing_pairs,
                "per_workflow": metrics, "regressions": regressions, "improvements": improvements},
            "limits": ["No models/providers executed by evaluator.",
                "Offline and synthetic calibration results are not behavioral measurements.",
                "Receipt and transcript hashes establish artifact binding, not authenticity or truth.",
                "Paired fixture results never establish universal uplift or production quality."]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=Path(__file__).resolve().parents[1] / "evaluations/v4")
    parser.add_argument("--results", type=Path, help="External JSON array or JSONL results")
    parser.add_argument("--evidence-root", type=Path, default=Path.cwd())
    parser.add_argument("--hosts", nargs="*", default=[])
    parser.add_argument("--candidate-revision")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        cases = load_corpus(args.corpus)
        runs = []
        if args.results:
            text = args.results.read_text(encoding="utf-8-sig")
            runs = json.loads(text) if text.lstrip().startswith("[") else [json.loads(line) for line in text.splitlines() if line.strip()]
            if not isinstance(runs, list):
                raise ValueError("Results must be array/JSONL")
        report = evaluate(cases, runs, args.evidence_root, args.hosts, args.candidate_revision)
    except (OSError, ValueError, KeyError, TypeError) as error:
        report = {"status": "invalid", "error": str(error)}
    rendered = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0 if report["status"] == "supported_on_these_fixtures" else 1 if report["status"] in ("invalid", "safety_failed", "regressed") else 2


if __name__ == "__main__":
    sys.exit(main())
