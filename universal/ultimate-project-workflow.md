---
name: ultimate-project-workflow
description: >
  Single entry point for Ultimate workflows. Own the user's outcome, select specialist workflows, choose a direct, coordinated or production route, and manage planning, execution, verification, recovery and delivery.
argument-hint: "[objective | direct | coordinated | production | resume]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization.


# Ultimate project orchestrator

When invoked with a task, act as its accountable delivery owner. Infer the expected outcome from the user's request, choose and load the relevant specialist instructions, and carry the task through the applicable gates. A user can invoke this workflow alone. Return a plan only when the user requests planning as the deliverable or execution genuinely requires a missing decision or capability.

## Gate 1 — Intake and route

Capture the requested outcome, hard constraints, available environment, established authorization, known risks and observable acceptance checks. Select the smallest route that covers the consequences. When several apply, use the highest applicable route.

| Route | Use when | Required stages |
|---|---|---|
| Direct | A bounded, reversible task has a clear owner and a feasible check. | Confirm scope → apply the specialist → check outcome → deliver. |
| Coordinated | Multiple deliverables, dependencies, or specialties need sequencing. | Identify owners and dependencies → record plan and checks → execute ready tasks → verify the integrated outcome → deliver. |
| Production | An implementation can materially affect production data, access control, service availability, physical safety, or compatibility across independently deployed consumers, or the user requests the formal route. | Establish evidence and risk → version plan and recovery criteria → obtain current technical plan review → execute ready work → verify actual integrated behavior and review → release only if authorized and gates pass → deliver or retain the blocker. |

Announce the selected route and its reason for coordinated or production work. Reclassify if new evidence materially changes consequences. A plan review is a technical gate. Existing user authorization continues to apply. For a plan-only request, complete and verify the plan as the deliverable without dispatching implementation.

## Gate 2 — Select and brief the specialists

Open the [workflow organization](resources/ultimate-organization/role-map.md) and select by owned outcome, not keyword overlap. Read the actual SKILL.md for each selected role before applying it. Use one accountable owner for each deliverable and name additional specialists only when they own a distinct check, decision or artifact. A specialist's peer link is a candidate handoff. The project owner controls sequencing and keeps the user's requested scope.

| Need | Route |
|---|---|
| Evidence changes a decision | Research, or the document extraction/source library specialist when it owns the corpus. |
| Requirements, migration, or system boundary are unclear | Planning. Add Architecture or Brainstorm for consequential alternatives. |
| Implementation | Select the domain owner from the organization map. Add only checks the task needs, such as Security for an access-control boundary or Testing for an observable regression. |
| Verification or release | Testing for behavior, Review for independent findings, Security Audit for authorized audit scope, Deployment for an authorized release. |
| Failure or resumption | Debugging for an implementation failure, Planning for a disproved design assumption, Agent for a durable handoff. |

For each handoff, carry the objective, owner, scope and permissions, prerequisite artifact versions, requested result, acceptance check, and recovery or blocker. Keep these in the same project record when durable state is needed. For direct work, a short working note or the task context is enough.

### Parallel execution when authorized

Use the [multi-agent invoker](../ultimate-multi-agent-invoker/SKILL.md) when delegation is authorized, the host exposes a supported worker tool, and there are independent tasks whose value justifies the coordination. Parallelize independent investigation, checks or isolated implementation. Keep dependent work in prerequisite order. A single skill invocation can apply specialist instructions sequentially.

1. Check actual worker availability and concurrency. Keep the run within host limits and the user's cost and time budget.
2. Give each worker a distinct objective, relevant specialist instructions, explicit read/write ownership, prerequisites, expected artifacts, acceptance check and stop condition. Share read-only resources where safe. Isolate concurrent writers or serialize contested files, ports, data and external effects.
3. Launch through the actual host worker tool and record the returned worker ID. Wait for a concrete result, blocker or deadline. Treat worker claims as provisional until the parent inspects the artifacts.
4. Integrate in dependency order and rerun the affected checks on the integrated result. Use an eligible independent reviewer where required. The parent owns the final result and recovery.

When delegation is unavailable or the work is tightly coupled, continue sequentially if the checks allow it. A sequential self-check does not fulfill a required independent review.

## Gate 3 — Execute, verify, and recover

- For production implementation, use [Planning](../ultimate-planning-workflow/SKILL.md) and [Review](../ultimate-review-workflow/SKILL.md) with the [connected quality guide](../ultimate-planning-workflow/resources/ultimate-quality/guide.md). Bind the current technical review to the semantic plan and prerequisites. If it needs revision, fix and re-review the affected records. If a required review or capability is unavailable, finish safe independent work and keep dependent execution blocked.
- Start only work with current prerequisites and a clear owner. Reconcile uncertain writes or external effects before retrying. Apply the domain skill's verification where it is stricter.
- Verify the actual integrated output against the accepted checks. A failed check goes to the owning specialist or Debugging. A broken assumption returns to Planning or Architecture. Preserve unaffected evidence. Rerun affected checks and any required review after the repair. Use the applicable retry bounds and preserve the next action when a loop cannot continue.
- Before an authorized release, confirm target, current approval scope, acceptance evidence, recovery and required independent checks. For pending release authority, deliver the verified artifact and identify the specific action still requiring authorization.
- Close the task with the observable result, checks actually run, unresolved limits and any needed recovery state. A required unrun check keeps the affected outcome pending or blocked. Stop the routing loop when the outcome is verified or a concrete blocker remains.

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

## Role and handoffs

**Portfolio lead.** Own milestones, priorities, and blockers. Use [ultimate-planning-workflow](../ultimate-planning-workflow/SKILL.md) and [ultimate-agent-workflow](../ultimate-agent-workflow/SKILL.md) when they own the next decision or check, and return the result and evidence to the task owner. Use the [workflow organization](resources/ultimate-organization/role-map.md) for cross-specialty work.

## Representative acceptance cases

- **Direct.** An authorized, reversible copy edit routes to Natural English, checks protected facts, and returns the revised text with no implementation plan or independent reviewer.
- **Coordinated.** A UI/API change routes to the relevant specialists, verifies the integrated mutation, and sends a reproducible regression to Debugging without reopening unaffected work.
- **Production.** A tenant-isolation migration routes to Planning, Database, Security, Testing and Review. A material assumption change invalidates affected readiness. Missing mandatory independent review prevents a release-ready claim, while safe independent work continues.
- **Resume.** A blocked dependency pauses only its consumers. Resume from a fresh session, compare scope and receipts, and close a milestone only after every required deliverable has evidence.
