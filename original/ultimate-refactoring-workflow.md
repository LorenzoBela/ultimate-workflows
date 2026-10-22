---
name: ultimate-refactoring-workflow
description: >
  Workflow for refactoring, debt eradication, Strangler Fig migrations,
  Mikado dependency graphs, Characterization / Golden Master safety harnesses, and AST code simplification.
  Triggers on "ultimate refactoring workflow", "/ultimate-refactoring-workflow", or when
  refactoring or restructuring code.
argument-hint: "[target-component | refactor-goal | --strangler | --mikado | --golden-master]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate Refactoring and Modernization Workflow

## Inputs and behavioral boundary

Define pain/goal, interfaces, observable behavior, baseline tests/performance, dynamic/plugin consumers and compatibility. Preserve behavior unless user authorizes a change; separate known-bug fixes from structure. Inspect dirty/staged/untracked baseline and preserve unrelated work.

Scale method to risk: local rename needs caller checks; subsystem replacement may need characterization, dependency plan and incremental routing. Do not require Strangler Fig or large snapshots for every refactor.

## Safety harness and impact evidence

Capture representative legacy inputs/outputs before editing, including failures/boundaries/effects. Freeze expected fixtures with provenance and redact production data. Normalize only documented nondeterminism; don't conceal meaningful differences. Identify preserved bugs and authorized behavior changes explicitly.

Combine characterization/differential checks with targeted assertions; snapshots can preserve irrelevant/incorrect behavior. Establish passing baseline and prove detection of a relevant injected regression in an isolated fixture where feasible. Expectations recomputed from already-modified legacy code are not frozen golden baselines.

Trace callers, exports, dynamic imports, entrypoints, config, reflection and external clients. Graph metadata can aid analysis but stale/incomplete graphs are not deletion proof. Corroborate source/runtime evidence before removing flags/helpers/public APIs; uncertain reachability stays uncertain.

## Incremental experiments and scoped rollback

Use a small dependency/Mikado plan when prerequisites matter. Change one isolated part; if it fails, record prerequisite and restore only this task's experiment. `git revert` undoes commits, not arbitrary uncommitted edits. Use isolated worktree/branch or recorded patch with verified ownership; never blanket-reset user work.

Solve prerequisites in reviewable increments and rerun behavior checks after meaningful steps. Complexity/nesting metrics are diagnostics, not universal limits. Prefer simpler interfaces with less incidental coupling; measure sensitive paths before speed claims.

## Strangler migration when justified

Introduce compatible adapter/router and new implementation alongside legacy. Shadow compare only side-effect-safe work or sandboxed/captured effects; never double-charge/send by replaying production writes to both systems.

Define routing identity, sufficient sample/observation gates, expected differences, error/latency limits and tested kill switch. Keep mixed revisions/schema/state compatible with expand-contract and resumable backfill. Account for in-flight work, sessions and external effects when routing back. Percent ramps alone do not prove safety.

Delete legacy paths after equivalence/usage evidence, client compatibility window and recovery gate. Check flag consumers, operational usage and retained data before declaring dead. Preserve rollback artifacts/config for agreed window.

## Validation, recovery and evidence

Run frozen corpus, targeted contracts, failures/cancellation and relevant performance checks. Cover dynamic entrypoints/old clients. Verify unrelated edits survive failed experiments. Test mixed versions, resumed backfill and route rollback without duplicate effects/data loss.

Return structure changes, equivalence evidence, authorized differences, actual commands/results and unverified consumers. Compilation alone is not zero regressions. Don't migrate design tokens/framework or reformat unrelated files without need.
