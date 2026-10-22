---
name: ultimate-agent-workflow
description: >
  Organize agent execution, durable handoffs, context and versioned memory. Use for complex execution or context management; use the multi-agent invoker for authorized parallel delegation.
argument-hint: "[handoff | execution | memory]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Agent execution and durable handoffs

Use for complex execution, context handoffs and persistent working notes. Use the multi-agent invoker when parallel agents are explicitly requested or otherwise authorized. Do not introduce Redis, cloud memory or a new runtime solely to track a small task.

## Inputs and scope

Record objective, constraints, current user authorization, base revision, existing dirty/index state, available tools, resource limits and acceptance criteria. Define each delegated task's read/write ownership and dependencies. A prompt boundary documents ownership; it is not enforced filesystem isolation.

Keep cross-cutting integration in the parent. Delegate bounded investigations or independent implementation only when the extra coordination helps. Read-only agents may share a workspace; parallel writers need a host-supported isolated workspace or verified non-overlapping ownership with serialized shared resources. Never imply a host creates isolated branches unless that feature is confirmed.

## Execution sequence

1. Decompose by deliverable and dependency, not an arbitrary two-file rule. State outputs and run-ready checks; keep uncertain file locations searchable rather than inventing exact line ranges.
2. Give the child the objective, relevant evidence, explicit ownership, constraints, verification commands, deadline and return schema. Include necessary source context; a graph summary alone may omit critical behavior.
3. Capture actual task ID/status. Respect host concurrency and child-spawning limits. Use configurable deadlines, cooperative cancellation and progress signals; a slow task is not automatically a failed task.
4. On completion, inspect the actual diff/artifact and independently integrate. Run checks appropriate to changed behavior; record baseline failures separately. Review by a second agent is useful for high-risk changes, but does not replace the builder's own checks.
5. Preserve failed branches, raw evidence and user-owned scratch files. Remove only artifacts created by this run when no longer needed and safely recoverable. Do not compress or overwrite README/memory files unless requested.

## Handoff contract

Use the host's durable task state when available; otherwise write a scoped local note. Store references, decisions and remaining work rather than an unbounded conversation transcript.

```json
{
  "schema_version": 1,
  "task_id": "example-investigation",
  "status": "blocked",
  "scope_fingerprint": "computed-from-objective-and-owned-resources",
  "base_revision": "actual-revision",
  "owned_paths": ["src/example.ts"],
  "completed": [],
  "remaining": ["Confirm actual provider response schema"],
  "decisions": [],
  "evidence": [],
  "usage": {"tokens": null, "source": "unavailable"},
  "blocker": {"reason": "Required tool unavailable", "next_action": "Connect supported provider"}
}
```

This is a format example, not a completed task. Production notes must contain actual IDs, revisions and evidence. Use `pending`, `running`, `blocked`, `failed`, `cancelled` and `complete` distinctly. A task is complete only when its acceptance evidence exists.

## Memory consistency

Persist only relevant, non-sensitive observations with source revision/date, author task, stable observation key and version. Use compare-and-set or a transaction for updates. An idempotency key prevents duplicate inserts on retry; concurrent incompatible observations remain a conflict to reconcile, not last-writer truth. If optional memory tooling is unavailable, retain a local note and disclose that external synchronization did not happen.

On resume, verify scope, repository state and freshness. Reconcile uncertain external effects before retrying. Do not blindly rollback a child's file when another actor has edited it; compare base/current/diff and preserve unrelated work.

## Context and output

Summarize tool output while retaining command, exit status, failure context and a raw-log reference when produced. Never turn text containing “pass” into success. Keep facts, uncertainty and constraints intact when compressing prose. Use actual usage metrics where exposed; no estimated token savings presented as measurements.

Return changed paths, concrete outcomes, checks and limitations, unresolved blockers, retained artifacts and the next resume action. Do not push, send messages or create paid resources without established task authorization.
