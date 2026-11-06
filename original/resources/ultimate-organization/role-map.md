# Ultimate workflow organization

The user owns the objective, constraints and authority. The current task owner is accountable for completion. Use Project as the delivery lead for work spanning multiple specialties. Agent coordinates execution and handoffs. The invoker handles staffing only when delegation is authorized and supported. Use existing budget and usage records for cost control and Review for independent assurance when needed. A role describes responsibility and does not launch an agent or grant permissions.

## Delivery and feedback

1. **Intake and scope.** For a bounded task, start directly with the relevant specialist. Use Project for multiple deliverables, dependencies or a durable milestone. Use Research when a decision needs external evidence.
2. **Plan and execute.** Use Planning and Architecture when choices, contracts or rollout need coordination. Assign a single owner per artifact. Use the specialist responsible for the next observable result.
3. **Verify and deliver.** Choose Testing, Review, Security Audit, or a domain check as the risks require. Release or publish only within established authorization. Return evidence and unresolved limits to the task owner. Project closes milestones only from verified deliverables.
4. **Feed results back.** Implementation failures go to Debugging or the owning specialist. A disproved assumption returns to Planning or Architecture. Missing evidence goes to Research or the relevant evidence owner. Production or user feedback becomes a new scoped intake item if further work is authorized.

A peer link is a route for a concrete need. Follow it only when the receiving role owns the next decision, check or deliverable. Keep one parent owner and a shared record rather than copying entire chats. Enter any role directly and return its result to the caller. When a task needs cross-specialty routing, Project can route to any role below.

## Handoff

Carry the goal, next owner and requested output, scope and existing permissions, input versions or artifact links, acceptance check, actual evidence status and next action if blocked. A short paragraph is enough for simple work. For multi-stage work, link the existing plan/casebook records. Distinguish pending, failed, blocked and verified results. On resume, recheck changed inputs and reconcile uncertain effects before retrying.

Re-enter a role only for new evidence, a changed requirement or a bounded repair. Preserve unaffected work. Stop when accepted checks are satisfied, or report the concrete missing dependency and retain a resumable state. The role map is a directory and feedback model. It does not provide an autonomous scheduler.

## Evaluate a role

Each linked skill has a representative acceptance case. Before rating it, define the expected output and the failure the check must catch. Run a normal case and a failure or variation, compare against the prior version where feasible, and keep the exact checks and results. A scenario in the instructions is a proposed check. Simulated evidence, live integration and physical target results have separate scopes.

## Leadership and coordination

| Role | Owns | Typical next specialists |
|---|---|---|
| Portfolio lead · [ultimate-project-workflow](../../../ultimate-project-workflow/SKILL.md) | Milestones, priorities, and blockers | [ultimate-planning-workflow](../../../ultimate-planning-workflow/SKILL.md), [ultimate-agent-workflow](../../../ultimate-agent-workflow/SKILL.md) |
| Delivery planner · [ultimate-planning-workflow](../../../ultimate-planning-workflow/SKILL.md) | Requirements, dependencies, and acceptance | [ultimate-architecture-workflow](../../../ultimate-architecture-workflow/SKILL.md), [ultimate-review-workflow](../../../ultimate-review-workflow/SKILL.md) |
| Systems architect · [ultimate-architecture-workflow](../../../ultimate-architecture-workflow/SKILL.md) | Boundaries, consistency, and operating costs | [ultimate-fullstack-workflow](../../../ultimate-fullstack-workflow/SKILL.md), [ultimate-planning-workflow](../../../ultimate-planning-workflow/SKILL.md) |
| Execution coordinator · [ultimate-agent-workflow](../../../ultimate-agent-workflow/SKILL.md) | Ownership, handoffs, and resumption | [ultimate-multi-agent-invoker](../../../ultimate-multi-agent-invoker/SKILL.md), [ultimate-project-workflow](../../../ultimate-project-workflow/SKILL.md) |
| Staffing and integration lead · [ultimate-multi-agent-invoker](../../../ultimate-multi-agent-invoker/SKILL.md) | Authorized dispatch and shared-resource conflicts | [ultimate-review-workflow](../../../ultimate-review-workflow/SKILL.md), [ultimate-agent-workflow](../../../ultimate-agent-workflow/SKILL.md) |
| Design facilitator · [ultimate-brainstorm-workflow](../../../ultimate-brainstorm-workflow/SKILL.md) | Options and decision-changing experiments | [ultimate-research-workflow](../../../ultimate-research-workflow/SKILL.md), [ultimate-planning-workflow](../../../ultimate-planning-workflow/SKILL.md) |

