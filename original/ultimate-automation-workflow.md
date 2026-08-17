---
name: ultimate-automation-workflow
description: >
  Flawless 10/10 Master Workflow for developer CLI utilities, task runners, build automations,
  durable step workflows, POSIX-compliant scripting, and idempotent cron schedulers.
  Triggers on "ultimate automation workflow", "/ultimate-automation-workflow", or when
  writing local automation scripts, build flows, or CLI utilities.
argument-hint: "[cli-script | build-automation | task-runner | --dry-run | --cron]"
---

# Ultimate Automation & Scripting Workflow (10/10 Master Engine)

This workflow guides the design, implementation, and deployment of local automation, developer CLI utilities, task runners, and serverless cron schedulers to guarantee reliability, safe execution, and clean outputs.

```
                                      [AUTOMATION TASK / SCRIPT REQUIREMENT]
                                                        │
                          ┌─────────────────────────────┴─────────────────────────────┐
                          ▼                                                           ▼
              [PHASE 1: CLI ARGUMENTS & DRY-RUN]                            [PHASE 2: IDEMPOTENT EXECUTION]
              ├─ Strict Flag Parsing (Commander / Argparse)                 ├─ Redis Lock Mutex (Concurrency Shield)
              ├─ Non-Destructive --dry-run Flag                             ├─ Bounded In-Project Scratch Folders
              └─ POSIX Exit Codes (0=Success, >0=Fail)                      └─ Graceful SIGINT/SIGTERM Cleanup
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: STRUCTURED OUTPUT & OBSERVABILITY                  │
        │  • stdout for Clean Data Pipes • stderr for Diagnostics • Structured JSON Logs │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: DURABLE SCHEDULING & CRON RUNNERS]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ ⏰ QSTASH    │           │ 🔄 WORKFLOW  │           │ 🚀 CI/CD     │
            │ Serverless   │           │ Upstash Auto │           │ Pre-Commit   │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Automation & Scripting

1. **Mandatory `--dry-run` for Destructive Operations**: Any script that deletes, overwrites, or modifies $>10$ files or database rows MUST provide a non-destructive `--dry-run` flag.
2. **Strict POSIX Exit Codes**: Scripts must exit `0` on success and unique non-zero codes (`1` for validation, `2` for network timeout, `3` for lock acquisition failure) on errors.
3. **Idempotence by Default**: Re-running an automation script multiple times against the same environment must produce the exact same final state without generating duplicate records.
4. **Clean stdout vs stderr Separation**: Machine-readable data (JSON, CSV, file lists) must be piped to `stdout`; debugging narratives and progress bars must go to `stderr`.
5. **No Orphaned Temp Files**: Scripts must create temp files within `./scratch/` and register exit hooks (`trap` / `process.on('exit')`) to clean them up unconditionally.

---

## 🔬 The 4-Phase Automation Pipeline

### Phase 1: Robust CLI Parsing Template
```typescript
import { Command } from 'commander';

const program = new Command();

program
  .name('deploy-cleaner')
  .description('Purge stale staging artifacts safely')
  .option('-d, --dry-run', 'Simulate execution without modifying files', false)
  .option('-p, --path <dir>', 'Target directory path', './dist')
  .action(async (options) => {
    if (options.dryRun) {
      console.error('[DRY RUN] Simulating artifact cleanup...');
    }
    await executeCleanup(options.path, options.dryRun);
    process.exit(0);
  });

program.parse(process.argv);
```

### Phase 2: Distributed Lock Mutex (`upstash-redis-js`)
```typescript
import { Redis } from '@upstash/redis';
const redis = Redis.fromEnv();

export async function withLock(lockName: string, task: () => Promise<void>) {
  const acquired = await redis.set(`lock:${lockName}`, '1', { nx: true, ex: 60 });
  if (!acquired) {
    console.error(`[LOCK CONFLICT] Task ${lockName} is already running elsewhere.`);
    process.exit(3);
  }
  try {
    await task();
  } finally {
    await redis.del(`lock:${lockName}`);
  }
}
```

### Phase 3: Serverless Cron Scheduling (`upstash-qstash-js`)
```typescript
import { Client } from '@upstash/qstash';
const client = new Client({ token: process.env.QSTASH_TOKEN! });

// Schedule a daily recurring cron job
await client.schedules.create({
  destination: 'https://api.my-app.com/api/crons/sync-inventory',
  cron: '0 0 * * *', // Midnight UTC
  retries: 3
});
```
