---
name: ultimate-code-cleaner
description: >
  Flawless 12/10 Master Workflow for AST-guided dead code elimination, unreferenced export pruning,
  circular dependency eradication, architectural boundary enforcement, and safe codebase slimming.
  Integrates Graphify In-Degree analysis, Knip / TypeScript compiler AST diagnostics, Zero-Orphan gates,
  and characterization testing to safely shrink bloated codebases without regressions.
  Triggers on "ultimate code cleaner", "/ultimate-code-cleaner", "clean dead code", "prune unused code",
  "audit bloat", or when optimizing build speed, removing legacy debt, or decoupling monolithic files.
argument-hint: "[target-path | --dry-run | --exports-only | --cycles | --full-purge]"
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
│                   ULTIMATE CODE CLEANER: AST-DRIVEN DEAD CODE & DEBT ERADICATION                 │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. 🔍 PRE-FLIGHT GRAPH & TYPE AUDIT (Ensure clean tsc compile & fresh graphify index)            │
│ 2. 🎯 ZERO-IN-DEGREE ORPHAN DETECTION (Find unreferenced exports, functions, and interfaces)     │
│ 3. 🌀 CIRCULAR DEPENDENCY IDENTIFICATION (Detect import cycles: A ➔ B ➔ A)                      │
│ 4. 🏛️ ARCHITECTURAL BOUNDARY ENFORCEMENT (Forbid utility ➔ route or UI ➔ direct DB imports)       │
│ 5. 🛡️ CHARACTERIZATION SAFETY HARNESS (Pin critical routes with snapshot tests before deletion) │
│ 6. ✂️ SURGICAL PRUNING & AST REFACTORING (Eradicate dead blocks with minimal diff blast-radius)  │
│ 7. 🧪 COMPILER & TEST SUITE VERIFICATION (Zero tsc errors & 100% passing test baseline)          │
│ 8. 🔄 POST-CLEANUP GRAPH SYNCHRONIZATION (`graphify update .` to confirm degree reduction)       │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 Phase 1: Pre-Flight Environment & Graph Verification

Before touching or deleting any line of code, establish an unshakeable ground-truth safety baseline:

### 1.1 Ground Truth Baseline Check
```powershell
# 1. Verify clean TypeScript compilation (must exit with code 0)
npx tsc --noEmit

# 2. Verify Graphify AST index freshness
graphify update .
```

If TypeScript compilation fails, **ABORT DEAD CODE CLEANING IMMEDIATELY**. Existing type errors must be fixed first before pruning unused code.

---

## 🎯 Phase 2: Zero-In-Degree Orphan Detection (Dead Code Hunting)

Dead code wastes memory, bloats bundle sizes, and confuses developers and AI models. We classify dead code into three distinct severity tiers:

### 2.1 The Three Tiers of Code Rot
1. **Tier 1: Completely Orphaned Files (In-Degree = 0)**
   - Entire files in `src/` or `lib/` that are never imported by any route, component, or test.
   - *Detection*: Query Graphify for file nodes with zero incoming `imports` or `imports_from` edges.
2. **Tier 2: Unused Named Exports (Exported-Unused)**
   - Functions, types, or constants marked `export` that are never imported outside their defining file.
   - *Action*: Demote to private file-scope or delete entirely if unused internally.
3. **Tier 3: Dead Discontinued Service Callers**
   - Leftover stub methods or fallback branches referencing deprecated services (e.g. `vehicle_daily_rollups`, discontinued rollups).

### 2.2 Graphify Orphan Inspection Protocol
```powershell
# Query Graphify to identify isolated nodes and low-degree remnants
# Inspect graphify-out/GRAPH_REPORT.md under Community Hubs and God Nodes
Get-Content "graphify-out/GRAPH_REPORT.md" -Head 100
```

### 2.3 AST-Level Symbol Verification
For any candidate dead symbol (e.g. `OldServiceFunction`):
```powershell
graphify explain "OldServiceFunction"
```
- **Rule**: If `Degree == 1` (only contains itself) and incoming edges == 0, mark as **SAFE FOR PRUNING**.
- **Exception**: Entry points (e.g., Next.js `GET`, `POST`, `default` page exports, middleware) have in-degree 0 from the file graph because the Next.js runtime router dispatches them dynamically. **NEVER DELETE FRAMEWORK ENTRY POINTS**.