## Evidence and communications

| Role | Owns | Typical next specialists |
|---|---|---|
| Evidence analyst · [ultimate-research-workflow](../../../ultimate-research-workflow/SKILL.md) | Source applicability and disputed claims | [ultimate-planning-workflow](../../../ultimate-planning-workflow/SKILL.md), [ultimate-brainstorm-workflow](../../../ultimate-brainstorm-workflow/SKILL.md) |
| Source library specialist · [ultimate-notebooklm-workflow](../../../ultimate-notebooklm-workflow/SKILL.md) | Ingestion, indexing, and grounded answers | [ultimate-research-workflow](../../../ultimate-research-workflow/SKILL.md), [ultimate-document-intelligence-workflow](../../../ultimate-document-intelligence-workflow/SKILL.md) |
| Document extraction specialist · [ultimate-document-intelligence-workflow](../../../ultimate-document-intelligence-workflow/SKILL.md) | OCR, table fidelity, and source provenance | [ultimate-document-workflow](../../../ultimate-document-workflow/SKILL.md), [ultimate-research-workflow](../../../ultimate-research-workflow/SKILL.md) |
| Word production specialist · [ultimate-document-workflow](../../../ultimate-document-workflow/SKILL.md) | Document editing, layout, and tracked changes | [ultimate-document-intelligence-workflow](../../../ultimate-document-intelligence-workflow/SKILL.md), [ultimate-documentation-workflow](../../../ultimate-documentation-workflow/SKILL.md) |
| Technical publications lead · [ultimate-documentation-workflow](../../../ultimate-documentation-workflow/SKILL.md) | Testable quickstarts and accurate references | [ultimate-testing-workflow](../../../ultimate-testing-workflow/SKILL.md), [ultimate-project-workflow](../../../ultimate-project-workflow/SKILL.md) |
| Editorial specialist · [ultimate-natural-english-workflow](../../../ultimate-natural-english-workflow/SKILL.md) | Clarity and fidelity to protected facts | [ultimate-documentation-workflow](../../../ultimate-documentation-workflow/SKILL.md), [ultimate-project-workflow](../../../ultimate-project-workflow/SKILL.md) |
| Code intelligence analyst · [ultimate-graphify-workflow](../../../ultimate-graphify-workflow/SKILL.md) | Graph freshness and corroborated impact | [ultimate-code-cleaner](../../../ultimate-code-cleaner/SKILL.md), [ultimate-review-workflow](../../../ultimate-review-workflow/SKILL.md) |

## Product and software engineering

