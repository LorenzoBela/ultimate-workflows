---
name: ultimate-planning-workflow
description: >
  Create technical specifications, implementation plans, dependency maps and recovery strategies proportional to risk. Use for substantial planning or migrations; preserve mandatory 15-engine coverage whenever research is invoked.
argument-hint: "[feature | migration | refactor | design-doc]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Technical planning and implementation specifications

Use for substantial feature plans, migrations and risky changes. Match planning depth to consequences, uncertainty and reversibility, rather than file count. Preserve existing authorization; do not require a second approval just because a plan artifact exists. The mandatory research contract below is unchanged by planning depth.

## Inputs and evidence

Read the actual implementation, manifests, tests and relevant requirements. Record goal, non-goals, current behavior, proposed behavior, constraints, assumptions, affected users/data, repository state and acceptance criteria. Unknowns remain explicit. For technical research invoked by this plan, use `ultimate-research-workflow`: all 15 substantive provider inputs and rich per-engine context remain mandatory. Missing providers mean incomplete research, never a reduced-engine substitute.

Choose an artifact suited to the decision: concise task checklist, feature specification, design doc, RFC for cross-team consensus, or ADR for a durable architectural choice. Avoid creating all of them by default.

## 1. Requirements and alternatives

Write observable behavior including failures, permissions and compatibility. EARS-style forms help when applicable:

- When a trigger occurs, the system performs an observable response.
- While a precondition holds, the system maintains an invariant.
- If a failure occurs, the system provides a defined recovery or error outcome.

Separate hard constraints from preferences. Compare the existing/incremental approach and realistic alternatives; identify evidence confidence and tradeoffs. Use decision weights only when useful, label estimates and test whether plausible weight changes alter the result. No invented customer quotes or measured performance.

## 2. Design and contracts

Identify boundaries, interfaces, state transitions, authorization checks, failure modes and data ownership. Define shared schemas before independent consumers where they prevent incompatible parallel work. Keep architecture diagrams at useful C4 levels; a small change does not need all levels. Use actual platform constraints, not unrelated aerospace/mobile budgets.

For external operations specify timeout, retry classes, idempotency, cancellation and uncertain-result reconciliation. For auth/data changes specify tenant/object access invariants and evidence. Include realistic capacity/latency budgets based on target workload, available measurements and tolerable failure behavior.

## 3. Task graph

Each task records:

| Field | Required content |
|---|---|
| ID, owner, dependencies | Stable identifier; prerequisite and shared-resource boundaries |
| Scope | Owned files/resources, base revision and intended behavior |
| Action | Small coherent deliverable; do not invent a fixed minute duration |
| Acceptance | Concrete state/output invariant and appropriate check command or inspection |
| Recovery | How to preserve user work and recover data/config; limitations |
| Evidence | Actual result/artifact after execution, initially pending |

Run only ready tasks within host concurrency/resource limits. Stop dependent work when a prerequisite fails; persist the failure and replan the affected subgraph. Independent tasks may continue if safe. Builders run their own meaningful checks; independent review is additional risk-based evidence.

## 4. Brownfield experiments and recovery

For tightly coupled refactors, use a disposable isolated checkout based on a recorded revision. Make an experiment, run characterization checks, record discovered prerequisites, then remove only the owned clean experiment. Never suggest `git reset --hard` or path checkout on the user's working tree as routine recovery. Preserve dirty/untracked/index state. Keep useful experiment evidence until findings are captured.

A recovery command must be valid for the real environment. `prisma migrate resolve --rolled-back` adjusts migration history; it does not undo applied SQL. Design and rehearse compensating SQL, restoration or forward repair where needed.

For compatible schema evolution:

1. Expand with backward-compatible fields/indexes and validate deploy ordering.
2. Backfill with checkpoints and reconciliation; dual-write only with defined conflict/consistency behavior.
3. Switch reads under a controlled gate and verify old/new consumers.
4. Contract only after all consumers, retained data and rollback windows are verified. Do not use a universal seven-day timer as proof of safety.

## 5. Risk, rollout and completion

Record credible risks with likelihood/impact confidence, owner, mitigation and observable trigger. High-consequence failures require mitigation even when a multiplied risk score is small. Select staging, feature flag, canary and recovery strategy based on the actual system; avoid mandatory infrastructure purchases or fixed rollout percentages.

Final plan includes acceptance evidence to collect, dependencies/unresolved decisions, rollout/recovery procedure and task status. Distinguish proposed checks from actual passes. Update the plan when scope changes and preserve decisions already accepted by the user.
