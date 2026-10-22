---
name: ultimate-code-cleaner
description: >
  Engineering workflow for AST-guided dead code elimination, unreferenced export pruning,
  circular dependency eradication, architectural boundary enforcement, and safe codebase slimming.
  Integrates Graphify In-Degree analysis, Knip / TypeScript compiler AST diagnostics, Zero-Orphan gates,
  and characterization testing to safely shrink bloated codebases without regressions.
  Triggers on "ultimate code cleaner", "/ultimate-code-cleaner", "clean dead code", "prune unused code",
  "audit bloat", or when optimizing build speed, removing legacy debt, or decoupling monolithic files.
argument-hint: "[target-path | --dry-run | --exports-only | --cycles | --full-purge]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


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

Discover the actual language/build/test commands and record baseline failures. If failures prevent proving safe deletion, stop that deletion and report the missing evidence; unrelated pre-existing failures do not authorize broad fixes or silently block independently verified cleanup.

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
- **Rule**: Zero incoming edges identify a **candidate requiring corroboration**, never deletion authority. Inspect the root/entry-point manifest, runtime loading and public consumers before deciding.
- **Exception**: Entry points (e.g., Next.js `GET`, `POST`, `default` page exports, middleware) have in-degree 0 from the file graph because the Next.js runtime router dispatches them dynamically. **NEVER DELETE FRAMEWORK ENTRY POINTS**.

---

## 🌀 Phase 3: Circular Dependency Eradication

Runtime cycles can cause initialization defects; type-only cycles and safe module cycles are not inherently bugs. Establish a concrete runtime consequence before changing architecture.

### 3.1 Cycle Detection Protocol
Detect strongly connected components or explicit directed cycles using a supported analyzer. A shortest path between two modules alone does not prove a cycle; the command below is exploratory only:
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
   # Run the repository-discovered, authorized smoke check for the affected contract.
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

## Entry-point manifest and safe removal contract

Before pruning, enumerate framework/runtime entry points, package exports and external consumers, CLI/build/test scripts, plugins, reflection/DI registrations, dynamic import patterns, side-effect imports, generated registries, conditional platform exports and configuration references. A graph or static analyzer may miss these roots. Use source search, package/framework configuration and runtime or consumer checks to corroborate every candidate. Knip/compiler diagnostics are optional stack-specific inputs, not proof of external unreachability.

Record each proposed deletion, evidence searched, explicit root exclusions, actual callers and uncertainty. Preserve uncertain/public interfaces until a consumer or compatibility check resolves the risk. Use dry-run inventory by default for broad purges; a requested cleanup authorizes only supported removals, not unrelated modernization. Compare baseline and post-change checks, preserve unrelated edits, and inspect the final diff. Graph node/LOC reduction is bookkeeping, not a quality score.

Acceptance fixtures: externally consumed export, dynamically loaded plugin and side-effect registration survive; a truly unused private helper is removable with evidence; runtime-cycle detection reports the complete cycle and distinguishes type-only edges. Report actual tests and unrun checks rather than filling a 100% passing template.
