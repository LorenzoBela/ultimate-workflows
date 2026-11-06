---
name: ultimate-notion-workflow
description: >
  Manage project plans, tasks, progress, blockers, review evidence and delivery in Notion. Resolve the current project from a validated binding or repository identity, reuse existing records, and recover uncertain tracking writes. Use for Notion-backed project tracking or the project orchestrator's mandatory tracking handoff.
---

# Notion project operations

Own Notion project identity and tracking while the project orchestrator owns the user's overall result. The orchestrator must use this specialist for its required tracking checkpoints. One assistant can apply both workflows sequentially. Use connected tools actually exposed by the current host and preserve the user's existing authorization.

## Resolve and inspect

Apply the [shared strict tracking guide](../ultimate-project-workflow/resources/ultimate-project-workflow/notion-tracking.md). It defines the canonical repository key, shared private registry, lifecycle checkpoints and interruption behavior. The [read-only identity resolver](../ultimate-project-workflow/resources/ultimate-project-workflow/notion_project.py) supports local binding discovery without creating or updating Notion records.

First honor a recorded project-specific user exclusion. A tracking_disabled_by_user result skips Notion tracking for that project and must not trigger page recreation. Only an explicit user instruction can create or remove that exclusion. Resolve the repository actually affected by the task, not an incidental chat directory. Honor explicit project selection, fetch saved targets and verify their identity. Search when unbound, reuse one clear match and ask when multiple matches remain plausible. For a new project, follow the host's Notion project-setup guidance and private draft default when no shared destination was selected. Preserve existing trackers and their schema.

Check current connector access and restrictions when unknown. Before database writes, inspect its actual data-source schema. Before writing content, read the connector's current Notion Markdown specification. Retain successful project, collection, plan and task IDs in private state.

## Maintain the same project records

| Request or trigger | Owned result |
|---|---|
| Start or resume project work | Validated project identity, current plan/tasks and reconciled pending updates |
| New plan or scope | Versioned plan/spec with accepted scope, requirements, dependencies, checks and links |
| Start implementation | Existing or newly created work item with its real in-progress state |
| Progress, blocker or review | Targeted state and content update with actual evidence and next action |
| Verification and delivery | Actual check results, reviewed revision/artifact and observed commit/PR/release result |
| Close or interrupt | Honest completion or checkpoint with open blockers and pending sync status |

Track each independently actionable deliverable. Group incidental edits and commands under their work item. Keep source code, detailed test artifacts and canonical external issues in their owning systems and link them from Notion. Update recorded status only from actual evidence.

Use existing names, properties, status options and relation targets. Preserve human content and ownership. Leave unknown people and dates unset. Project relations and saved IDs must match the intended destination. Use the connector's supported targeted updates and assess warnings.

## Reliable synchronization

Use a stable project key, run/task/document key and event ID. The designated parent is the progress writer unless non-overlapping record ownership is explicitly delegated. Workers return evidence and proposed updates.

Persist recoverable pending events before uncertain writes and retain returned IDs immediately. A timeout leaves the outcome unknown until the original object/event is reconciled. Read retained target IDs before recreating records; recent search results can lag. Merge a newer human edit within scope or report a conflict.

Strict mode blocks new tracked implementation, release and full completion while required project identity or tracking writes are unresolved. Read-only discovery and safe checkpointing can continue. Keep the implementation result separate from sync state so a failed Notion update never repeats the original code or release side effect. Apply a temporary exception only when the user explicitly authorizes its scope.

## Return to the orchestrator

Return the project and task/doc URLs, stable IDs, actual state and evidence, update warnings, pending events and the next action. Mark a tracking checkpoint satisfied only when the actual write or read establishes it. The [project orchestrator](../ultimate-project-workflow/SKILL.md) decides when implementation may continue and when the overall task is complete.

The workflow runs while an agent uses it. Tool availability, credentials, permissions and host concurrency determine execution. A saved binding or installed skill does not establish a running background integration.

## Role and handoffs

**Notion project operations lead.** Own project matching and durable project tracking. Use [Planning](../ultimate-planning-workflow/SKILL.md) for implementation decisions, [Review](../ultimate-review-workflow/SKILL.md) for technical findings, and [Project](../ultimate-project-workflow/SKILL.md) for orchestration. Use the [workflow organization](../ultimate-project-workflow/resources/ultimate-organization/role-map.md) for cross-specialty work.

## Representative acceptance cases

- Equivalent SSH/HTTPS repository remotes and linked worktrees resolve to one saved project and reuse its task IDs.
- An ambiguous destination blocks tracker writes and new implementation until identity is resolved.
- A write timeout is reconciled against the original object/event before replay, preserving human edits and preventing duplicate records.
- A verified local change with failed Notion sync remains pending for tracking; it is not reimplemented to repair the sync gap.
