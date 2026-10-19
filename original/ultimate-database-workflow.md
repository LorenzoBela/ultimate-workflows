---
name: ultimate-database-workflow
description: >
  Flawless 10/10 Master Workflow for database schema design, query optimization, indexing strategies,
  and transaction planning. Integrates Postgres/Supabase best practices, query plan analysis (EXPLAIN ANALYZE),
  keyset cursor pagination, deadlock tree diagnostics, and connection pooling.
  Triggers on "ultimate database workflow", "/ultimate-database-workflow", or when
  designing SQL schemas or optimizing slow queries.
argument-hint: "[table-schema | slow-query | --explain | --index | --migration]"
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

# Ultimate Database & Query Optimization Workflow (10/10 Master Engine)

This workflow guides the design, index planning, execution optimization, and securing of relational and distributed databases. It guarantees sub-millisecond query performance, absolute mathematical data integrity, and bulletproof Row-Level Security (RLS).

```
                                      [DATABASE SCHEMA / QUERY TARGET]
                                                     │
                          ┌──────────────────────────┴──────────────────────────┐
                          ▼                                                     ▼
              [PHASE 1: SCHEMA CONSTRAINTS]                         [PHASE 2: INDEX STRATEGY & EXPLAIN]
              ├─ Primary Keys & Strict Types                        ├─ B-Tree / GIN / GiST Selection
              ├─ Foreign Keys & Cascade Policies                    ├─ EXPLAIN (ANALYZE, BUFFERS) Profiling
              └─ Check Constraints & Timestamps                     └─ Partial & Covering Indexes
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: HIGH-PERFORMANCE QUERYING & KEYSET CURSORS         │
        │  • Zero `SELECT *` • Keyset Pagination (O(1)) • Avoid N+1 Join Optimizations│
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: ROW-LEVEL SECURITY & LOCK DIAGNOSTICS]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🔒 RLS POLICY│           │ ⚡ DEADLOCK  │           │ 🏊 PGBOUNCER │
            │ auth.uid()   │           │ pg_locks SQL │           │ Port 6543    │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Database Engineering

1. **Schema Is the Absolute Source of Truth**: Business invariants belong in database constraints (`NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY`), not in application code.
2. **Zero Floating-Point Numbers for Currency**: Always use `integer` minor units (cents) or `numeric(19,4)`.
3. **No `SELECT *` in Production**: Specify exact columns to allow index-only scans and prevent bandwidth bloat.
4. **Explain Before Optimizing**: Every query modification must be verified with `EXPLAIN (ANALYZE, BUFFERS)`.
5. **Reversible Migrations Only**: Every schema alteration must have a documented, tested down/rollback migration.
6. **Keyset Pagination for Deep Sets**: Keyset (`WHERE id > $last_id LIMIT 50`) is required over `OFFSET` for tables $> 1000$ rows.
7. **Serverless Connection Pooling**: All serverless connections MUST connect via PgBouncer in transaction mode (port 6543) with `connection_limit=1`.

---

## 🔬 The 6-Phase Database Pipeline

### Phase 1: Schema Design & Strict Typing
*   **Primary Keys:** `uuid` with `gen_random_uuid()` or `bigint generated always as identity`.
*   **Timestamps:** Always `timestamptz` (with timezone).
*   **Text/Enums:** Prefer `text` + `CHECK (status IN ('PENDING', 'ACTIVE', 'COMPLETED'))` over native Postgres ENUM for smooth migrations.

### Phase 2: Index Strategy Matrix
| Query Pattern | Optimal Index Type | Example |
|---|---|---|
| Foreign Keys & ID Lookups | B-Tree | `CREATE INDEX idx_deliveries_rider ON deliveries(rider_id)` |
| Filtered Subsets (Active only) | Partial B-Tree | `CREATE INDEX idx_active_tasks ON tasks(status) WHERE status != 'DONE'` |
| Multi-column `WHERE A = 1 AND B = 2` | Composite B-Tree | `CREATE INDEX idx_user_org ON members(org_id, user_id)` |
| JSONB Key-Value Search | GIN (jsonb_path_ops) | `CREATE INDEX idx_meta ON logs USING gin(metadata jsonb_path_ops)` |
| Full-Text Search | GIN (to_tsvector) | `CREATE INDEX idx_search ON articles USING gin(to_tsvector('english', title))` |
| Geospatial Proximity | GiST | `CREATE INDEX idx_geo ON places USING gist(geom)` |

### Phase 3: EXPLAIN (ANALYZE, BUFFERS) Profiling
- **Red Flag 1:** `Seq Scan` on table with $> 1000$ rows $\rightarrow$ Add B-Tree index.
- **Red Flag 2:** `Sort: external merge Disk` $\rightarrow$ Increase `work_mem` or add covering index.
- **Red Flag 3:** `Buffers: shared read` high $\rightarrow$ Cache cold or table exceeds `shared_buffers`.

### Phase 4: Row-Level Security (RLS) Policy Design
```sql
ALTER TABLE deliveries ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Rider view assigned deliveries"
ON deliveries FOR SELECT
USING (rider_id = auth.uid());

CREATE POLICY "Rider update assigned deliveries"
ON deliveries FOR UPDATE
USING (rider_id = auth.uid())
WITH CHECK (rider_id = auth.uid());
```

### Phase 5: Keyset (Cursor-Based) Pagination
```sql
SELECT id, title, created_at
FROM events
WHERE (created_at, id) < ($last_created_at, $last_id)
ORDER BY created_at DESC, id DESC
LIMIT 50;
```

### Phase 6: Deadlock & Lock Tree Diagnostics
```sql
SELECT blocked_locks.pid AS blocked_pid,
       blocked_activity.query AS blocked_query,
       blocking_locks.pid AS blocking_pid,
       blocking_activity.query AS blocking_query
FROM pg_catalog.pg_locks blocked_locks
JOIN pg_catalog.pg_stat_activity blocked_activity ON blocked_activity.pid = blocked_locks.pid
JOIN pg_catalog.pg_locks blocking_locks ON blocking_locks.locktype = blocked_locks.locktype
JOIN pg_catalog.pg_stat_activity blocking_activity ON blocking_activity.pid = blocking_locks.pid
WHERE NOT blocked_locks.granted;
```
