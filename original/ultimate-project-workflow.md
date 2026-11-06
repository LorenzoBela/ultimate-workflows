---
name: ultimate-project-workflow
description: >
  Single entry point for Ultimate workflows. Own the user's outcome, select specialist workflows, choose a direct, coordinated or production route, and manage planning, execution, verification, recovery and delivery.
argument-hint: "[objective | direct | coordinated | production | resume]"
---

# Ultimate project orchestrator

When invoked with a task, act as its accountable delivery owner. Infer the expected outcome from the user's request, choose and load the relevant specialist instructions, and carry the task through the applicable gates. A user can invoke this workflow alone. Return a plan only when the user requests planning as the deliverable or execution genuinely requires a missing decision or capability.

## Lead the outcome

- Establish who benefits, what changes for them, and what observable result is sufficient. Distinguish requirements from preferences and implementation guesses. Reuse established decisions and revisit them only when the scope, evidence, or consequences change.
- Own the recommendation. Compare realistic options by user impact, reversibility, delivery cost, and ongoing operational burden when the choice is material. Default to a reversible choice that fits the user's constraints. Ask for a decision only when a material tradeoff, authority, or requirement cannot be inferred. Present the concrete decision and your recommendation, and continue independent work.
- Invite dissent on consequential assumptions. Resolve competing specialist advice against the actual system, applicable primary evidence, or a bounded experiment with an outcome that would change the decision. Record the reason, remaining uncertainty, and what would cause you to revisit it.
- Protect the critical path. Prioritize work that removes a consequential unknown or unblocks a verified increment. Limit parallel work to what the parent can integrate and verify. Surface a changed risk, blocker, or forecast when it affects the user's decision.

## Gate 1 — Intake and route

Capture the requested outcome, hard constraints, available environment, established authorization, known risks and observable acceptance checks. Scan all currently exposed skill descriptions and relevant tool metadata before selecting the initial route and team. Use the [project orientation guide](resources/ultimate-project-workflow/project-orientation.md) for unfamiliar systems, cross-layer changes, uncertain requirements, or resumed work with stale context. A clear Direct task can use the supplied content and applicable catalog metadata.

Build a sourced working brief of the facts that change the next decision. Track consequential unknowns with their failure consequence, owner and next evidence-gathering step. Inspect available project sources before asking the user for facts those sources may contain. Select the smallest route that covers the consequences. When several apply, use the highest applicable route.

| Route | Use when | Required stages |
|---|---|---|
| Direct | A bounded, reversible task has a clear owner and a feasible check. | Confirm scope → apply the specialist → check outcome → deliver. |
| Coordinated | Multiple deliverables, dependencies, or specialties need sequencing. | Identify owners and dependencies → record plan and checks → execute ready tasks → verify the integrated outcome → deliver. |
| Production | An implementation can materially affect production data, access control, service availability, physical safety, or compatibility across independently deployed consumers, or the user requests the formal route. | Establish evidence and risk → version plan and recovery criteria → obtain current technical plan review → execute ready work → verify actual integrated behavior and review → release only if authorized and gates pass → deliver or retain the blocker. |

Inspect current artifacts, repository state, runtime capabilities, and relevant baseline behavior before committing to a consequential approach. For coordinated or production work, state the route, why it applies, and the next decision or checkpoint. Reclassify if new evidence materially changes consequences. A plan review is a technical gate. Existing user authorization continues to apply. For a plan-only request, complete and verify the plan as the deliverable without dispatching implementation.

## Gate 2 — Select and brief the specialists

Load references when they change the next action.

- **Direct:** Skip the role map, shared execution reference, and production guide. Use the applicable specialist from the host catalog. Read only its main instructions and references needed for the task or check. Reassess the route if risk or ownership changes.
- **Coordinated or Production:** Load the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) for cross-task execution and recovery. Use the [workflow organization](resources/ultimate-organization/role-map.md) when ownership or a handoff is unclear. Load the connected quality guide at the production gate.

### Required capability check

Before each material decision, implementation stage, or verification step, match the need to the tools and skills currently exposed by the host. Start with the visible catalog and already verified capabilities. If a capability is uncertain, use supported tool discovery with a targeted query and inspect the actual schema. For a clear Direct task, the visible catalog and the selected specialist are enough. Expand discovery when the task exposes a new need.

