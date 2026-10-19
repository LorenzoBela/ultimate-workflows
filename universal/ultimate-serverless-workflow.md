---
name: ultimate-serverless-workflow
description: >
  Flawless 10/10 Master Workflow for configuring, deploying, and managing serverless backend platforms
  (Supabase/Firebase), Edge Functions, connection poolers (PgBouncer), and ORM systems (Prisma)
  using Model Context Protocol (MCP) integrations.
  Triggers on "ultimate serverless workflow", "/ultimate-serverless-workflow", or when
  configuring database schemas, deploying Edge/Cloud functions, or writing RLS security rules.
argument-hint: "[supabase-deploy | firebase-rules | prisma-migrate | --edge | --pgbouncer]"
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

# Ultimate Serverless Backend Workflow (10/10 Master Engine)

This workflow coordinates operations, schema migrations, function deployments, cold-start mitigations, and environment configuration across serverless backends (Supabase, Firebase) and ORM systems (Prisma) using specialized MCP integrations.

```
                                      [SERVERLESS BACKEND TARGET]
                                                   │
                        ┌──────────────────────────┴──────────────────────────┐
                        ▼                                                     ▼
            [PHASE 1: ENVIRONMENT & MCP AUTH]                     [PHASE 2: SCHEMA MIGRATIONS & ORM]
            ├─ Supabase / Firebase Environment Scoping            ├─ Prisma migrate-dev / apply_migration
            ├─ Project Secrets & Connection Strings               ├─ PgBouncer Port 6543 (Pooler) Direct 5432
            └─ SDK Configs Generation                             └─ Typed TypeScript Definitions Gen
                        │
                        ▼
      ┌─────────────────────────────────────────────────────────────────────────────┐
      │                 PHASE 3: SECURITY POLICIES & RLS VERIFICATION               │
      │  • Supabase execute_sql (RLS Policies) • Firebase Security Rules • get_advisors│
      └──────────────────────────────────────┬──────────────────────────────────────┘
                                             ▼
                                [PHASE 4: EDGE FUNCTIONS & DURABLE WORKFLOWS]
                  ┌──────────────────────────┼──────────────────────────┐
                  ▼                          ▼                          ▼
          ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
          │ ⚡ DENO EDGE │           │ 🔄 WORKFLOW  │           │ 📬 QSTASH    │
          │ Deno Deploy  │           │ Upstash Flow │           │ Webhook Msg  │
          └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Serverless Backends

1. **Transaction Pooling on Port 6543**: Serverless functions must connect via PgBouncer transaction mode (`?pgbouncer=true&connection_limit=1`), reserving direct port 5432 strictly for ORM migrations.
2. **Cold-Start Budget ($< 250\text{ms}$)**: Edge functions must optimize dependencies, minimize global imports, and use lightweight HTTP clients (`@upstash/redis` over raw TCP drivers).
3. **Strict Row-Level Security**: No table may be deployed to production without explicit RLS policies for `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.
4. **Zero State in Edge Memory**: Serverless and edge instances are ephemeral; state must reside in PostgreSQL, Upstash Redis, or QStash queues.
5. **Durable Multi-Step Execution**: Long-running or multi-stage operations MUST use `upstash-workflow-js` to guarantee execution resilience across cold-restarts.

---

## 🔬 The 4-Phase Serverless Pipeline

### Phase 1: Environment & Project Scoping
- Retrieve project configurations and publishable keys via MCP tools:
  - `supabase-mcp-server/get_project`, `supabase-mcp-server/get_publishable_keys`.
  - `firebase-mcp-server/firebase_get_sdk_config`, `firebase-mcp-server/firebase_get_environment`.

### Phase 2: Schema Migrations & Dual Connection Strings (Prisma)
- Configure `schema.prisma` with pooler and direct URL separation:
  ```prisma
  datasource db {
    provider  = "postgresql"
    url       = env("DATABASE_URL")      // PgBouncer Port 6543 (transaction mode)
    directUrl = env("DIRECT_URL")        // Direct Port 5432 (migrations only)
  }
  ```
- Run migrations via `prisma-mcp-server/migrate-dev` or `supabase-mcp-server/apply_migration`.
- Generate TypeScript client types using `supabase-mcp-server/generate_typescript_types`.

### Phase 3: RLS Security Policies & Advisor Audits
- Apply strict tenant policies using `supabase-mcp-server/execute_sql`:
  ```sql
  ALTER TABLE user_data ENABLE ROW LEVEL SECURITY;
  CREATE POLICY "Tenant isolation" ON user_data
    FOR ALL USING (tenant_id = auth.jwt()->>'tenant_id');
  ```
- Run `supabase-mcp-server/get_advisors` to detect missing policies or unindexed foreign keys.

### Phase 4: Edge Functions & Durable Upstash Workflows
- Deploy Deno edge functions using `supabase-mcp-server/deploy_edge_function`.
- Deploy durable serverless workflows with `upstash-workflow-js`:
  ```typescript
  import { serve } from '@upstash/workflow/nextjs';

  export const { POST } = serve(async (context) => {
    const data = await context.run('step-1', async () => fetchData());
    await context.sleep('wait-for-webhook', 300); // 5 minutes durable sleep
    await context.run('step-2', async () => processData(data));
  });
  ```
