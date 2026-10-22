---
name: ultimate-automation-workflow
description: >
  Workflow for developer CLI utilities, task runners, build automations,
  durable step workflows, POSIX-compliant scripting, and idempotent cron schedulers.
  Triggers on "ultimate automation workflow", "/ultimate-automation-workflow", or when
  writing local automation scripts, build flows, or CLI utilities.
argument-hint: "[cli-script | build-automation | task-runner | --dry-run | --cron]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate Automation and Scripting Workflow

## Inputs and boundaries

Identify the requested operation, resolved target roots/resources, shell/OS, credentials scope, rerun semantics, destructive effects and recovery needs. Keep local tasks local; use distributed scheduling only when needed. Discover installed parser, scheduler and locking APIs. Existing authorization persists; a dry run does not authorize additional targets.

## Safe execution contract

1. Validate flags, paths and environment before mutation. Destructive operations need a useful dry run regardless of object count. Show exact resolved targets, proposed changes and exclusions. Reject filesystem root, allowed-root escape, unexpected symlink/junction traversal and unapproved recursive scope. Use native shell file APIs end-to-end.
2. Preserve user files. Use a unique task scratch directory and manifest; do not delete a pre-existing shared `scratch/`. Write replacements atomically where supported. Record checkpoints before irreversible boundaries.
3. Repeated runs must have defined effects: stable record keys, compare-before-write, transactional updates or resumable operation IDs. Not every operation can be repeated safely; document reconciliation for uncertain external outcomes.
4. Separate machine output (stdout) from progress/diagnostics (stderr). Redact credentials and private data. Use documented nonzero failure statuses; avoid assuming arbitrary code numbers are portable conventions.
5. Bound network calls, retries, concurrency, total runtime and output size. Honor cancellation; distinguish retryable transport failures from validation/auth failures. Do not retry side effects without a deduplication/reconciliation protocol.

## Await async CLI actions

Illustrative Commander integration; verify installed version and actual operation implementation. Await async parsing; set exitCode rather than exiting before pending output flushes. `executeCleanup` must enforce the target policy above, not merely log a dry-run banner.

```javascript
import { Command } from 'commander';

export async function runCli(argv, executeCleanup) {
  const program = new Command();
  program.name('artifact-cleaner')
    .requiredOption('--path <dir>', 'Explicit cleanup target')
    .option('--dry-run', 'List proposed changes without mutation', false)
    .action(async (options) => {
      await executeCleanup(options.path, { dryRun: options.dryRun });
    });
  await program.parseAsync(argv);
}
// Entry point: await runCli(process.argv, executeCleanup).catch(error => {
//   console.error(safeError(error)); process.exitCode = 1;
// });
```

## Owner-token lock example

Executable JavaScript with the same atomic adapter contract as the caching workflow: acquisition is SET NX PX; release compares token and deletes atomically. Adapter honors signal and uses network timeouts. Throw on contention so the caller chooses skip, retry or failure. Never terminate the whole process inside a reusable lock helper.

```javascript
import { randomUUID } from 'node:crypto';

export async function withLock({ store, key, task, leaseMs = 60000,
  timeoutMs = 30000, signal }) {
  if (!(leaseMs > 0 && timeoutMs > 0 && timeoutMs < leaseMs)) {
    throw new RangeError('Task deadline must be positive and shorter than lease');
  }
  const bounded = signal
    ? AbortSignal.any([signal, AbortSignal.timeout(timeoutMs)])
    : AbortSignal.timeout(timeoutMs);
  const token = randomUUID();
  if (!await store.tryAcquire(key, token, { leaseMs, signal: bounded })) {
    throw new Error('Lock conflict');
  }
  try {
    bounded.throwIfAborted();
    return await task({ signal: bounded });
  } finally {
    try {
      await store.releaseIfOwner(key, token, { signal: AbortSignal.timeout(500) });
    } catch { /* Lease expires; report cleanup failure through telemetry. */ }
  }
}
```

A nominal deadline shorter than lease is not a correctness guarantee during process suspension or ignored cancellation. Use fencing/transaction constraints at the actual resource for exclusive writes. An expired owner must never delete its successor's lock; a plain DEL is forbidden. Local process/file locking may be more appropriate than Redis for a local script.

## Interruptions and schedules

Handle SIGINT/SIGTERM with an idempotent shutdown path and bounded cleanup. Exit hooks cannot await arbitrary async work and cannot guarantee cleanup on power loss/SIGKILL; inspect the manifest on next startup and resume/reconcile safely. Do not erase unresolved work automatically.

For scheduled jobs, explicitly record timezone/DST behavior, run identity, overlapping-run policy, missed-run/coalescing behavior, retry budget, delivery authentication, duplicate-event handling, alert destination and disabled-job rollback. Match the selected scheduler's actual semantics; creating a schedule twice must not create accidental duplicates. Codex reminder/chat automation uses its automation tools rather than application cron code.

## Completion evidence

Verify dry run causes no mutation; escaped/symlinked target is rejected; rejected async action exits nonzero; pipes contain valid machine data; lock A cannot unlock successor B; concurrent runs and interrupted resume preserve invariants. Use disposable files/stubs, never live deletion as a test. Report actual checks, untested scheduler/provider assumptions and recovery manifest location.

Sources: [Commander async actions](https://github.com/tj/commander.js#action-handler), [Redis lock ownership](https://redis.io/docs/latest/develop/clients/patterns/distributed-locks/).
