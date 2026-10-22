#!/usr/bin/env python3
"""Local evidence bookkeeping, not a search client or a truth verifier.

init --run-dir DIR --question TEXT --registry FILE
record --run-dir DIR --provider NAME --input FILE
report --run-dir DIR [--claims FILE]

Provider results supplied to this tool must come from actual provider calls.
Synthetic fixtures validate bookkeeping only and never prove live coverage.
"""
import argparse
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

PROVIDERS = (
    "tavily", "context7", "you", "exa", "jina", "serpdive", "linkup",
    "parallel", "serpapi", "github", "firecrawl", "crawleo", "brightdata",
    "apify", "brave",
)
QUERY_WORD_FLOORS = {"you": 150, "exa": 100, "linkup": 200, "parallel": 100, "jina": 80}
STATUSES = {"received", "empty", "failed", "unavailable", "cancelled"}


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def write_json(path, value):
    path = Path(path)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     delete=False, suffix=".tmp") as stream:
        temp = Path(stream.name)
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    try:
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def required_text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be nonempty text")
    return value.strip()


def load_config(run_dir):
    config = read_json(Path(run_dir) / "run.json")
    payload = {k: v for k, v in config.items() if k != "scope_sha256"}
    actual = hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()
    if actual != config.get("scope_sha256"):
        raise ValueError("Run scope/registry changed; initialize a new run directory")
    return config


def canonical_url(value):
    value = required_text(value, "source URL")
    parts = urlsplit(value)
    if parts.scheme not in {"https", "http"} or not parts.hostname or parts.username or parts.password:
        raise ValueError("source URL must be an HTTP(S) URL without credentials")
    query = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
             if not k.lower().startswith("utm_") and k.lower() not in {"fbclid", "gclid"}]
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path or "/",
                       urlencode(sorted(query)), ""))


