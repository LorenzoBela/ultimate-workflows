---
name: ultimate-graphify-workflow
description: >
  Flawless 12/10 Master Workflow for AST code property graph intelligence, architectural blast radius analysis,
  multi-hop call-path fault tracing, god-node decomposition, and automatic graph synchronization using Graphify.
  Enforces zero-blind-grep invariants, Leiden community clustering, and subagent context-clamping for large codebases.
  Triggers on "ultimate graphify workflow", "/ultimate-graphify-workflow", "graphify workflow", or when
  analyzing architecture, tracing cross-module dependencies, auditing blast radius, or diagnosing complex multi-file flows.
argument-hint: "[target-symbol | source-target-path | query-concept | --explain | --path | --update | --audit]"
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

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│              ULTIMATE GRAPHIFY WORKFLOW: DETERMINISTIC AST GRAPH INTELLIGENCE PIPELINE           │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. 🔍 GRAPH FRESHNESS & RE-SYNC GATE (Verify HEAD commit matches graph.json metadata)            │
│ 2. 🛡️ ZERO-BLIND-GREP ENFORCEMENT (Strict query/explain/path invocation before file reading)      │
│ 3. 💥 PRE-MODIFICATION BLAST RADIUS MATRIX (Map all upstream callers & downstream sinks)         │
│ 4. 🧭 MULTI-HOP CALL-PATH TRACING (BFS/DFS directed & undirected causal fault traversal)          │
│ 5. 🏛️ GOD-NODE DECOMPOSITION AUDIT (Identify out-of-control hubs with degree > 25)               │
│ 6. 🌐 LEIDEN COMMUNITY ISOLATION (Cluster-bounded subagent worktrees & mutex scheduling)        │
│ 7. 🧪 TEST COVERAGE GAP LOCALIZATION (Intersect graph callers with Vitest/Jest suite boundaries) │
│ 8. 🔄 POST-CHANGE INCREMENTAL SYNCHRONIZATION (Fast 2s delta AST update without LLM cost)        │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 Phase 1: Graph Freshness & Environmental Verification

Before running any graph query or architecture reasoning, verify that the local graph index is not stale:

### 1.1 Freshness Verification Protocol
```powershell
# 1. Compare git HEAD against graph.json built commit
$currentCommit = git rev-parse --short HEAD
$graphReport = Get-Content "graphify-out/GRAPH_REPORT.md" -Head 20
Write-Host "Current Commit: $currentCommit"
```

### 1.2 Automated Delta Resync Gate
If `graphify-out/graph.json` is missing or the current git commit does not match `GRAPH_REPORT.md`, run immediate local AST incremental synchronization:
```powershell
# 0-token, 2-4 second local Tree-sitter AST delta extraction
graphify extract . --code-only
graphify cluster-only .
```

---

## 🛡️ Phase 2: Zero-Blind-Grep Invariant & AST Navigation

Never perform raw global text searches across large enterprise repos when looking for architectural linkages. Raw text search produces false positives from comments, strings, and identically named variables.

### 2.1 Symbol & Concept Resolution (`graphify query`)
Use when locating implementation sites, interfaces, and semantic concepts:
```powershell
# Broad BFS traversal across architectural clusters
graphify query "<concept_or_function_name>"

# Deep DFS trace through a single execution flow
graphify query "<concept_or_function_name>" --dfs

# Bounded token budget for agent subcontexts
graphify query "<concept_or_function_name>" --budget 2000
```

### 2.2 Pre-Modification Blast Radius (`graphify explain`)
**MANDATORY HARD GATE**: Before touching or deleting ANY function, class, type, or service, you MUST run:
```powershell
graphify explain "<TargetSymbol>"
```

#### Verification Criteria:
1. **Degree Analysis**: If `Degree > 15`, classify the target as a **High-Risk Shared Component**.
2. **Upstream Callers (`<-- [imports]` / `<-- [calls]`)**: Enumerate all consumer files. Every consumer must be tested after the edit.
3. **Downstream Dependencies (`--> [calls]` / `--> [method]`)**: Verify that changes do not alter contractual expectations of downstream callees.

---

## 🧭 Phase 3: Multi-Hop Call-Path Fault Tracing (`graphify path`)

When investigating how a request from a frontend component or API route reaches a database, Redis cache, or third-party client:

### 3.1 Directed Path Tracing
Traces explicit execution dependencies:
```powershell
graphify path "src/app/api/reports/client/data/route.ts" "HistoricalJobEngine"
```