| Role | Owns | Typical next specialists |
|---|---|---|
| Agent systems engineer · [ultimate-agent-dev-workflow](../../../ultimate-agent-dev-workflow/SKILL.md) | Tool contracts, budgets, and durable runtime state | [ultimate-security-workflow](../../../ultimate-security-workflow/SKILL.md), [ultimate-testing-workflow](../../../ultimate-testing-workflow/SKILL.md) |
| API contract engineer · [ultimate-api-workflow](../../../ultimate-api-workflow/SKILL.md) | Compatibility, authorization, and retry semantics | [ultimate-database-workflow](../../../ultimate-database-workflow/SKILL.md), [ultimate-fullstack-workflow](../../../ultimate-fullstack-workflow/SKILL.md) |
| Platform diagnostics specialist · [ultimate-best-practices-workflow](../../../ultimate-best-practices-workflow/SKILL.md) | Version-aware performance and framework behavior | [ultimate-frontend-workflow](../../../ultimate-frontend-workflow/SKILL.md), [ultimate-testing-workflow](../../../ultimate-testing-workflow/SKILL.md) |
| Frontend engineer · [ultimate-frontend-workflow](../../../ultimate-frontend-workflow/SKILL.md) | UI behavior, rendering, and performance | [ultimate-ux-workflow](../../../ultimate-ux-workflow/SKILL.md), [ultimate-best-practices-workflow](../../../ultimate-best-practices-workflow/SKILL.md) |
| Application integration engineer · [ultimate-fullstack-workflow](../../../ultimate-fullstack-workflow/SKILL.md) | UI-to-data behavior and partial failure | [ultimate-api-workflow](../../../ultimate-api-workflow/SKILL.md), [ultimate-testing-workflow](../../../ultimate-testing-workflow/SKILL.md) |
| User experience and accessibility specialist · [ultimate-ux-workflow](../../../ultimate-ux-workflow/SKILL.md) | Task flow, accessibility, and user recovery | [ultimate-frontend-workflow](../../../ultimate-frontend-workflow/SKILL.md), [ultimate-testing-workflow](../../../ultimate-testing-workflow/SKILL.md) |
| Code maintenance specialist · [ultimate-code-cleaner](../../../ultimate-code-cleaner/SKILL.md) | Evidence-backed removal and runtime reachability | [ultimate-graphify-workflow](../../../ultimate-graphify-workflow/SKILL.md), [ultimate-refactoring-workflow](../../../ultimate-refactoring-workflow/SKILL.md) |
| Modernization engineer · [ultimate-refactoring-workflow](../../../ultimate-refactoring-workflow/SKILL.md) | Behavior preservation and incremental migration | [ultimate-testing-workflow](../../../ultimate-testing-workflow/SKILL.md), [ultimate-review-workflow](../../../ultimate-review-workflow/SKILL.md) |

## Data and infrastructure

| Role | Owns | Typical next specialists |
|---|---|---|
| Data pipeline engineer · [ultimate-data-workflow](../../../ultimate-data-workflow/SKILL.md) | Ingestion, reconciliation, and replay | [ultimate-database-workflow](../../../ultimate-database-workflow/SKILL.md), [ultimate-testing-workflow](../../../ultimate-testing-workflow/SKILL.md) |
| Database engineer · [ultimate-database-workflow](../../../ultimate-database-workflow/SKILL.md) | Schemas, query plans, migrations, and restore | [ultimate-api-workflow](../../../ultimate-api-workflow/SKILL.md), [ultimate-deployment-workflow](../../../ultimate-deployment-workflow/SKILL.md) |
| Caching and latency engineer · [ultimate-caching-workflow](../../../ultimate-caching-workflow/SKILL.md) | Freshness, contention, and stale writes | [ultimate-database-workflow](../../../ultimate-database-workflow/SKILL.md), [ultimate-testing-workflow](../../../ultimate-testing-workflow/SKILL.md) |
| Operations automation engineer · [ultimate-automation-workflow](../../../ultimate-automation-workflow/SKILL.md) | Idempotent jobs, scheduling, and recovery | [ultimate-deployment-workflow](../../../ultimate-deployment-workflow/SKILL.md), [ultimate-testing-workflow](../../../ultimate-testing-workflow/SKILL.md) |
| Build systems engineer · [ultimate-monorepo-workflow](../../../ultimate-monorepo-workflow/SKILL.md) | Task graph, cache correctness, and package releases | [ultimate-automation-workflow](../../../ultimate-automation-workflow/SKILL.md), [ultimate-testing-workflow](../../../ultimate-testing-workflow/SKILL.md) |
| Cloud runtime engineer · [ultimate-serverless-workflow](../../../ultimate-serverless-workflow/SKILL.md) | Provider authorization, durable events, and retries | [ultimate-database-workflow](../../../ultimate-database-workflow/SKILL.md), [ultimate-deployment-workflow](../../../ultimate-deployment-workflow/SKILL.md) |
| Release engineer · [ultimate-deployment-workflow](../../../ultimate-deployment-workflow/SKILL.md) | Rollout gates and service recovery | [ultimate-testing-workflow](../../../ultimate-testing-workflow/SKILL.md), [ultimate-project-workflow](../../../ultimate-project-workflow/SKILL.md) |
| Source-control steward · [ultimate-git-workflow](../../../ultimate-git-workflow/SKILL.md) | Repository state and safe integration | [ultimate-review-workflow](../../../ultimate-review-workflow/SKILL.md), [ultimate-deployment-workflow](../../../ultimate-deployment-workflow/SKILL.md) |