---

## 🌀 Phase 3: Circular Dependency Eradication

Circular dependencies (`A ➔ B ➔ C ➔ A`) cause runtime `undefined` imports, bundler de-optimizations, and memory leaks.

### 3.1 Cycle Detection Protocol
Run Graphify path traversal to detect loop closures:
```powershell
# Trace cycles between suspect architectural hubs
graphify path "src/app/api/reports/client/data/route.ts" "src/lib/telematics/historical-job-engine.ts"
```

### 3.2 Cycle Resolution Strategies
1. **Extract Shared Types / Interfaces**:
   - Move shared TypeScript interfaces (e.g. `VehicleRecord`, `DateRangePeriod`) into a dedicated leaf file (`src/types/telematics.ts`).
2. **Dependency Inversion**:
   - Make the lower-level module accept callbacks or interfaces rather than importing higher-level route handlers.

---

## 🏛️ Phase 4: Architectural Boundary Enforcement

Enforce strict architectural layering across Next.js and backend services:

```
┌─────────────────────────────────────────────────────────┐
│  Presentation Layer: UI Components (`src/components/*`) │
└───────────────────────────┬─────────────────────────────┘
                            │ Allowed: imports hooks & types
                            ▼
┌─────────────────────────────────────────────────────────┐
│  API / Route Handlers: Controllers (`src/app/api/*`)    │
└───────────────────────────┬─────────────────────────────┘
                            │ Allowed: imports domain services
                            ▼
┌─────────────────────────────────────────────────────────┐
│  Domain Service Layer: Business Logic (`src/lib/*`)     │
└───────────────────────────┬─────────────────────────────┘
                            │ Allowed: imports database & SDKs
                            ▼
┌─────────────────────────────────────────────────────────┐
│  Infrastructure Layer: Database / Cache (`prisma`, Redis)│
└─────────────────────────────────────────────────────────┘
```

### 4.1 Boundary Invariants:
- **FORBIDDEN**: UI components directly importing `prisma` or server database clients.
- **FORBIDDEN**: Infrastructure or utility modules (`src/lib/utils.ts`) importing API route handlers (`src/app/api/*`).
- **FORBIDDEN**: Discontinued tables (e.g. `vehicleDailyRollup`) imported anywhere in active pipelines.

---

## 🛡️ Phase 5: Characterization Safety Harness

Before performing deletions on core modules:

1. **Identify Critical Business Paths**:
   - Check if the file is an active revenue/telematics route (e.g. `/api/reports/client/data`).
2. **Execute Existing Test Harness**:
   ```powershell
   npx vitest run
   ```
3. **Run Live Smoke Test**:
   - If live API routes are affected, run the synthetic audit script:
   ```powershell
   python scratch/audit_all_ranges.py
   ```

---

## ✂️ Phase 6: Surgical Pruning Protocol

When deleting code:

1. **Delete from Leaves to Roots**:
   - Delete unused internal helper functions first.
   - Delete unreferenced interfaces/types second.
   - Delete unused file-level imports third.
2. **Minimal Diff Discipline**:
   - Touch only the lines being pruned. Do not reformat unrelated code in the same commit.
   - Preserve comments explaining non-obvious business logic.

---

## 🧪 Phase 7: Post-Pruning Verification Gate

Immediately following any code deletion:

```powershell
# 1. Verify TypeScript compiles with 0 errors
npx tsc --noEmit

# 2. Run unit and integration tests
npx vitest run

# 3. Synchronize Knowledge Graph (AST delta update)
graphify update .
```

Verify that `graph.json` reflects the deleted nodes and that total node count has decreased cleanly.

---

## 📊 Phase 8: Cleaner Audit Report Format

When completing an `/ultimate-code-cleaner` run, output the standard Cleanliness Scorecard:

```markdown
### 🧹 Ultimate Code Cleaner Scorecard
- **Target Path**: `src/...`
- **Orphan Nodes Removed**: N functions / interfaces
- **Dead Imports Pruned**: N import lines
- **Bytes / LOC Eliminated**: -N lines
- **Circular Dependencies Broken**: N cycles resolved
- **TypeScript Health**: 0 errors (`npx tsc --noEmit` verified)
- **Test Suite Status**: 100% passing
- **Graphify Sync**: Updated (Old: X nodes ➔ New: Y nodes)
```