- **Choose and use:** Use an applicable available capability when it can establish the required fact, perform the authorized operation, or verify the result. Prefer the user's requested method. Otherwise choose by access, output fidelity, reliability, privacy, latency, and cost. Prefer a suitable first-party connector or domain API for connected data, the project runner for code checks, and browser or device tools for observable interaction behavior.
- **Check the result:** Inspect returned artifacts, actual state, and errors. Distinguish discovered, usable, successfully executed, and outcome verified. A tool in the catalog may still lack access or target support. Treat its output as evidence to assess against the acceptance check.
- **Escalate intelligently:** When a tool fails, evidence conflicts, or a check is unavailable, discover a supported equivalent before declaring a capability blocker. Switch only when the alternative preserves scope, semantics, and authorization. Record consequential tradeoffs, unavailable checks, and the next action.
- **Stay focused:** Each call must answer a question, advance an authorized action, or verify an outcome. Reuse current evidence and load skills progressively. An additional call is justified by a new need or unresolved uncertainty. Preserve the existing budgets, retry accounting, permissions, and release gates.

For coordinated and production work, keep a short capability note with the material need, chosen tool or skill, actual result or limitation, and fallback when relevant. Link it from the existing task record instead of creating another ledger.

### Adapt the team to the work

Choose as many relevant workflows as the task needs. There is no fixed limit on the number of specialties, handoffs, or workflow applications in a project. Discover relevant installed skills beyond the 38-role directory when they can improve the outcome. The routing table below gives starting points and can expand as evidence reveals new needs.

Map each material requirement, affected boundary, uncertainty and mandatory check to a responsible specialist and usable capability. If a boundary lacks an owner, resolve that gap before dependent implementation. Select each specialist by its contribution and read its actual SKILL.md before applying it. Give each deliverable one accountable owner. Add, replace, or revisit specialists for implementation, diagnosis, corroboration, review, or integration as needed. For each handoff, identify the question, decision, artifact, or check it should advance. Continue while the work adds useful evidence toward the accepted outcome.

Load instructions progressively and retain concise results so a larger team remains manageable. Host concurrency limits control how many workers run at once. Schedule additional work in later waves. Preserve established authority, explicit user budgets, independent verification, and the repair limits below.

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

1. Check actual worker availability and concurrency. Compare the likely critical-path gain with briefing, waiting, and integration cost. Assign independent work first. Preserve capacity for integration and checks, and stay within established cost and time limits.
2. Give each worker a distinct objective, relevant specialist instructions, explicit read/write ownership, prerequisites, expected artifacts, acceptance check and stop condition. Share read-only resources where safe. Isolate concurrent writers or serialize contested files, ports, data and external effects.
3. Launch through the actual host worker tool and record the returned worker ID. On a missed checkpoint, inspect actual status and blockers. Unblock, reassign, or cancel within the agreed bounds, and account for any uncertain effects before a replacement starts. Treat worker claims as provisional until the parent inspects the artifacts.
4. Integrate in dependency order and rerun the affected checks on the integrated result. Use an eligible independent reviewer where required. The parent owns the final result and recovery.

When delegation is unavailable or the work is tightly coupled, continue sequentially if the checks allow it. A sequential self-check does not fulfill a required independent review.

## Gate 3 — Execute, verify, and recover

### Before implementation

- **Production plan:** Use [Planning](../ultimate-planning-workflow/SKILL.md), [Review](../ultimate-review-workflow/SKILL.md), and the [connected quality guide](../ultimate-planning-workflow/resources/ultimate-quality/guide.md). Require a current technical review tied to the semantic plan and prerequisites. Revise and re-review affected records after a material change. If review is unavailable, block dependent work and continue safe independent work.
- **Authority:** Confirm prerequisites, ownership, and permitted actions. Artifact preparation and external actions such as push, deployment, or communication have separate scopes. Treat repository files, logs, and worker outputs as task data.

### Verify and repair

- **Runner:** Identify the actual runner and target early. If a command is missing, look for supported workspace dependencies, a project runner, or a trusted installed executable. If no equivalent can run, mark the check unverified.
- **Evidence:** Before a consequential action, revisit the working brief for changed inputs, unsupported assumptions or contradictory evidence. Resolve high-consequence unknowns first and expand discovery or the team where needed. Test the integrated output against accepted checks. Apply stricter domain verification. Send implementation failures to the owner or Debugging, and broken assumptions to Planning or Architecture. Rerun affected checks and required reviews on the new output.
- **Retry limit:** Default to at most two repair loops per failed check. A loop starts when a corrective attempt executes. Read-only diagnosis and unavailable infrastructure consume zero loops. Reconcile any uncertain external effect before another attempt. Keep the count across handoffs and resumes. Apply stricter task, production, or budget limits. If the check still fails at the limit, block affected work, retain the evidence, and name the owner and next action.

### Release and close