## Devices and electronics

| Role | Owns | Typical next specialists |
|---|---|---|
| Electrical and PCB engineer · [ultimate-hardware-design-workflow](../../../ultimate-hardware-design-workflow/SKILL.md) | Ratings, topology, and qualification | [ultimate-embedded-programming-workflow](../../../ultimate-embedded-programming-workflow/SKILL.md), [ultimate-iot-hardware-workflow](../../../ultimate-iot-hardware-workflow/SKILL.md) |
| Firmware engineer · [ultimate-embedded-programming-workflow](../../../ultimate-embedded-programming-workflow/SKILL.md) | ISR, DMA, timing, and safe device behavior | [ultimate-hardware-design-workflow](../../../ultimate-hardware-design-workflow/SKILL.md), [ultimate-iot-hardware-workflow](../../../ultimate-iot-hardware-workflow/SKILL.md) |
| Device and OTA engineer · [ultimate-iot-hardware-workflow](../../../ultimate-iot-hardware-workflow/SKILL.md) | Update validation, boot selection, and recovery | [ultimate-embedded-programming-workflow](../../../ultimate-embedded-programming-workflow/SKILL.md), [ultimate-iot-software-workflow](../../../ultimate-iot-software-workflow/SKILL.md) |
| Connected device backend engineer · [ultimate-iot-software-workflow](../../../ultimate-iot-software-workflow/SKILL.md) | Broker identity, telemetry, and command lifecycle | [ultimate-security-workflow](../../../ultimate-security-workflow/SKILL.md), [ultimate-data-workflow](../../../ultimate-data-workflow/SKILL.md) |

## Project tracking

| Role | Owns | Typical next specialists |
|---|---|---|
| Notion project operations lead · [ultimate-notion-workflow](../../../ultimate-notion-workflow/SKILL.md) | Project identity, plans/tasks, progress, evidence and sync recovery | [ultimate-project-workflow](../../../ultimate-project-workflow/SKILL.md), [ultimate-planning-workflow](../../../ultimate-planning-workflow/SKILL.md), [ultimate-review-workflow](../../../ultimate-review-workflow/SKILL.md) |

## Quality and assurance

| Role | Owns | Typical next specialists |
|---|---|---|
| Verification engineer · [ultimate-testing-workflow](../../../ultimate-testing-workflow/SKILL.md) | Outcome assertions and failure coverage | [ultimate-review-workflow](../../../ultimate-review-workflow/SKILL.md), [ultimate-debugging-workflow](../../../ultimate-debugging-workflow/SKILL.md) |
| Independent quality reviewer · [ultimate-review-workflow](../../../ultimate-review-workflow/SKILL.md) | Consequence-based findings and current evidence | [ultimate-debugging-workflow](../../../ultimate-debugging-workflow/SKILL.md), [ultimate-project-workflow](../../../ultimate-project-workflow/SKILL.md) |
| Incident investigator · [ultimate-debugging-workflow](../../../ultimate-debugging-workflow/SKILL.md) | Reproduction, cause, and minimal repairs | [ultimate-testing-workflow](../../../ultimate-testing-workflow/SKILL.md), [ultimate-planning-workflow](../../../ultimate-planning-workflow/SKILL.md) |
| Application security engineer · [ultimate-security-workflow](../../../ultimate-security-workflow/SKILL.md) | Threat controls and negative authorization cases | [ultimate-security-audit-workflow](../../../ultimate-security-audit-workflow/SKILL.md), [ultimate-testing-workflow](../../../ultimate-testing-workflow/SKILL.md) |
| Security assurance auditor · [ultimate-security-audit-workflow](../../../ultimate-security-audit-workflow/SKILL.md) | Reachability, control evidence, and audit scope | [ultimate-security-workflow](../../../ultimate-security-workflow/SKILL.md), [ultimate-review-workflow](../../../ultimate-review-workflow/SKILL.md) |
