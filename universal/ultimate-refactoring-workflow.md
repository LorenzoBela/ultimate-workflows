---
name: ultimate-refactoring-workflow
description: >
  Flawless 10/10 Master Workflow for refactoring, debt eradication, Strangler Fig migrations,
  Mikado dependency graphs, Characterization / Golden Master safety harnesses, and AST code simplification.
  Triggers on "ultimate refactoring workflow", "/ultimate-refactoring-workflow", or when
  refactoring or restructuring code.
argument-hint: "[target-component | refactor-goal | --strangler | --mikado | --golden-master]"
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

# Ultimate Refactoring & Architecture Modernization Workflow (10/10 Master Engine)

This workflow guides the structured refactoring of legacy codebases, the eradication of technical debt, the application of the Mikado Method and Strangler Fig patterns, and zero-regression Characterization Testing.

```
                                      [LEGACY COMPONENT / DEBT TARGET]
                                                     │
                          ┌──────────────────────────┴──────────────────────────┐
                          ▼                                                     ▼
              [PHASE 1: CHARACTERIZATION & GOLDEN HARNESS]          [PHASE 2: MIKADO DEPENDENCY GRAPH]
              ├─ Snapshot Current Inputs/Outputs                    ├─ Graph Prerequisites (DAG Tree)
              ├─ Pin Baseline Behavior Tests                        ├─ Revert on Structural Blocker
              └─ Cyclomatic Complexity Audit (CC <= 10)             └─ Incremental Micro-Refactoring Step
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: STRANGLER FIG ARCHITECTURE REPLACEMENT             │
        │  • Introduce Modern Adapter • Route 1% -> 50% -> 100% Traffic • Decommission│
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: TOKEN & DESIGN SYSTEM ALIGNMENT]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🎨 TOKENS    │           │ ✂️ YAGNI PR  │           │ 🎯 0 REGRESS │
            │ CSS Variables│           │ Delete Dead  │           │ Full Tests Ok│
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Refactoring

1. **Never Refactor Without a Golden Safety Harness**: Untested legacy code must have Characterization Tests (Golden Master snapshots) recorded *before* editing source lines.
2. **Behavioral Invariance**: Refactoring modifies internal software structure without altering external observable behavior.
3. **The Mikado Rule**: If a refactoring change breaks existing architecture dependencies, immediately `git revert` and record the missing prerequisite as a child leaf in the Mikado graph.
4. **Complexity Limit (Cyclomatic Complexity $\le 10$)**: No refactored function may exceed cyclomatic complexity 10 or nesting depth 3.
5. **Delete Dead Code Aggressively**: Dead feature flags, unused helper classes, and commented-out code blocks must be deleted, not preserved.

---

## 🔬 The 4-Phase Refactoring Pipeline

### Phase 1: Characterization Testing (Golden Master)
```typescript
// Record baseline behavior of legacy calculation
test('Characterization Test: PricingEngine returns identical output for 100 sample vectors', () => {
  const vectors = loadRecordedProductionVectors();
  for (const input of vectors) {
    const output = legacyPricingEngine(input);
    expect(refactoredPricingEngine(input)).toEqual(output);
  }
});
```

### Phase 2: The Mikado Method DAG
1. Set top-level goal (e.g. "Replace legacy callback payment processor with typed async service").
2. Try naive edit $\rightarrow$ If compilation or tests fail due to dependency $X$, **revert edit** and add "Decouple dependency $X$" as a sub-leaf.
3. Solve leaf nodes first in atomic, committed increments.

### Phase 3: Strangler Fig Migration Pattern
- Wrap legacy component with a Router/Adapter interface.
- Implement modern engine alongside legacy engine.
- Gradually route live traffic to the modern engine until the legacy component is completely stranded, then delete the legacy implementation.

### Phase 4: Token & Contract Cleanliness
- Eliminate ad-hoc magic numbers/colors; bind all visual styles to design tokens (`var(--color-...)`).
- Verify all TypeScript types compile without `any`.
