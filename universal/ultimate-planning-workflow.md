---
name: ultimate-planning-workflow
description: >
  Create technical specifications, implementation plans, dependency maps and recovery strategies proportional to risk. Use for substantial planning or migrations; preserve mandatory 15-engine coverage whenever research is invoked.
argument-hint: "[feature | migration | refactor | design-doc]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Technical planning and implementation specifications

This is the planning stage of **Research → Plan → Plan Review → Invoke → Debug when needed → Final Code Review**. Apply the [connected quality guide](resources/ultimate-quality/guide.md). Planning produces a versioned proposal; `ultimate-review-workflow` in **plan** mode evaluates technical readiness before the invoker dispatches its dependent implementation. This is not a new human approval ceremony and does not revoke inherited implementation authorization.

## Versioned plan and evidence-linked decisions

Use one run/casebook and stable IDs. Trace **question → claim/evidence → requirement/assumption → decision/interface → task → acceptance check**. For each hard requirement name the concrete behavior, relevant evidence and at least one feasible task/check. Compare incremental/no-change and realistic alternatives where the decision is open. Source consensus without applicable decision evidence is insufficient.

For every consequential assumption record its support, uncertainty, failure consequence, owner and a discriminating experiment. Stress-test unavailable dependencies, concurrency/resource conflicts, compatibility/deploy ordering, partial failure and recovery. A test oracle must establish the required outcome—an exit-zero script or printed “verified” is not enough. Separate mandatory checks from optional exploration, and record required tools/capabilities honestly.

Compute the semantic `plan_hash` from canonical structured requirements, assumptions, decisions, interfaces, tasks and acceptance checks. A Markdown reformat does not change that fingerprint. Plan review binds to the current hash, scope and relevant evidence/input versions; changed requirements/assumptions/contracts/checks invalidate affected readiness. Expected implementation edits and accepted prerequisite outputs advance task state without invalidating an unchanged plan. Unrelated repository changes alone do not restart planning.

Submit a coherent plan for a `ready`, `needs_revision` or `blocked` verdict, using the precise P0/P1 consequences and precedence in the guide. A remediable internal gap returns here for revision and another plan review. Missing essential evidence/capability, genuine uninferable tradeoff or insufficient authority is blocked with its next action. Seek user decisions only for those real gaps; never ask again for already-established authorization.

Design-level debugger feedback reopens the linked assumptions/decisions/tasks: preserve experiments, revise the affected records and recovery/check contracts, recompute the semantic hash and renew plan review before dependent dispatch. Preserve unrelated ready work. A risk acceptance records the actual bounded tradeoff/mitigation and cannot waive a hard requirement, missing provider or unrun check.

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

Dispatch only tasks from a current technically ready plan review, with valid prerequisites, within host concurrency/resource limits. Stop dependent work when a prerequisite fails; persist the failure and replan the affected subgraph. Independent tasks may continue if safe. Builders run their own meaningful checks; independent review is additional risk-based evidence.

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