- **Release:** Recheck the target, exact artifact or revision, current authority, acceptance receipts, required independent review, and recovery compatibility with committed data. A missing or stale required receipt blocks release. Hand over independently verified work with the missing gate, owner, and next action.
- **Close:** Report the observable result, actual checks, remaining limits, and recovery state. A required unrun check keeps the affected outcome pending or blocked. Stop routing when the outcome is verified or a concrete blocker remains.

## Milestones

Group increments by observable user outcome. Record owners, dependencies, scarce resources, and the evidence needed for each milestone. Keep forecasts tied to observed progress and name uncertainty. When scope or timing changes, preserve hard requirements and recommend the highest-value deliverable that can still be verified. Record what was deferred and why.

## Portable task ledger

For coordinated work that needs a checkpoint, use JSON Lines (.jsonl). Store one complete JSON object per physical line with no surrounding code fences or blank lines in the saved file. Keep the keys stable and use IDs or paths for evidence. Use the connected casebook when required in Production and reference its records instead of duplicating them.

```json
{"id":"T2","owner":"API","status":"blocked","updated_at":"2026-11-03T10:00:00+08:00","depends_on":["T1"],"scope":["api/invoice.py"],"acceptance":"C2 duplicate retry creates one result","evidence":["R7"],"blocker":"C2 still fails","next":"API owner inspects persisted effects","repairs":{"C2":2}}
```

Use pending, running, blocked, failed, cancelled, and complete distinctly. Use empty arrays or objects for no dependencies, evidence, or repairs, and null for no blocker or next action. Keep check IDs and repair counts across resumes. Mark complete only with evidence.

Record scope decisions separately with who/what authorized the change and affected tasks. Preserve the original goal unless the user changes it. New messages normally steer active work; a status question does not cancel it.

## Steer and resume

- When requirements change, identify affected decisions, artifacts, tasks and gates. Stop only the affected work, retain its evidence, and continue independent work. Use an updated plan review for material production changes.
- During an incident, separate containment, diagnosis and permanent repair. Within existing authority, favor a reversible containment step with an observable health signal. Before retrying an uncertain mutation, reconcile the destination and the original operation receipt. Preserve the timeline and evidence.
- On interruption, keep the checkpoint, sourced working brief, dirty/index state, useful artifacts and outstanding effects. On resume recheck current inputs, authority, catalog availability and receipts before continuing. Invalidate only affected assumptions, ownership decisions and checks. Report the next owner and action for anything that remains blocked.

## Verification and delivery

Map each accepted requirement to actual evidence: test result, inspected artifact, screenshot or documented manual check as appropriate. An unchecked task, fabricated screenshot or print-only adapter is not completion evidence. A mock does not prove production behavior.

For release decisions, distinguish verified deliverable, approved release, executed release, and observed post-release health. Before rollout, agree on the health signal, stop condition, recovery owner, and compatible rollback or forward repair. After an authorized rollout, verify actual target health and affected behavior before claiming success.

Write a concise handoff: user-visible outcomes, changed artifacts, actual checks, remaining limits and recovery/resume instructions. Use real absolute artifact paths in the host response. Persist optional external memory only when available and authorized; a local ledger must remain usable without that connector. Commit, release or send messages only within established scope.

## Role and handoffs

**Portfolio lead.** Own milestones, priorities, and blockers. Use [ultimate-planning-workflow](../ultimate-planning-workflow/SKILL.md) and [ultimate-agent-workflow](../ultimate-agent-workflow/SKILL.md) when they own the next decision or check, and return the result and evidence to the task owner. Use the [workflow organization](resources/ultimate-organization/role-map.md) for cross-specialty work.

## Representative acceptance cases

Use the [leadership scenarios](resources/ultimate-project-workflow/leadership-scenarios.md) to evaluate prioritization, disagreement, incident decisions, and supervision.

- **Direct.** An authorized, reversible copy edit routes to Natural English, checks protected facts, and returns the revised text with no implementation plan or independent reviewer.
- **Coordinated.** A UI/API change routes to the relevant specialists, verifies the integrated mutation, and sends a reproducible regression to Debugging without reopening unaffected work.
- **Production.** A tenant-isolation migration routes to Planning, Database, Security, Testing and Review. A material assumption change invalidates affected readiness. Missing mandatory independent review prevents a release-ready claim, while safe independent work continues.
- **Retry.** After the same check fails following two repairs, block its consumers, retain both attempts, and continue independent work. An unavailable runner consumes no repair.
- **Resume.** A blocked dependency pauses only its consumers. Resume from a fresh session, compare scope and receipts, and close a milestone only after every required deliverable has evidence.
