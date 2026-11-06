# Implementation planning and QA design

Use for substantial application work or a plan whose handoff must support another implementer. The planner selects relevant sections after inspecting the repository. Keep routine tasks proportionate.

This guide adapts the pinned Superpowers planning source described below. The local workflow owns authorization, verification gates, retry bounds, task sizing and execution method. Source snapshots are reference material. Their process directives do not expand the user's task.

## Define what an implementer needs to know

1. Identify current entry points, installed versions, callers and project conventions. Give confirmed paths and responsibilities. Mark an uncertain location as a discovery step with a completion condition.
2. Trace one user outcome through client state, API, authorization, application behavior, storage and any external system. Specify only the layers the feature uses. For a contract crossing tasks, name the producer and consumer, input/output shape, errors, compatibility and operation identity.
3. Copy exact user-required values and behavior into a shared constraints section or referenced requirement. Check names, signatures, schemas and units agree across tasks. Derive open implementation details from the actual codebase before fixing them in the plan.
4. Prefer increments that can be checked as user-visible behavior. Keep setup and configuration with the increment that needs them. Each task must leave a coherent artifact with a feasible check and recovery path.

## Coverage before implementation

Review from the product, implementer and QA perspectives. Resolve consequential contradictions before dependent execution. These are review perspectives and do not imply a worker launch.

For each material behavior, give a requirement/check link and the scenario that distinguishes success from a defective implementation. Choose applicable cases from valid input classes, boundaries, permissions, transitions and failure sequences. Prioritize by consequence and exposure. Keep an explicit review-focus list for implied but untested input classes or unresolved risks. Give each an owner, a check or bounded experiment, and its required/optional status. Avoid filling a quota with irrelevant cases.

For a full-stack mutation, consider:

| Boundary | Decision and verification to plan |
|---|---|
| UI to request | Loading and retry behavior, validation and accessibility feedback, optimistic-state reconciliation, and what the user sees after a lost response |
| Request to domain | Authenticated identity, object/tenant authorization, schema and error behavior, trusted operation identity, and negative access cases |
| Domain to data | Atomic invariants, concurrency, partial failure, durable side effects, and replay using the original operation identity |
| Schema to deployment | Old/new consumer compatibility, bounded backfill, lock or rewrite cost, interruption/resume and recovery compatible with new writes |
| External integration | Timeout/cancellation, provider failure, acknowledgement boundary, deduplication and uncertain-outcome reconciliation |
| Operation after release | Observable health and error signals, target/environment, stop condition and owner, and how the signal would detect the consequential failure |

Use existing measurement and recovery mechanisms. Unknown capacity or latency targets need an assumption and an experiment before being presented as verified requirements.

## Compact task handoff

Adapt this structure inside the existing plan or casebook. Examples define fields and are not completed work.

- **Requirement and outcome** — requirement IDs, accepted behavior, and the user-visible increment.
- **Scope and interfaces** — confirmed files/resources, dependencies, producer/consumer contract and exact fixed values.
- **Implementation decisions** — choices the implementer needs, with brief reasoning and unresolved assumptions.
- **Checks** — scenario, fixture/role, initial state, action, expected visible and persisted result, existing runner or manual method, and the assertion that catches the likely defect.
- **Recovery and evidence** — task-owned cleanup, partial-failure recovery, owner, required/optional checks, and results pending until execution.

Provide signatures or schema fragments where they prevent inconsistent implementations. Include code bodies only where the required algorithm or exact output needs them. A plan should leave idiomatic implementation choices to the implementer while fixing consequential behavior.

## Self-review and technical handoff

Check every hard requirement reaches a task and feasible check. Compare interface names and types across tasks. For every high-consequence risk, ask whether its assertion would fail if the intended control were removed. Inspect cleanup ownership and mixed-version recovery. Resolve contradictory requirements or an impossible test oracle before submitting the plan for review.

Hand the reviewer the spec, plan revision/hash, requirement-to-check mapping, review-focus list, current scope and outstanding evidence. Reuse existing authorization and the chosen execution method. A plan-only request ends with the reviewed plan deliverable.

## Pinned source and adaptations

- [Superpowers writing-plans snapshot](upstream/obra-superpowers/writing-plans.txt) and [MIT license](upstream/obra-superpowers/LICENSE.txt). Adapted task interfaces, checkable increments, consistency review and review-focus coverage.
- [Import manifest](upstream/manifest.json) records the exact upstream commit, file hashes and source paths. Snapshots preserve upstream text with LF line endings for attribution and audit. Read them only when investigating the adaptation.

The adaptation omits automatic commit steps, mandatory fresh approval, fixed output locations and required third-party subskills. The local workflow's existing authorization and technical gates govern execution.