def initialize(run_dir, question, registry):
    required_text(question, "question")
    if not isinstance(registry, dict) or set(registry) != set(PROVIDERS):
        raise ValueError("registry must contain exactly the 15 required provider IDs")
    for name, item in registry.items():
        if not isinstance(item, dict):
            raise ValueError(f"{name} registry entry must be an object")
        required_text(item.get("tool"), f"{name}.tool")
        query = required_text(item.get("query"), f"{name}.query")
        if name in QUERY_WORD_FLOORS and len(query.split()) < QUERY_WORD_FLOORS[name]:
            raise ValueError(f"{name} requires at least {QUERY_WORD_FLOORS[name]} query words")
    run_dir = Path(run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)
    # Exclusive creation prevents silently reusing a checkpoint for a different scope.
    config = {"schema_version": 1, "question": question, "registry": registry}
    config["scope_sha256"] = hashlib.sha256(
        json.dumps(config, sort_keys=True).encode("utf-8")).hexdigest()
    with (run_dir / "run.json").open("x", encoding="utf-8") as stream:
        json.dump(config, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return config


def validate_result(result):
    if not isinstance(result, dict) or result.get("status") not in STATUSES:
        raise ValueError("result requires a recognized status")
    observed = required_text(result.get("observed_at"), "observed_at")
    try:
        timestamp = datetime.fromisoformat(observed.replace("Z", "+00:00"))
        if timestamp.tzinfo is None:
            raise ValueError("timestamp requires a timezone")
    except ValueError as exc:
        raise ValueError("observed_at must be an ISO timestamp with timezone") from exc
    required_text(result.get("artifact"), "artifact (actual call result location)")
    if result["status"] != "received":
        required_text(result.get("reason"), "reason")
        return
    required_text(result.get("summary"), "provider summary")
    sources = result.get("sources")
    if not isinstance(sources, list) or not sources:
        raise ValueError("received input requires substantive sources")
    for source in sources:
        if not isinstance(source, dict):
            raise ValueError("source must be an evidence object")
        canonical_url(source.get("url"))
        required_text(source.get("evidence"), "source evidence")
        digest = source.get("content_sha256")
        if digest is not None and not re.fullmatch(r"[a-f0-9]{64}", digest):
            raise ValueError("content_sha256 must be a lowercase SHA-256 digest")


def record(run_dir, provider, result):
    if provider not in PROVIDERS:
        raise ValueError("unknown provider")
    run_dir = Path(run_dir)
    config = load_config(run_dir)
    validate_result(result)
    # Per-provider files allow independent providers to finish concurrently.
    # Concurrent updates to the same provider fail rather than dropping an attempt.
    lock = run_dir / f"{provider}.lock"
    fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    try:
        os.close(fd)
        path = run_dir / f"{provider}.json"
        attempts = read_json(path)["attempts"] if path.exists() else []
        attempts.append(result)
        write_json(path, {"scope_sha256": config["scope_sha256"], "attempts": attempts})
    finally:
        lock.unlink(missing_ok=True)


def summarize(run_dir, claims=None):
    run_dir = Path(run_dir)
    config = load_config(run_dir)
    received, statuses, source_sets, identity_links = {}, {}, {}, {}
    def find(item):
        identity_links.setdefault(item, item)
        while identity_links[item] != item:
            item = identity_links[item]
        return item
    for provider in PROVIDERS:
        path = run_dir / f"{provider}.json"
        if not path.exists():
            statuses[provider] = "pending"
            continue
        entry = read_json(path)
        if entry["scope_sha256"] != config["scope_sha256"]:
            raise ValueError(f"stale checkpoint for {provider}")
        result = entry["attempts"][-1]
        validate_result(result)
        statuses[provider] = result["status"]
        if result["status"] == "received":
            received[provider] = result
            source_sets[provider] = {canonical_url(s["url"]) for s in result["sources"]}
            for s in result["sources"]:
                url = canonical_url(s["url"])
                find(url)
                if s.get("content_sha256"):
                    digest = "sha256:" + s["content_sha256"]
                    identity_links[find(url)] = find(digest)
    matrix_valid, errors, unresolved = False, [], []
    if claims is not None:
        if not isinstance(claims, list) or not claims:
            errors.append("claims must be a nonempty list")
        else:
            seen = set()
            for claim in claims:
                try:
                    identifier = required_text(claim.get("id"), "claim.id")
                    if identifier in seen:
                        raise ValueError("duplicate claim ID")
                    seen.add(identifier)
                    required_text(claim.get("text"), "claim.text")
                    positions = claim.get("positions")
                    if not isinstance(positions, dict) or set(positions) != set(PROVIDERS):
                        raise ValueError("each claim needs all 15 provider positions")
                    stances = set()
                    for name, position in positions.items():
                        if name not in received:
                            raise ValueError(f"{name} has no valid received input")
                        stance = position.get("stance")
                        if stance not in {"support", "contradict", "insufficient"}:
                            raise ValueError("invalid stance")
                        required_text(position.get("rationale"), "position.rationale")
                        urls = position.get("sources", [])
                        if not isinstance(urls, list):
                            raise ValueError("position sources must be a list")
                        if stance != "insufficient" and not urls:
                            raise ValueError("support/contradiction needs evidence URLs")
                        if any(canonical_url(u) not in source_sets[name] for u in urls):
                            raise ValueError("position cites an unrecorded provider source")
                        stances.add(stance)
                    review = claim.get("review", {})
                    required_text(review.get("conclusion"), "review.conclusion")
                    required_text(review.get("reasoning"), "review.reasoning")
                    if "support" in stances and "contradict" in stances:
                        if review.get("disagreement") not in {"resolved", "unresolved"}:
                            raise ValueError("contradictory evidence requires disagreement status")
                        if review["disagreement"] == "unresolved":
                            unresolved.append(identifier)
                except (ValueError, TypeError, AttributeError) as exc:
                    errors.append(f"claim {claim.get('id', '?') if isinstance(claim, dict) else '?'}: {exc}")
            matrix_valid = not errors
    return {
        "scope_sha256": config["scope_sha256"], "received_count": len(received),
        "required_count": 15, "collection_complete": len(received) == 15,
        "consensus_complete": len(received) == 15 and matrix_valid,
        "matrix_valid": matrix_valid, "matrix_errors": errors,
        "statuses": statuses, "missing": [p for p in PROVIDERS if p not in received],
        "unique_source_identities": len({find(key) for key in identity_links}),
        "unresolved_claims": unresolved,
        "limitation": "Bookkeeping validates submitted records; it cannot authenticate provider calls or prove truth. Content hashes only help identify exact copies, not all syndication.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["init", "record", "report"])
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--question")
    parser.add_argument("--registry")
    parser.add_argument("--provider", choices=PROVIDERS)
    parser.add_argument("--input")
    parser.add_argument("--claims")
    args = parser.parse_args()
    try:
        if args.command == "init":
            if not args.question or not args.registry:
                parser.error("init requires --question and --registry")
            result = initialize(args.run_dir, args.question, read_json(args.registry))
        elif args.command == "record":
            if not args.provider or not args.input:
                parser.error("record requires --provider and --input")
            record(args.run_dir, args.provider, read_json(args.input))
            result = summarize(args.run_dir)
        else:
            result = summarize(args.run_dir, read_json(args.claims) if args.claims else None)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        # Report incompleteness explicitly in both machine-readable fields and exit status.
        if args.command == "report" and not result["consensus_complete"]:
            raise SystemExit(2)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(1, f"research-state: {exc}\n")


if __name__ == "__main__":
    main()
