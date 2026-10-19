---
name: ultimate-automation-workflow
description: >
  Flawless 10/10 Master Workflow for developer CLI utilities, task runners, build automations,
  durable step workflows, POSIX-compliant scripting, and idempotent cron schedulers.
  Triggers on "ultimate automation workflow", "/ultimate-automation-workflow", or when
  writing local automation scripts, build flows, or CLI utilities.
argument-hint: "[cli-script | build-automation | task-runner | --dry-run | --cron]"
---

<!-- INVARIANT_START:ANTI_AI_SLOP -->
## 🛑 HARDENED ANTI-AI SLOP MANDATE: NATURAL PROSE & BESPOKE DESIGN CRAFT
All agent communications, architectural plans, reviews, code comments, and frontend implementations MUST strictly adhere to natural human engineering standards. Both corporate AI prose slop and cookie-cutter "vibecoded" UI slop are strictly banned.

### 1. Zero Prose & Grammar Slop (Natural Human Voice)
- **Banned Lexicon:**
  - *Empty Verbs:* delve, embark, foster, resonate, underscore, leverage, elevate, harness, navigate, empower, illuminate, facilitate, tailor, showcase, unveil.
  - *Corporate Buzz-Adjectives:* testament, tapestry, beacon, cornerstone, robust, seamless, pivotal, crucial, paramount, cutting-edge, vibrant, bespoke, game-changer, journey, realm, landscape, holistic, comprehensive, multifaceted, versatile, transformative.
  - *Formulaic Transitions:* furthermore, moreover, in conclusion, it is worth noting, at the end of the day, without further ado, needless to say.
- **Banned Syntactical Patterns:**
  - **Zero Sycophancy / Pleasantries:** NEVER start responses with "Certainly!", "Great question!", "I'd be happy to help!", "Awesome!", or "Let's dive in!".
  - **Zero Summary Outros:** NEVER end answers with a repetitive paragraph restating earlier points using generic corporate filler.
  - **Zero Formulaic "Rule-of-Three" Bullets:** Do not default to 3-bullet lists where each bullet starts with a bold abstract noun followed by a colon and fluff.
  - **Zero Hedging:** Do not write "You might want to potentially consider checking...". Write "Check X, or Y crashes."
- **Natural Voice Standard:** Speak like a systems developer in terminal, Slack, or GitHub issues: blunt, concise, precise, pragmatic. Code and runnable shell commands come first.

### 2. Zero Visual & UI/UX Design Slop (Bespoke Engineering Craft)
- **Banned Color Clichés:**
  - BAN default AI Blue-to-Indigo/Purple gradients (`bg-gradient-to-r from-blue-600 to-indigo-700` or violet hues).
  - BAN colored ambient glowing shadows (`box-shadow` with >= 24px blur matching accent color).
  - BAN washed-out low-contrast gray text (`text-gray-400` / `text-gray-500` failing WCAG AA 4.5:1).
  - BAN gradient headline text (`bg-clip-text text-transparent bg-gradient-to-r` on H1s).
- **Banned Layout & Component Tropes:**
  - BAN cookie-cutter Bento Grid walls filled with fake stats, empty cards, or generic Lucide icon spam.
  - BAN centered hero boilerplate with a floating pill above H1 (`"✨ New: [Feature]"`).
  - BAN unmodified shadcn/ui defaults (`--radius: 0.5rem`, stock button/card exports without brand styling).
  - BAN tinted circular icon containers (`bg-primary/10 text-primary p-3 rounded-full`).
  - BAN static terminal window mockups with red/yellow/green dots in the hero.
  - BAN raw emojis used as icons (`✨`, `🚀`, `⚡`, `🔒`) in production UI markup.
- **Bespoke Design Standard:**
  - Commit to an intentional aesthetic: brutalist, high-density telemetry, refined editorial, or precision dark-mode.
  - High information density (Linear/Stripe standard), micro-borders (`rgba(255,255,255,0.08)`), and tabular numerals (`tabular-nums`).
  - Every component must implement all 7 states: `Default, Hover, Focus-Visible, Active, Loading (Skeleton), Disabled, Error`.
<!-- INVARIANT_END:ANTI_AI_SLOP -->

<!-- INVARIANT_START:GRAPHIFY -->
## 🧠 HARDENED GRAPHIFY KNOWLEDGE ENGINE GATE (AST-FIRST CODE INTELLIGENCE)
Whenever `graphify-out/graph.json` exists in the repository root, agents MUST interact with the AST knowledge graph. Blind directory traversal and unconstrained multi-file context dumping are strictly banned.

1. **Zero-Blind-Grep Invariant:**
   - Running unstructured grep (`grep -r`, `Select-String *.*`, `ripgrep` across entire project) to locate callers or symbol references is FORBIDDEN when `graph.json` is present.
   - Agents must query Graphify first: `graphify query "<symbol_or_concept>"`.

2. **Blast Radius Gate (`graphify explain "<symbol>"`):**
   - Before modifying, refactoring, or deleting any shared interface, model, route, or function, the agent MUST run `graphify explain "<symbol>"`.
   - If incoming edge count > 0, every caller surfaced by Graphify MUST be explicitly enumerated in the task DAG or implementation plan before touching code.

3. **Call-Path Fault Tracing (`graphify path "<source>" "<target>" --undirected`):**
   - When debugging multi-hop failures (e.g. UI -> API -> DB), the agent must run `graphify path` to map the exact shortest call chain between entry point and crash sink before reading source code.

4. **Leiden Community Worktree Partitioning:**
   - When spawning parallel subagents in `ultimate-multi-agent-invoker`, tasks MUST be partitioned by Leiden community clusters (from `graphify-out/graph.json`).
   - If two tasks share a God Node (identified in `graphify-out/GRAPH_REPORT.md`), they CANNOT run concurrently without explicit file-level mutex locks.

5. **Subagent Context Clamp (70% Token Reduction):**
   - Never dump entire raw source files into subagent prompts. Inject only the scoped subgraph from `graphify query "<task_scope>"`.

6. **Post-Commit AST Synchronization (`graphify update .`):**
   - After completing code modifications or merging Git worktrees, the agent MUST run `graphify update .` (local AST delta update, 2s runtime, 0 API tokens) to maintain graph synchronization.
<!-- INVARIANT_END:GRAPHIFY -->

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
