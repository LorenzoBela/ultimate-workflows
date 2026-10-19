---
name: ultimate-deployment-workflow
description: >
  Flawless 10/10 Master Workflow for CI/CD, multi-stage Docker packaging, blue-green / canary rollouts,
  automated health check synthetic probes, feature flag safety shields, and zero-downtime rollbacks.
  Triggers on "ultimate deployment workflow", "/ultimate-deployment-workflow", or when
  handling releases, Dockerfiles, CI configurations, or service deployments.
argument-hint: "[ci-config | dockerfile | deploy-target | --canary | --blue-green | --rollback]"
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

# Ultimate Deployment & Release Engineering Workflow (10/10 Master Engine)

This workflow drives multi-stage container optimization, declarative CI/CD pipelines, zero-downtime progressive rollouts (Blue/Green & Canary), synthetic health probing, and automated rollback triggers.

```
                                      [TAGGED COMMIT / RELEASE ARTIFACT]
                                                      │
                          ┌───────────────────────────┴───────────────────────────┐
                          ▼                                                       ▼
              [PHASE 1: MULTI-STAGE CONTAINER PACKAGING]              [PHASE 2: PROGRESSIVE ROLLOUT ENGINE]
              ├─ Builder Stage (Compiles + Types)                     ├─ Blue/Green or Canary (10% -> 50% -> 100%)
              ├─ Scratch/Alpine Distroless Runner                     ├─ Feature Flags (Upstash Redis Toggle)
              └─ Pinned SHA256 Base Image Digests                     └─ Reversible DB Migration Pre-Flight
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: SYNTHETIC PROBES & READINESS GATES                 │
        │  • /healthz (Liveness) • /ready (Deep Dependency DB Check) • Synthetic Smoke│
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: AUTOMATED ROLLBACK & INCIDENT GUARD]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🛑 ROLLBACK  │           │ 📉 METRICS   │           │ 📴 SIGTERM   │
            │ Auto-Revert  │           │ 5xx Spikes   │           │ Drain Conns  │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Deployment Engineering

1. **Pinned Digest Base Images**: Base images must be pinned to immutable SHA256 hashes or specific minor tags (`node:20.11-alpine`), never `:latest`.
2. **Distroless / Non-Root Containers**: Production container images must run as non-root users (`USER 1001`) with unnecessary debug binaries stripped out.
3. **Deep vs Shallow Health Checks**:
   - `/healthz` (Liveness): Validates the HTTP server is accepting connections.
   - `/ready` (Readiness): Actively validates database connectivity, Redis ping, and queue consumer status.
4. **Automated Rollback on Error Spike**: If 5xx error rate exceeds $1.0\%$ or latency increases by $> 50\%$ within 5 minutes of release, automatically revert to the previous stable release.
5. **Zero-Downtime Graceful Teardown**: Listen for `SIGTERM`, stop accepting new connections, finish inflight requests (30s timeout), and close database pools cleanly.

---

## 🔬 The 4-Phase Deployment Pipeline

### Phase 1: Production Multi-Stage Dockerfile
```dockerfile
# Stage 1: Build & Dependencies
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json pnpm-lock.yaml ./
RUN npm install -g pnpm && pnpm install --frozen-lockfile
COPY . .
RUN pnpm build

# Stage 2: Production Distroless Runner
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
RUN addgroup --system --gid 1001 nodejs && adduser --system --uid 1001 appuser
COPY --from=builder --chown=appuser:nodejs /app/dist ./dist
COPY --from=builder --chown=appuser:nodejs /app/node_modules ./node_modules
USER appuser
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

### Phase 2: Canary & Feature-Flagged Rollouts
- Route $10\%$ of live traffic to the new revision; monitor error rates for 10 minutes before expanding to $50\%$ and $100\%$.
- Guard new UI and billing features behind Upstash Redis feature flags for instant 0-second killswitch capability:
  ```typescript
  import { Redis } from '@upstash/redis';
  const redis = Redis.fromEnv();

  export async function isFeatureEnabled(flagName: string): Promise<boolean> {
    const status = await redis.get<string>(`flag:${flagName}`);
    return status === 'enabled';
  }
  ```

### Phase 3: Synthetic Health & Readiness Probes
```typescript
import express from 'express';
import { db } from './db';
import { redis } from './redis';

const app = express();

app.get('/healthz', (req, res) => res.status(200).send('OK'));

app.get('/ready', async (req, res) => {
  try {
    await db.$queryRaw`SELECT 1`;
    await redis.ping();
    res.status(200).json({ status: 'READY', uptime: process.uptime() });
  } catch (err) {
    res.status(503).json({ status: 'UNAVAILABLE', error: (err as Error).message });
  }
});
```

### Phase 4: Graceful Shutdown (`SIGTERM` Handler)
```typescript
const server = app.listen(3000);

process.on('SIGTERM', () => {
  console.log('SIGTERM signal received: closing HTTP server');
  server.close(async () => {
    console.log('HTTP server closed. Draining DB & Redis pools...');
    await db.$disconnect();
    await redis.quit();
    process.exit(0);
  });
});
```
