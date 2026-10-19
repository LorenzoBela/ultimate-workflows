---
name: ultimate-fullstack-workflow
description: >
  Flawless 10/10 Master Workflow for building full-stack applications, scalable backend microservices,
  and seamless frontend client integrations. Coordinates database schema design, REST/GraphQL/tRPC APIs,
  auth middleware, CORS controls, real-time sync (SSE/WebSockets), Next.js 15 Server Actions,
  and typed end-to-end client SDKs.
  Triggers on "ultimate fullstack workflow", "/ultimate-fullstack-workflow", or when
  initiating backend, full-stack, or API integration tasks.
argument-hint: "[api-spec | database-schema | fullstack-feature | --monolith | --microservices]"
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

# Ultimate Full-Stack Integration Workflow (10/10 Master Engine)

This workflow guides the end-to-end architecture, implementation, and production hardening of full-stack systems—linking high-performance databases, secure API layers, and fluid frontend client surfaces.

```
                                      [FULL-STACK FEATURE / SERVICE REQUIREMENT]
                                                          │
                          ┌───────────────────────────────┴───────────────────────────────┐
                          ▼                                                               ▼
              [PHASE 1: ARCHITECTURE & PROTOCOL]                              [PHASE 2: DATABASE & MIGRATIONS]
              ├─ Boundary Contract (tRPC / OpenAPI / gRPC)                    ├─ Relational Schemas & Indexes
              ├─ Storage Architecture (SQL + Redis)                           ├─ Reversible SQL Migrations
              └─ Real-Time Strategy (SSE / WebSockets)                        └─ Supabase / Postgres RLS Multi-Tenant
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: BACKEND CONTROLLERS & SECURE MIDDLEWARE            │
        │  • RequestID • CORS • RateLimit • Auth/RBAC • Input Validation (Zod) • Handlers │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: TYPED CLIENT INTEGRATIONS]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🌐 REACT RSC │           │ 📱 REACT NAT │           │ 🔄 CACHE/SWR │
            │ Server Action│           │ Offline Sync │           │ TanStack Qry │
            └──────────────┘           └──────────────┘           └──────────────┘
                                               │
                                               ▼
                                  [PHASE 5: PRODUCTION HARDENING & SMOKE]
                    Build Verifications ──► DB Connection Pool Sizing ──► Graceful SIGTERM
```

---

## 🏛️ Iron Laws of Full-Stack Engineering

1. **Feature-First Modularity**: Group controllers, services, repositories, and UI components by **feature/domain** rather than technical layer.
2. **Strict Layer Separation**:
   - *Controllers / Handlers:* Handle HTTP parsing, parameter extraction, and status code serialization.
   - *Services:* Pure business logic with zero framework/HTTP coupling.
   - *Repositories:* Pure database access and query construction.
3. **Never Trust the Client**: Validate all data entering the backend via strict Zod schemas, regardless of frontend type-safety.
4. **Zero Float Currency Invariant**: Store financial amounts in integer minor currency units (cents).
5. **Mandatory Idempotency on Mutating Endpoints**: State-changing endpoints (`POST`/`PUT`/`PATCH`) must enforce `Idempotency-Key` headers.
6. **Graceful Teardown**: Listen for `SIGTERM` / `SIGINT` signals to flush connection pools, drain active requests, and close background queues cleanly.

---

## 🔬 The 5-Phase Full-Stack Pipeline

### Phase 1: Stack Architecture & Protocol Design
*   **Action:**
    1. Define boundary protocol: **tRPC** (type-safe monorepos), **OpenAPI REST** (public APIs), or **gRPC** (high-throughput microservices).
    2. Design database schemas and caching tiers (PostgreSQL + Upstash Redis).
    3. Specify real-time strategy (Server-Sent Events for one-way feeds, WebSockets for bidirectional collaboration).

### Phase 2: Database Schema & Migration Engineering
*   **Action:**
    1. Define declarative schema with explicit relational foreign keys, indexes on filtered/sorted fields, and check constraints.
    2. Write reversible migrations (`up` and `down` SQL).
    3. Configure connection pooling (PgBouncer in transaction mode on port 6543) to prevent connection starvation.
    4. Generate TypeScript definitions directly from the database schema.

### Phase 3: Backend API & Middleware Architecture
*   **Action:**
    1. Chain middleware in deterministic order:
       `RequestID` $\rightarrow$ `Structured Logger` $\rightarrow$ `CORS (Explicit)` $\rightarrow$ `Upstash Rate Limiter` $\rightarrow$ `Auth/JWT` $\rightarrow$ `RBAC Scope` $\rightarrow$ `Zod Validator` $\rightarrow$ `Handler` $\rightarrow$ `Global Error Catcher`.
    2. Implement transactional operations: wrap multi-table state mutations in database transactions with strict timeout limits.

### Phase 4: Typed Client & Frontend Integration
*   **Action:**
    1. In **Next.js 15 App Router**:
       - Default to React Server Components (RSC) for direct server-side data fetching.
       - Use Server Actions for mutations with authentication checks *inside* the action body.
    2. In **React / Client SPAs**:
       - Use TanStack Query (React Query) with optimistic updates and automatic cache invalidation.
    3. In **React Native**:
       - Implement offline-first local SQLite / WatermelonDB sync with background network reconciliation.

### Phase 5: Production Hardening, Smoke Testing & Handoff
*   **Action:**
    1. Execute end-to-end smoke test suite: verify happy path, authentication failure, validation errors, and network retry deduplication.
    2. Verify graceful process shutdown (`SIGTERM` handler closes database pool and Redis connection).
    3. Run `lint-and-validate` to guarantee clean TypeScript builds across all workspaces.
