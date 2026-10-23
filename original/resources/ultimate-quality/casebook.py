#!/usr/bin/env python3
"""Local evidence casebook. This validates records, not actors, permission or truth.

Mutations serialize using an exclusive lock and require the last observed generation.
No lock is automatically stolen. Inspect/recover interrupted runs explicitly.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import stat
import subprocess
import threading
import time
import uuid


SCHEMA = 1
TYPES = {"question", "claim", "requirement", "assumption", "decision", "interface",
         "task", "hypothesis", "experiment", "check", "review", "finding"}
PLAN_TYPES = {"requirement", "assumption", "decision", "interface", "task", "check"}
IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9_.:-]{0,95}\Z")


class Invalid(ValueError):
    """Malformed, stale or conflicting input; no state mutation is committed."""


class Blocked(Invalid):
    """A valid request cannot proceed through a current technical gate."""


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise Invalid(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=_pairs,
                          parse_constant=lambda value: (_ for _ in ()).throw(Invalid(value)))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise Invalid(f"cannot read JSON: {error}") from error


def _id(value):
    if not isinstance(value, str) or not IDENTIFIER.fullmatch(value):
        raise Invalid("invalid record/run/actor identifier")
    return value


def _text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise Invalid(f"{label} must be nonempty text")
    return value


def _list(value, label):
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise Invalid(f"{label} must be a string list")
    if len(value) != len(set(value)):
        raise Invalid(f"{label} has duplicates")
    return value


def safe_path(path, root=None, must_exist=False):
    """Reject traversal and links/reparse points, including existing ancestors."""
    path = Path(path)
    if ".." in path.parts:
        raise Invalid("path traversal is forbidden")
    if root is not None:
        if path.is_absolute() or path.drive:
            raise Invalid("scoped paths must be relative")
        path = Path(root) / path
    absolute = Path(os.path.abspath(path))
    for part in [*reversed(absolute.parents), absolute]:
        try:
            info = part.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
            raise Invalid("symlink/reparse paths are forbidden")
    absolute = absolute.resolve(strict=False)
    if root is not None:
        base = Path(root).resolve()
        if absolute != base and base not in absolute.parents:
            raise Invalid("path is outside scope")
    if must_exist and not absolute.exists():
        raise Invalid("required path is missing")
    return absolute


def _file_hash(path):
    if not path.exists():
        return None
    if not path.is_file():
        raise Invalid("input/artifact path must identify a file")
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            value.update(chunk)
    return value.hexdigest()


def _now():
    return datetime.now(timezone.utc).isoformat()


class Casebook:
    def __init__(self, run_dir):
        self.root = safe_path(run_dir)
        self.path = self.root / "casebook.json"
        self.lock = self.root / ".casebook.lock"

    @classmethod
    def init(cls, run_dir, repo, run_id, scope, authorization, inputs=None,
             repair_limit=3, review_limit=3):
        book = cls(run_dir)
        repo = safe_path(repo, must_exist=True)
        _id(run_id)
        _text(scope, "scope")
        _text(authorization, "authorization")
        for value in (repair_limit, review_limit):
            if type(value) is not int or value < 1:
                raise Invalid("configured bounds must be positive integers")
        paths = _list(inputs or [], "inputs")
        for path in paths:
            safe_path(path, repo)
        baseline = cls._head(repo)
        book.root.mkdir(parents=True, exist_ok=True)
        with book._locked():
            if book.path.exists():
                raise Invalid("casebook already exists; old checkpoints are not migrated/overwritten")
            state = {"schema_version": SCHEMA, "run_id": run_id, "scope": scope,
                     "authorization": authorization, "repo": str(repo),
                     "baseline_revision": baseline, "input_paths": paths,
                     "scope_fingerprint": digest([str(repo), scope, authorization, paths]),
                     "generation": 0, "created_at": _now(),
                     "config": {"repair_limit": repair_limit, "review_limit": review_limit},
                     "records": {}, "history": {}, "checks": {}, "tasks": {}, "closures": {},
                     "final_rounds": 0, "repair_review": None, "events": []}
            state["baseline_inputs"] = book._hashes(state, paths)
            book._validate(state)
            book._save(state)
        return book.validate()

    @staticmethod
    def _head(repo):
        try:
            result = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"],
                                    check=True, capture_output=True, text=True, timeout=10)
        except (OSError, subprocess.SubprocessError) as error:
            raise Invalid("repository must have a readable Git HEAD") from error
        return result.stdout.strip()

    @contextmanager
    def _locked(self):
        safe_path(self.root, must_exist=True)
        try:
            descriptor = os.open(self.lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError as error:
            raise Invalid("run is locked; do not steal an active/interrupted lock") from error
        try:
            os.write(descriptor, canonical({"pid": os.getpid(), "time": _now()}))
            os.fsync(descriptor)
            yield
        finally:
            os.close(descriptor)
            self.lock.unlink()

    def _load(self):
        safe_path(self.path, must_exist=True)
        state = read_json(self.path)
        if not isinstance(state, dict):
            raise Invalid("state must be an object")
        expected = state.pop("digest", None)
        if expected != digest(state):
            raise Invalid("state digest mismatch; preserve checkpoint for recovery")
        self._validate(state)
        return state

    def _save(self, state):
        state = deepcopy(state)
        state["digest"] = digest(state)
        temporary = safe_path(".casebook-" + uuid.uuid4().hex + ".tmp", self.root)
        try:
            with temporary.open("xb") as stream:
                stream.write(canonical(state) + b"\n")
                stream.flush()
                os.fsync(stream.fileno())
            safe_path(self.path)
            os.replace(temporary, self.path)
        finally:
            if temporary.exists():
                temporary.unlink()

    def _update(self, generation, event, operation):
        if type(generation) is not int:
            raise Invalid("expected generation is required")
        with self._locked():
            original = self.path.read_bytes()
            state = self._load()
            if state["generation"] != generation:
                raise Invalid("stale generation; reload before retrying")
            result = operation(state)
            self._validate(state)
            state["generation"] += 1
            state["events"].append({"event": event, "time": _now(),
                                    "generation": state["generation"]})
            if self.path.read_bytes() != original:
                raise Invalid("state changed during operation; refusing concurrent overwrite")
            self._save(state)
            return {"status": "recorded", "generation": state["generation"], **(result or {})}

    def _hashes(self, state, paths):
        repo = safe_path(state["repo"], must_exist=True)
        return {path: _file_hash(safe_path(path, repo)) for path in sorted(set(paths))}

    def _code_paths(self, state):
        paths = set(state["input_paths"])
        for record in state["records"].values():
            if record["type"] == "task":
                paths.update(record["data"].get("paths", []))
            if record["type"] in {"check", "finding"}:
                paths.update(record["data"].get("inputs", record["data"].get("paths", [])))
        return sorted(paths)

    def _code_stamp(self, state, paths=None):
        return {"revision": self._head(state["repo"]),
                "inputs": self._hashes(state, self._code_paths(state) if paths is None else paths)}

    def _plan_stamp(self, state):
        records = [{key: record[key] for key in ("id", "type", "data", "links")}
                   for _, record in sorted(state["records"].items())
                   if record["type"] in PLAN_TYPES]
        # Follow explicit revision links: supporting claims/questions are plan inputs,
        # but unrelated research records do not invalidate an otherwise unchanged plan.
        dependencies = {}
        def collect(key):
            for link in state["records"][key]["links"]:
                target = state["records"][link["id"]]
                if target["id"] not in dependencies:
                    dependencies[target["id"]] = target
                    collect(target["id"])
        for record in records:
            collect(record["id"])
        expected_outputs = set()
        for record in state["records"].values():
            if record["type"] == "task":
                expected_outputs.update(record["data"].get("paths", []))
        inputs = [path for path in state["input_paths"] if path not in expected_outputs]
        return {"scope": state["scope_fingerprint"], "plan_hash": digest([records, dependencies]),
                "inputs": self._hashes(state, inputs)}

    def _validate(self, state):
        required = {"schema_version", "run_id", "scope", "authorization", "repo",
                    "baseline_revision", "baseline_inputs", "input_paths", "scope_fingerprint", "generation",
                    "created_at", "config", "records", "history", "checks", "tasks", "closures",
                    "final_rounds", "repair_review", "events"}
        if set(state) != required or state["schema_version"] != SCHEMA:
            raise Invalid("unknown schema/state fields; no implicit checkpoint migration")
        _id(state["run_id"])
        if type(state["generation"]) is not int or state["generation"] < 0:
            raise Invalid("invalid generation")
        repo = safe_path(state["repo"], must_exist=True)
        if digest([str(repo), state["scope"], state["authorization"], state["input_paths"]]) != state["scope_fingerprint"]:
            raise Invalid("scope fingerprint mismatch")
        for path in _list(state["input_paths"], "inputs"):
            safe_path(path, repo)
        if (not isinstance(state["baseline_inputs"], dict)
                or set(state["baseline_inputs"]) != set(state["input_paths"])
                or any(value is not None and (not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value))
                       for value in state["baseline_inputs"].values())):
            raise Invalid("invalid baseline input hashes")
        for field in ("records", "history", "checks", "tasks", "closures", "config"):
            if not isinstance(state[field], dict):
                raise Invalid(field + " must be an object")
        if (set(state["config"]) != {"repair_limit", "review_limit"}
                or any(type(value) is not int or value < 1 for value in state["config"].values())):
            raise Invalid("invalid fixed run bounds")
        if type(state["final_rounds"]) is not int or not 0 <= state["final_rounds"] <= state["config"]["review_limit"]:
            raise Invalid("invalid final repair-round counter")
        if not isinstance(state["events"], list):
            raise Invalid("events must be a list")
        records = state["records"]
        if not isinstance(records, dict):
            raise Invalid("records must be an object")
        history = state["history"]
        if not isinstance(history, dict) or any(key not in records for key in history):
            raise Invalid("history must reference existing record IDs")
        for key, versions in history.items():
            if not isinstance(versions, list):
                raise Invalid("record history must be a list")
            for index, version in enumerate(versions, 1):
                if (not isinstance(version, dict) or set(version) != {"id", "type", "revision", "data", "links"}
                        or version["id"] != key or version["type"] != records[key]["type"]
                        or version["revision"] != index or not isinstance(version["data"], dict)
                        or not isinstance(version["links"], list)):
                    raise Invalid("invalid historical record revision")
        edges = {}
        for key, record in records.items():
            if not isinstance(record, dict) or set(record) != {"id", "type", "revision", "data", "links"}:
                raise Invalid("invalid typed record")
            if _id(key) != record["id"] or record["type"] not in TYPES:
                raise Invalid("record identity/type mismatch")
            if (type(record["revision"]) is not int or record["revision"] != len(history.get(key, [])) + 1
                    or not isinstance(record["data"], dict)):
                raise Invalid("invalid record revision/data")
            if not isinstance(record["links"], list):
                raise Invalid("links must be a list")
            linked = set()
            for link in record["links"]:
                if not isinstance(link, dict) or set(link) != {"id", "revision"}:
                    raise Invalid("links require ID and exact revision")
                target = records.get(link["id"])
                if (target is None or type(link["revision"]) is not int
                        or not 1 <= link["revision"] <= target["revision"] or link["id"] in linked):
                    raise Invalid("missing, invalid or duplicate record link")
                linked.add(link["id"])
            edges[key] = set(linked)
            data = record["data"]
            if "evidence_status" in data and data["evidence_status"] not in {"observed", "inferred", "failed", "unavailable", "unverified", "superseded"}:
                raise Invalid("invalid evidence status")
            for field in ("paths", "inputs"):
                for path in _list(data.get(field, []), field):
                    safe_path(path, repo)
            references = []
            if record["type"] == "task":
                _text(data.get("owner"), "task owner")
                _text(data.get("recovery"), "task recovery")
                references.extend((item, "task") for item in _list(data.get("dependencies", []), "dependencies"))
                references.extend((item, "check") for item in _list(data.get("checks", []), "checks"))
                edges[key].update(data.get("dependencies", []))
            if record["type"] == "requirement":
                if type(data.get("hard", True)) is not bool:
                    raise Invalid("hard must be a boolean")
                references.extend((item, "task") for item in _list(data.get("tasks", []), "tasks"))
                references.extend((item, "check") for item in _list(data.get("checks", []), "checks"))
            if record["type"] == "finding":
                if data.get("severity") not in {"P0", "P1", "P2", "P3"} or data.get("mode") not in {"plan", "code"}:
                    raise Invalid("finding requires severity and mode")
                _text(data.get("reason"), "finding reason")
                if data["mode"] == "code":
                    references.append((data.get("task"), "task"))
                references.extend((item, "check") for item in _list(data.get("checks", []), "checks"))
            if record["type"] == "check":
                argv = data.get("argv")
                if not isinstance(argv, list) or not argv or any(not isinstance(arg, str) or not arg or "\x00" in arg for arg in argv):
                    raise Invalid("check argv must contain nonempty argument strings")
                timeout = data.get("timeout_seconds", 60)
                if type(timeout) not in (int, float) or not math.isfinite(timeout) or not 0 < timeout <= 300:
                    raise Invalid("check timeout must be between 0 and 300 seconds")
                cap = data.get("max_output_bytes", 1024 * 1024)
                if type(cap) is not int or not 1 <= cap <= 10 * 1024 * 1024:
                    raise Invalid("check output cap must be 1..10485760 bytes")
                if type(data.get("mandatory", True)) is not bool:
                    raise Invalid("mandatory must be a boolean")
                safe_path(data.get("cwd", "."), repo, must_exist=True)
            for target, expected_type in references:
                if target not in records or records[target]["type"] != expected_type:
                    raise Invalid("missing reference or wrong record type")
        visiting, visited = set(), set()

        def visit(key):
            if key in visiting:
                raise Invalid("cyclic record/task dependencies")
            if key in visited:
                return
            visiting.add(key)
            for target in edges[key]:
                visit(target)
            visiting.remove(key)
            visited.add(key)

        for key in records:
            visit(key)
        for receipt_id, receipt in state["checks"].items():
            _id(receipt_id)
            if receipt.get("check_id") not in records or records[receipt["check_id"]]["type"] != "check":
                raise Invalid("check receipt references missing check")
            for field in ("stdout", "stderr"):
                artifact = receipt[field]
                path = safe_path(artifact["path"], self.root, must_exist=True)
                if _file_hash(path) != artifact["sha256"]:
                    raise Invalid("check artifact missing/changed; evidence is corrupt")
        canonical(state)  # Reject non-JSON values/NaN before committing.

    def validate(self):
        state = self._load()
        return {"status": "valid", "generation": state["generation"],
                "run_id": state["run_id"], "plan": self._plan_stamp(state),
                "limits": "Actor identity, authority, source truth and check semantics are not authenticated."}

    def put(self, record, expected_generation):
        def operation(state):
            if not isinstance(record, dict) or set(record) - {"id", "type", "data", "links"}:
                raise Invalid("put accepts id/type/data/links only")
            key = _id(record.get("id"))
            kind = record.get("type")
            if kind not in TYPES - {"review"}:
                raise Invalid("unknown/protected record type; reviews use review operation")
            previous = state["records"].get(key)
            if previous and (previous["type"] != kind or kind == "finding"):
                raise Invalid("record type/finding identity is immutable")
            if previous:
                state["history"].setdefault(key, []).append(deepcopy(previous))
            state["records"][key] = {"id": key, "type": kind,
                "revision": 1 if previous is None else previous["revision"] + 1,
                "data": deepcopy(record.get("data")), "links": deepcopy(record.get("links", []))}
            return {"id": key, "revision": state["records"][key]["revision"]}
        return self._update(expected_generation, "put", operation)

    def _current_check(self, state, receipt_id, exact_revision=True):
        receipt = state["checks"].get(receipt_id)
        if not receipt or receipt["status"] != "passed":
            return False
        check = state["records"][receipt["check_id"]]
        current = self._code_stamp(state, list(receipt["stamp"]["inputs"]))
        return (check["revision"] == receipt["check_record_revision"]
                and receipt["stamp"] == receipt["end_stamp"]
                and receipt["stamp"]["inputs"] == current["inputs"]
                and (not exact_revision or receipt["stamp"]["revision"] == current["revision"]))

    def _evidence(self, state, evidence, check_ids=None, exact_revision=True):
        evidence = _list(evidence, "evidence")
        if not evidence or any(not self._current_check(state, key, exact_revision) for key in evidence):
            raise Blocked("current passed check receipts are required")
        supplied = {state["checks"][key]["check_id"] for key in evidence}
        if not set(check_ids or []).issubset(supplied):
            raise Blocked("required checks are absent from current evidence")

    def _finding_open(self, state, key):
        record = state["records"][key]
        closure = state["closures"].get(key)
        if not closure or closure["status"] not in {"verified-fixed", "non-actionable-with-reason"}:
            return True
        if closure["record_revision"] != record["revision"]:
            return True
        current = self._plan_stamp(state) if record["data"]["mode"] == "plan" else self._code_stamp(state)
        if closure["stamp"] != current:
            return True
        try:
            self._evidence(state, closure["evidence"], record["data"].get("checks", []))
        except Blocked:
            return True
        return False

    def _ready_plan(self, state):
        current = self._plan_stamp(state)
        reviews = [r for r in state["records"].values() if r["type"] == "review"
                   and r["data"]["mode"] == "plan" and r["data"]["plan"] == current]
        if not reviews or max(reviews, key=lambda r: r["data"]["sequence"])["data"]["verdict"] != "ready":
            raise Blocked("current ready plan review is required")
        if self._plan_gaps(state):
            raise Blocked("plan readiness conditions are no longer satisfied")
        return max(reviews, key=lambda r: r["data"]["sequence"])["id"]

    def _plan_gaps(self, state):
        gaps = []
        relevant = {r["id"] for r in state["records"].values() if r["type"] in PLAN_TYPES}
        pending = list(relevant)
        while pending:
            key = pending.pop()
            for link in state["records"][key]["links"]:
                if state["records"][link["id"]]["revision"] != link["revision"]:
                    gaps.append("stale plan evidence link: " + key + " -> " + link["id"])
                if link["id"] not in relevant:
                    relevant.add(link["id"])
                    pending.append(link["id"])
        requirements = [r for r in state["records"].values() if r["type"] == "requirement"]
        if not requirements:
            gaps.append("no requirements")
        for record in requirements:
            data = record["data"]
            if data.get("hard", True) and (not data.get("tasks") or not data.get("checks")):
                gaps.append("hard requirement lacks tasks/checks: " + record["id"])
        for record in state["records"].values():
            data = record["data"]
            if record["type"] == "task" and (not data.get("paths") or not data.get("checks")):
                gaps.append("task lacks ownership/checks: " + record["id"])
            if record["type"] == "assumption" and data.get("consequential") and data.get("status") != "supported":
                if not (data.get("status") == "accepted-bounded" and data.get("decision") and data.get("mitigation")
                        and data["decision"] in state["records"] and state["records"][data["decision"]]["type"] == "decision"):
                    gaps.append("consequential assumption unresolved: " + record["id"])
            if record["type"] == "finding" and data["mode"] == "plan" and data["severity"] in {"P0", "P1"} and self._finding_open(state, record["id"]):
                gaps.append("open plan finding: " + record["id"])
        return gaps

    def record_check(self, check_id, actor, expected_generation):
        _id(actor)
        def operation(state):
            record = state["records"].get(check_id)
            if not record or record["type"] != "check":
                raise Invalid("unknown check ID")
            data = record["data"]
            paths = data.get("inputs", self._code_paths(state))
            stamp = self._code_stamp(state, paths)
            receipt_id = "check-" + uuid.uuid4().hex
            directory = safe_path("checks", self.root)
            directory.mkdir(exist_ok=True)
            outputs = {name: safe_path(f"checks/{receipt_id}.{name}", self.root) for name in ("stdout", "stderr")}
            start = time.monotonic()
            status, returncode, error = "failed_to_start", None, None
            cap = data.get("max_output_bytes", 1024 * 1024)
            total = [0]
            guard = threading.Lock()
            exceeded = threading.Event()
            with outputs["stdout"].open("xb") as stdout, outputs["stderr"].open("xb") as stderr:
                try:
                    process = subprocess.Popen(data["argv"], cwd=safe_path(data.get("cwd", "."), state["repo"], True),
                                               shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except OSError as exc:
                    error = str(exc)
                    stderr.write(error.encode("utf-8", errors="replace")[:cap])
                else:
                    def copy_output(source, target):
                        try:
                            for chunk in iter(lambda: source.read(4096), b""):
                                with guard:
                                    allowed = max(0, cap - total[0])
                                    target.write(chunk[:allowed])
                                    total[0] += min(len(chunk), allowed)
                                    if len(chunk) > allowed:
                                        exceeded.set()
                                        break
                        finally:
                            source.close()
                    readers = [threading.Thread(target=copy_output, args=(process.stdout, stdout), daemon=True),
                               threading.Thread(target=copy_output, args=(process.stderr, stderr), daemon=True)]
                    for reader in readers:
                        reader.start()
                    status = "running"
                    while process.poll() is None:
                        if exceeded.is_set() or time.monotonic() - start > data.get("timeout_seconds", 60):
                            status = "output_limit" if exceeded.is_set() else "timeout"
                            process.kill()
                            break
                        time.sleep(0.01)
                    returncode = process.wait(timeout=5)
                    for reader in readers:
                        reader.join(timeout=1)
                    if any(reader.is_alive() for reader in readers):
                        raise Invalid("descendant retains output pipes; preserve artifacts and inspect owned process tree")
                    if status == "running":
                        status = "output_limit" if exceeded.is_set() else ("passed" if returncode == 0 else "failed")
            receipt = {"id": receipt_id, "check_id": check_id,
                       "check_record_revision": record["revision"], "actor": actor,
                       "observed_at": _now(), "argv": data["argv"], "cwd": data.get("cwd", "."),
                       "status": status, "exit_code": returncode, "error": error,
                       "duration_seconds": time.monotonic() - start, "stamp": stamp,
                       "end_stamp": self._code_stamp(state, paths)}
            for name, path in outputs.items():
                receipt[name] = {"path": path.relative_to(self.root).as_posix(), "sha256": _file_hash(path)}
            state["checks"][receipt_id] = receipt
            return {"receipt": receipt, "status": "recorded" if status == "passed" else "incomplete"}
        return self._update(expected_generation, "record-check", operation)

    def review(self, review_id, mode, actor, verdict, expected_generation, evidence=None):
        _id(review_id)
        _id(actor)
        if mode not in {"plan", "code"} or verdict not in {"ready", "needs_revision", "blocked"}:
            raise Invalid("invalid review mode/verdict")
        def operation(state):
            if review_id in state["records"]:
                raise Invalid("review IDs are immutable and unique")
            data = {"mode": mode, "actor": actor, "verdict": verdict,
                    "plan": self._plan_stamp(state), "observed_at": _now(),
                    "evidence": _list(evidence or [], "evidence"),
                    "sequence": state["generation"] + 1}
            if mode == "plan":
                if verdict == "ready" and self._plan_gaps(state):
                    raise Blocked("plan has unresolved material gaps: " + "; ".join(self._plan_gaps(state)))
            else:
                self._ready_plan(state)
                builders = {r["data"]["owner"] for r in state["records"].values() if r["type"] == "task"}
                for runtime in state["tasks"].values():
                    builders.update(runtime.get("builders", []))
                if actor in builders:
                    raise Blocked("final code reviewer must be independent of builders")
                data["code"] = self._code_stamp(state)
                if verdict == "ready":
                    self._completion_gates(state)
                    checks = self._required_checks(state)
                    self._evidence(state, evidence or [], checks)
            state["records"][review_id] = {"id": review_id, "type": "review", "revision": 1, "data": data, "links": []}
            return {"review": review_id, "verdict": verdict, "status": "recorded" if verdict == "ready" else "incomplete"}
        return self._update(expected_generation, "review", operation)

    def _task_valid(self, state, key):
        task = state["tasks"].get(key)
        if not task or task["status"] != "complete" or task["plan"] != self._plan_stamp(state):
            return False
        try:
            self._evidence(state, task["evidence"], state["records"][key]["data"].get("checks", []), exact_revision=False)
        except Blocked:
            return False
        return True

    def task(self, task_id, action, actor, expected_generation, evidence=None):
        _id(actor)
        if action not in {"dispatch", "repair", "complete", "fail", "block"}:
            raise Invalid("invalid task action")
        def operation(state):
            record = state["records"].get(task_id)
            if not record or record["type"] != "task":
                raise Invalid("unknown task")
            prior = state["tasks"].get(task_id, {"status": "pending", "attempts": 0, "builders": []})
            runtime = deepcopy(prior)
            if action in {"dispatch", "repair", "complete"}:
                review = self._ready_plan(state)
                if any(not self._task_valid(state, dep) for dep in record["data"].get("dependencies", [])):
                    raise Blocked("task dependencies have no current valid output")
                runtime["plan_review"] = review
            if action == "dispatch":
                if prior["status"] != "pending":
                    raise Blocked("task is not pending; blocked/failed work resumes only through explicit bounded repair")
                runtime["status"] = "running"
            elif action == "repair":
                if prior["status"] not in {"failed", "blocked", "complete"}:
                    raise Blocked("repair requires a failed/blocked/reviewed task")
                if prior["attempts"] >= state["config"]["repair_limit"]:
                    raise Blocked("task repair limit exhausted")
                reviews = [r for r in state["records"].values() if r["type"] == "review" and r["data"]["mode"] == "code"]
                if reviews:
                    latest = max(reviews, key=lambda r: r["data"]["sequence"])["id"]
                    if state["repair_review"] != latest:
                        if state["final_rounds"] >= state["config"]["review_limit"]:
                            raise Blocked("final review repair-round limit exhausted")
                        state["final_rounds"] += 1
                        state["repair_review"] = latest
                runtime["attempts"] += 1
                runtime["status"] = "running"
            elif action == "complete":
                if prior["status"] not in {"running", "complete"}:
                    raise Blocked("task must be dispatched before completion")
                self._evidence(state, evidence or [], record["data"].get("checks", []))
                runtime.update(status="complete", evidence=list(evidence))
            else:
                if prior["status"] == "pending":
                    raise Blocked("task was not dispatched")
                runtime["status"] = "failed" if action == "fail" else "blocked"
            if action in {"dispatch", "repair"}:
                runtime["builders"] = sorted(set(prior["builders"] + [actor, record["data"]["owner"]]))
            runtime.update(actor=actor, plan=self._plan_stamp(state), updated_at=_now())
            state["tasks"][task_id] = runtime
            return {"task": task_id, "task_state": runtime}
        return self._update(expected_generation, "task", operation)

    def finding(self, finding_id, action, actor, expected_generation, evidence=None, reason=""):
        _id(actor)
        if action not in {"resolved-unverified", "verified-fixed", "non-actionable-with-reason", "blocked"}:
            raise Invalid("invalid finding transition")
        def operation(state):
            record = state["records"].get(finding_id)
            if not record or record["type"] != "finding":
                raise Invalid("unknown finding")
            data = record["data"]
            if action in {"blocked", "non-actionable-with-reason"}:
                _text(reason, "reason")
            if action in {"verified-fixed", "non-actionable-with-reason"}:
                task = state["tasks"].get(data.get("task"), {})
                builders = set(task.get("builders", [])) | {data.get("builder")}
                if data.get("task") in state["records"]:
                    builders.add(state["records"][data["task"]]["data"]["owner"])
                if actor in builders:
                    raise Blocked("builder cannot close their own code finding")
                self._evidence(state, evidence or [], data.get("checks", []))
                if action == "verified-fixed" and state["closures"].get(finding_id, {}).get("status") != "resolved-unverified":
                    raise Blocked("a repair claim must first be resolved-unverified")
            stamp = self._plan_stamp(state) if data["mode"] == "plan" else self._code_stamp(state)
            state["closures"][finding_id] = {"status": action, "actor": actor, "reason": reason,
                "evidence": list(evidence or []), "stamp": stamp,
                "record_revision": record["revision"], "observed_at": _now()}
            return {"finding": finding_id, "finding_state": action}
        return self._update(expected_generation, "finding", operation)

    def _required_checks(self, state):
        checks = set()
        for record in state["records"].values():
            data = record["data"]
            if record["type"] == "check" and data.get("mandatory", True):
                checks.add(record["id"])
            if record["type"] == "task" or (record["type"] == "requirement" and data.get("hard", True)):
                checks.update(data.get("checks", []))
        return sorted(checks)

    def _completion_gates(self, state):
        self._ready_plan(state)
        tasks = [r["id"] for r in state["records"].values() if r["type"] == "task"]
        if not tasks or any(not self._task_valid(state, key) for key in tasks):
            raise Blocked("tasks are not complete with current evidence")
        for key, record in state["records"].items():
            if record["type"] == "finding" and record["data"]["severity"] in {"P0", "P1"} and self._finding_open(state, key):
                raise Blocked("actionable material finding remains open/stale: " + key)

    def report(self):
        state = self._load()
        gaps = []
        try:
            self._completion_gates(state)
        except Blocked as error:
            gaps.append(str(error))
        reviews = [r for r in state["records"].values() if r["type"] == "review" and r["data"]["mode"] == "code"]
        latest = max(reviews, key=lambda r: r["data"]["sequence"]) if reviews else None
        if not latest or latest["data"]["verdict"] != "ready" or latest["data"]["code"] != self._code_stamp(state) or latest["data"]["plan"] != self._plan_stamp(state):
            gaps.append("final code review is absent, unready or stale")
        else:
            checks = self._required_checks(state)
            try:
                self._evidence(state, latest["data"]["evidence"], checks)
            except Blocked as error:
                gaps.append(str(error))
        return {"status": "complete" if not gaps else "incomplete", "generation": state["generation"],
                "run_id": state["run_id"], "plan": self._plan_stamp(state),
                "revision": self._head(state["repo"]), "gaps": gaps,
                "tasks": state["tasks"], "findings": {key: {"open": self._finding_open(state, key),
                    "resolution": state["closures"].get(key)} for key, record in state["records"].items() if record["type"] == "finding"},
                "limits": "Records do not authenticate actors, permissions, semantic truth or check adequacy; no agent orchestration is performed."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("init", "put", "validate", "record-check", "review", "task", "finding", "report"):
        child = sub.add_parser(command)
        child.add_argument("--run-dir", required=True)
        if command not in {"init", "validate", "report"}:
            child.add_argument("--expect-generation", required=True, type=int)
        if command == "init":
            for flag in ("repo", "run-id", "scope", "authorization"):
                child.add_argument("--" + flag, required=True)
            child.add_argument("--inputs", nargs="*", default=[])
            child.add_argument("--repair-limit", type=int, default=3)
            child.add_argument("--review-limit", type=int, default=3)
        elif command == "put":
            child.add_argument("--record", required=True)
        elif command == "record-check":
            child.add_argument("--check-id", required=True)
            child.add_argument("--actor", required=True)
        elif command in {"review", "task", "finding"}:
            child.add_argument("--id", required=True)
            child.add_argument("--actor", required=True)
            child.add_argument("--evidence", nargs="*", default=[])
            if command == "review":
                child.add_argument("--mode", required=True)
                child.add_argument("--verdict", required=True)
            else:
                child.add_argument("--action", required=True)
            if command == "finding":
                child.add_argument("--reason", default="")
    args = parser.parse_args(argv)
    try:
        book = Casebook(args.run_dir)
        if args.command == "init":
            result = Casebook.init(args.run_dir, args.repo, args.run_id, args.scope, args.authorization,
                                   args.inputs, args.repair_limit, args.review_limit)
        elif args.command == "put":
            result = book.put(read_json(safe_path(args.record, must_exist=True)), args.expect_generation)
        elif args.command == "record-check":
            result = book.record_check(args.check_id, args.actor, args.expect_generation)
        elif args.command == "review":
            result = book.review(args.id, args.mode, args.actor, args.verdict, args.expect_generation, args.evidence)
        elif args.command == "task":
            result = book.task(args.id, args.action, args.actor, args.expect_generation, args.evidence)
        elif args.command == "finding":
            result = book.finding(args.id, args.action, args.actor, args.expect_generation, args.evidence, args.reason)
        else:
            result = getattr(book, args.command.replace("-", "_"))()
        print(json.dumps(result, ensure_ascii=False, allow_nan=False))
        return 2 if result["status"] in {"incomplete", "blocked"} else 0
    except Blocked as error:
        print(json.dumps({"status": "blocked", "error": str(error)}))
        return 2
    except (Invalid, KeyError, TypeError, OSError, RecursionError) as error:
        print(json.dumps({"status": "invalid", "error": str(error)}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
