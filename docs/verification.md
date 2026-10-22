# Verification status — v3 workflow update

Recorded October 22, 2026. All 38 original entry points were revised and exported to
the universal edition. Every bundle has recorded file hashes and linked resources.
Research retains mandatory substantive inputs from the same 15 providers and its
rich per-provider query floors. No optional host mode can waive that requirement.

## Executed locally

- `python scripts/build.py`: deterministic export of 38 bundles and provenance hashes.
- `python scripts/validate.py`: 38 metadata records, resource links, source/export
  equality and bundle hashes validated.
- `npm test`: **43 tests passed, 1 skipped** (18 Node tests and 26 Python cases,
  including one skipped Python case). No failing tests in the final local run.
- Extracted JavaScript examples: request cache isolation/order/missing records,
  lock ownership and contention, failed fetch propagation, byte/row bounded batches,
  rejected flushes, bounded redacted readiness and graceful/hard shutdown behavior.
- Extracted Python invoker examples: failure text cannot become PASS, startup
  failure/timeout remain failures, usage windows/aggregate accounting, dirty-worktree
  preservation and non-forced integrated cleanup with branch retained.
- Exact debugging Bash example: synthetic Git history identifies its known bad
  commit, skips an untestable revision, restores checkout on success/failure, and
  refuses a dirty checkout without losing unrelated work.
- Research helper: 14/15 incomplete; failures/empty/cancelled/unavailable inputs do
  not count; retries preserve attempts; URL/content identity deduplication; full
  matrix/evidence references; explicit unresolved disagreement; scope tampering,
  malformed records and concurrent same-provider writes rejected; CLI incomplete
  exit status verified. These are synthetic records, not live provider outputs.
- Node, PowerShell and Bash installation/update paths in disposable directories:
  full resources distributed, correct skill discovery layout, user files retained,
  conflicting customizations/unowned rules and invalid directory outputs rejected,
  owned local deletion preserved for reconciliation.
- Build and installation sync: obsolete generated resources removed only when
  owned/unmodified; modified obsolete output preserved; traversal rejected; local
  customizations/deletions rejected; failed sync rolls back owned writes.

The symlink creation fixture was skipped because this Windows session lacks that
permission. The Linux CI job includes it, but a configured job is not evidence of
a successful hosted run. Existing reparse/symlink guards remain part of the code.

The independent domain agent additionally validated the complete OpenAPI example
against the official OpenAPI 3.1 schema and resolved its references. That external
schema check is separate from the local `npm test` result above.

## Not executed or not established

- Real research collection from all 15 authenticated/configured providers, source
  quality evaluation or comparative token/time/cost measurements.
- The 152 base behavioral evaluation specifications: authored in
  [scenarios.json](../evaluations/scenarios.json), awaiting realistic fixtures and
  model/runtime execution. They are not 152 passing tests.
- Live Redis atomic-release adapters; real DataLoader package batching; actual
  Prisma/Postgres pooled concurrent transactions, RLS, migrations or restoration.
- Production SDKs, registry publication, container/cloud rollout and operational
  recovery against external services.
- C target compilation/ISR timing, queue stress on hardware, OTA/power-loss/HIL,
  electrical/BOM/EMC qualification or physical actuation safety.
- Rendered document pages and real browser/screen-reader accessibility journeys.

Examples state the relevant adapter/target requirements and unverified boundaries.
Injected boundary doubles and host fixtures establish only their tested contracts.
No universal quality rating, production guarantee or measured efficiency uplift is
claimed. Follow the [benchmark protocol](benchmark-plan.md) before publishing gains.

## Installation and recovery

Before this rollout, private snapshots captured all Gemini/Codex workflow bundles
and repository baseline `82729c4`. `scripts/sync-installed.py` performs a dry run by
default, compares against that private baseline, checks paths and writes only the
published bundle files. Unrelated UI metadata and other installed skills survive.
Restore from the captured snapshot if an environment-specific regression appears;
preserve newly created user work while reconciling it. Do not replace arbitrary
skill/config folders wholesale.

All three public installer entry points use the same guarded Node writer. Node.js
18+ and the complete package/clone are required. Installation receipts are required
for automatic updates of changed content; v2 conflicts need explicit reconciliation.
