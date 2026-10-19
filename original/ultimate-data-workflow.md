---
name: ultimate-data-workflow
description: >
  Flawless 10/10 Master Workflow for data pipeline engineering, streaming ETL pipelines,
  backpressure flow control, transactional batch COPY upserts, and Dead-Letter Queue (DLQ) error recovery.
  Triggers on "ultimate data workflow", "/ultimate-data-workflow", or when designing
  batch pipelines, parser scripts, database aggregations, or data transformations.
argument-hint: "[etl-pipeline | parser-script | database-aggregation | --stream | --batch | --dlq]"
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

# Ultimate Data Pipeline & ETL Workflow (10/10 Master Engine)

This workflow drives streaming data ingestion, bounded memory buffering, backpressure flow control, schema validation, transaction-safe bulk loading (PostgreSQL `COPY` / batch upsert), and Dead-Letter Queue (DLQ) anomaly isolation.

```
                                      [RAW SOURCE STREAM / BATCH DATA]
                                                     │
                          ┌──────────────────────────┴──────────────────────────┐
                          ▼                                                     ▼
              [PHASE 1: STREAMING EXTRACTION (E)]                   [PHASE 2: SCHEMA VALIDATION & CLEAN]
              ├─ Node.js / Python Reactive Streams                  ├─ Zod / Pydantic Row Validation
              ├─ Bounded Chunk Buffering (10k rows)                 ├─ Outlier Filtering & Normalization
              └─ Backpressure Ingestion Throttling                  └─ ISO-8601 UTC & Cents Conversion
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: DETERMINISTIC BUSINESS TRANSFORMATION (T)          │
        │  • Pure Functions • Idempotent Key Generation • Vector Embeddings (Upstash) │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: TRANSACTIONAL BULK LOAD (L) & DLQ]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🚀 PG COPY   │           │ 💾 DB TX     │           │ 📭 DEAD-LETT │
            │ Batch Upsert │           │ All-or-None  │           │ DLQ QStash   │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Data Pipeline Engineering

1. **Bounded Memory Invariant**: Never load entire datasets into memory. Use streaming readers (`stream.Transform`, Python generators) with fixed buffer limits ($\le 10,000$ records).
2. **Backpressure Compliance**: Pipeline consumers must signal upstream producers to pause when ingestion queues reach high-water marks.
3. **Pure & Deterministic Transformations**: Given identical input rows, transformation logic must produce bit-for-bit identical output rows.
4. **Idempotent Loading via Upsert**: Bulk database insertions must utilize `ON CONFLICT (natural_key) DO UPDATE` to prevent duplicate record corruption.
5. **Dead-Letter Queue (DLQ) Quarantine**: Malformed or unparseable records must be routed to a quarantine DLQ (QStash / Kafka DLQ) without crashing the primary pipeline execution.

---

## 🔬 The 4-Phase Streaming ETL Pipeline

### Phase 1: Streaming Extraction with Backpressure
```typescript
import { createReadStream } from 'fs';
import { pipeline } from 'stream/promises';
import { Transform } from 'stream';
import csvParser from 'csv-parser';

export async function processDataPipeline(filePath: string) {
  let batch: any[] = [];
  const BATCH_SIZE = 5000;

  const transformer = new Transform({
    objectMode: true,
    async transform(chunk, encoding, callback) {
      batch.push(chunk);
      if (batch.length >= BATCH_SIZE) {
        await flushBatch(batch);
        batch = [];
      }
      callback();
    },
    async flush(callback) {
      if (batch.length > 0) await flushBatch(batch);
      callback();
    }
  });

  await pipeline(createReadStream(filePath), csvParser(), transformer);
}
```

### Phase 2: Transactional Batch Upsert
```sql
INSERT INTO transactions (id, user_id, amount_in_cents, status, created_at)
VALUES 
  ($1, $2, $3, $4, $5),
  ($6, $7, $8, $9, $10)
ON CONFLICT (id) 
DO UPDATE SET 
  status = EXCLUDED.status,
  updated_at = now();
```

### Phase 3: Dead-Letter Queue (DLQ) Logging
- Route rows failing schema validation directly to an isolated table `pipeline_quarantine_dlq` containing `raw_payload`, `error_reason`, `source_file`, and `quarantined_at`.
