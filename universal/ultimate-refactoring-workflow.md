---
name: ultimate-refactoring-workflow
description: >
  Flawless 10/10 Master Workflow for refactoring, debt eradication, Strangler Fig migrations,
  Mikado dependency graphs, Characterization / Golden Master safety harnesses, and AST code simplification.
  Triggers on "ultimate refactoring workflow", "/ultimate-refactoring-workflow", or when
  refactoring or restructuring code.
argument-hint: "[target-component | refactor-goal | --strangler | --mikado | --golden-master]"
---

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