### 3.2 Undirected Causal Tracing
If directed tracing yields no direct single-direction edge (e.g. shared state, event brokers, or circular dependencies), trace using the undirected graph:
```powershell
graphify path "src/app/api/reports/client/data/route.ts" "HistoricalJobEngine" --undirected
```

---

## 🏛️ Phase 4: God-Node Architecture Auditing

Enterprise systems suffer from monolithic "God Nodes" (e.g. route files or services with 3,000+ lines and > 30 inbound/outbound edges).

### 4.1 God Node Identification
Inspect `graphify-out/GRAPH_REPORT.md` under **Top God Nodes (Highest Degree)**:
- Nodes with `Degree > 25` require priority refactoring.
- Check community bridges (nodes connecting 3+ distinct Leiden communities).

### 4.2 Safe Decomposition Protocol
1. Run `graphify explain "<GodNode>"` to categorize callers into functional clusters.
2. Extract sub-services along Leiden community boundaries.
3. Replace direct God-Node references with bounded sub-service calls.
4. Run `graphify extract . --code-only` to verify degree reduction.

---

## 🌐 Phase 5: Leiden Community Subagent Partitioning

When orchestrating multi-agent swarms (`ultimate-multi-agent-invoker` or `cavecrew`):

### 5.1 Mutual Exclusion Invariant
- **Rule**: Two parallel subagents CANNOT edit files belonging to the same Leiden Community or sharing a God Node simultaneously.
- **Partitioning Procedure**:
  1. Inspect `graphify-out/graph.json` community clusters.
  2. Subagent A assigned exclusively to Community X (e.g. Telematics Engine).
  3. Subagent B assigned exclusively to Community Y (e.g. Frontend View/Chart Components).
  4. Changes must meet at established interface contracts without concurrent file locks.

---

## 🧪 Phase 6: Test Coverage Gap Analysis

Use the code graph to identify untested code paths:

### 6.1 Finding Untested Sinks
1. Run `graphify explain "<CriticalBusinessFunction>"`.
2. Inspect all `<-- [imports]` connections.
3. If zero inbound edges originate from files matching `*.test.ts`, `*.test.tsx`, or `__tests__/*`, flag as **UNTESTED PRODUCTION INVARIANT**.
4. Generate target regression tests before proceeding with refactoring.

---

## 🔄 Phase 7: Post-Change Incremental Synchronization

Immediately after completing code modifications, commits, or branch rebases:

```powershell
# Fast, local AST re-extraction (0 API cost, takes ~2 seconds)
graphify update .
```

Verify that the terminal reports:
```
[graphify watch] Rebuilt: N nodes, M edges, C communities
graph.json, graph.html and GRAPH_REPORT.md updated in graphify-out
```

---

## 🚦 Phase 8: When NOT to Use Graphify (The Disambiguation Gate)

Do not misuse Graphify for runtime state failures:

| Problem Scenario | Correct Tool | Why Graphify Fails |
| :--- | :--- | :--- |
| **API Payload Mismatches** (e.g. 11 vs 25 vehicles) | `scratch/audit_all_ranges.py` (Live HTTP harness) | AST graphs only see code syntax, not WAN responses. |
| **Stale Distributed Locks** (e.g. Redis lease deadlock) | Redis CLI / Upstash Console | AST graphs cannot read memory contents or TTLs. |
| **Database Pool Starvation** (e.g. Supabase IOPS spike) | `pg_stat_activity` / APM logs | AST graphs cannot measure query runtime or connection count. |
| **Finding Exact Error Strings** | `git grep` / ripgrep | Grep is faster (10ms) for exact verbatim literals. |
| **Refactoring Blast Radius & Upstream Callers** | **GRAPHIFY (`graphify explain`)** | **100% Exact AST relationship traversal.** |
| **Call Chain Mapping Across Architecture** | **GRAPHIFY (`graphify path`)** | **Traces shortest multi-hop route across files.** |

---

## 📊 Summary Output Checklist

When executing `/ultimate-graphify-workflow`, output the structured audit summary:
1. **Target Symbol / Query**: Exact entity analyzed.
2. **Node ID & Source Line**: Exact file and line definition.
3. **Degree & Community Cluster**: Architectural weight and module boundary.
4. **Upstream Callers (Blast Radius)**: All files that consume this entity.
5. **Downstream Callees**: All modules consumed by this entity.
6. **Actionable Risk Assessment**: LOW (degree < 5), MEDIUM (5-15), HIGH (> 15 / God Node).
7. **Post-Op Sync Status**: Verification that `graphify update .` completed.
