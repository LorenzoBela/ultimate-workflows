# Verification status — v4 connected quality routine

Recorded October 23, 2026. Baseline: `9d8e606f7898e310e722ff31b63b182281eee573`.
Five workflow entry points changed: research, planning, multi-agent invoker,
debugging and review. The remaining 33 instructions retain their v3 content.

## Implemented scope

- Explicit plan/code review modes and version-bound readiness/finding gates.
- Shared local casebook with generation checks, atomic updates, revision links,
  actual subprocess receipts and independent repair closure.
- Additive research question coverage and decision readiness; old checkpoints
  remain readable and do not silently acquire the new readiness status.
- Shared resources packaged into the five selected bundles, including all nested
  guide dependencies. All 38 bundles retain source/export provenance hashes.
- Seventy simulated evaluation fixtures, fixed oracles and separate semantic
  rubrics, with 58 development and 12 held-out cases; external result consumer.

## Verification evidence

The local suite exercises actual disposable Git repositories, failing and passing
commands, stale evidence, repair/independent closure, provider-ledger fixtures,
evaluation calibration and guarded packaging/install/update behavior. A connected
test reproduces a real local counting defect, records its failure, applies a fix,
verifies independent closure and rejects completion after a later code change.
This local program is not a live agent/provider benchmark.

Final frozen-source `npm test`: **87 passed, 2 skipped** (18 Node tests and 71
Python cases, including the two skips). Both skips require symlink creation,
which this Windows session does not permit; configured Linux CI is not a hosted
execution receipt. The 38-bundle build and validation passed, including nested
resource membership and source/export SHA-256 parity. Build preflight also rejects
CRLF sources that Git would normalize into different committed hashes; staged Git
blobs were independently checked against every published bundle hash. A credential-pattern scan
found no matching files; this is a limited pattern check, not a security audit.

Guarded Gemini/Codex synchronization applied 40 owned file updates after a clean
dry run, then 10 helper copies received canonical LF bytes. All 38 installed
bundles on each host match the final published manifest (91 files per host);
baseline files outside the declared bundle ownership remain unchanged. Private
pre-update snapshots and local raw test/installation receipts were retained.
An independent final consistency review found no new material defects within
the changed workflow/helper/guide/packaging scope.

The default v4 evaluator validated 70 fixtures and returned `pending` (exit 2),
with no behavioral results or comparison pairs. Evaluator calibration is tested
separately and cannot establish measured workflow improvement.
The previous v3 evidence remains in [verification.md](verification.md).

## Pending measurements and limits

No actual 70-case baseline/candidate host benchmark has been run. No live research
run with all 15 configured providers is claimed. Three repetitions per case/host,
original host transcripts and independent semantic grading remain required before
reporting comparative quality gains. The default evaluator reports pending.

Held-out fixture files are public; they are regression holdouts rather than a
secret capability test. Keep them out of workflow tuning and disclose exposure.
Synthetic receipts cannot establish live provider coverage. Content hashes bind
artifacts; they do not authenticate actor identity or prove semantic truth.

The casebook is a local evidence helper, not a sandbox, scheduler, authorization
service or full agent runtime. Reviewers must still assess source relevance,
assertion adequacy, independence and actual permissions. Hosted CI, production
services, target devices and the older broad 152-scenario benchmark retain the
unrun limitations documented for v3.
