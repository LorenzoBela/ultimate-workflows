---
name: ultimate-project-workflow
description: >
  Manage a requested project from accepted requirements through milestones, durable task states, blockers and verified deliverables. Use for multi-step project coordination and resumable progress tracking.
argument-hint: "[scope | milestones | progress | delivery]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Project execution and milestone tracking

Use for a requested multi-step project through verified deliverables. Use the host's task state or a repository-local ledger rather than assuming a particular IDE's appDataDir. Do not turn a single routine fix into a sprint process.

## Inputs and scope

Capture objective, users, constraints, accepted requirements, non-goals, authorization, current repository state, dependencies and acceptance criteria. Clarify only missing information that materially blocks decisions; continue independent work. Existing authorization persists and does not authorize unrelated releases or external communication.

## Milestones

Group useful increments with an observable user outcome. Apply Must/Should/Could/Won't prioritization when helpful; record why scope is deferred. Identify critical dependencies, owners, external inputs, available resources and risks. Estimates are estimates. Prefer coherent tasks to mandatory 2–10 minute subdivisions.

## Portable task ledger

For each task retain stable ID, owner, status, dependencies, owned paths/resources, acceptance criterion, evidence reference, blocker/next action and updated timestamp. Use `pending`, `running`, `blocked`, `failed`, `cancelled`, `complete` distinctly; do not mark a blocked task complete to clear the checklist.

Record scope decisions separately with who/what authorized the change and affected tasks. Preserve the original goal unless the user changes it. New messages normally steer active work; a status question does not cancel it.

## Execution and recovery

- Run ready work within actual host capabilities. Delegate only when authorized and keep writer ownership explicit.
- Update the ledger at meaningful transitions. Batch checks suited to changed behavior; repeating the entire suite after every wording edit is unnecessary.
- Capture failures with reproducible context and actual output. Distinguish baseline failure, new regression, unavailable dependency and flaky result.
- When interrupted, preserve checkpoint, dirty/index state, useful artifacts and uncertain side effects. On resume verify scope/revision/resources, reconcile outstanding actions and continue unfinished work.
- Replan affected downstream tasks when a dependency fails. Keep a concrete blocker and next action; do not endlessly retry unavailable services.

## Verification and delivery

Map each accepted requirement to actual evidence: test result, inspected artifact, screenshot or documented manual check as appropriate. An unchecked task, fabricated screenshot or print-only adapter is not completion evidence. A mock does not prove production behavior.

Write a concise walkthrough only when it helps the handoff: user-visible outcomes, changed artifacts, actual checks, remaining limits and recovery/resume instructions. Use real absolute artifact paths in the host response. Persist optional external memory only when available and authorized; a local ledger must remain usable without that connector. Commit, release or send messages only within established scope.
