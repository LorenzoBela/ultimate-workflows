---
name: ultimate-refactoring-workflow
description: >
  Master workflow for refactoring and code cleanup. Guides the systematic simplification
  of codebases, dependency reduction, YAGNI enforcement, and design token synchronization.
  Triggers on "ultimate refactoring workflow", "/ultimate-refactoring-workflow", or when
  refactoring or restructuring code.
argument-hint: "[target-component | refactor-goal]"
---

# Ultimate Refactoring Workflow

This workflow guides refactoring to simplify codebases, remove technical debt, enforce modularity, and align with design systems without changing runtime behavior.

---

## The 4-Phase Refactoring Pipeline

### Phase 1: Technical Debt & Bloat Scan
*   **Sub-skills:** `ponytail-audit`, `ponytail-debt`, `ponytail`, `kaizen`
*   **Action:**
    1. Scan the target codebase for code smells: excessive nesting, high cyclomatic complexity, circular dependencies, and duplicate logic.
    2. Collect and review all `ponytail:` comments in the target files to understand what shortcuts were previously deferred.
    3. Generate a ranked list of refactoring opportunities, placing the largest line/dependency reductions at the top.
    4. Apply `kaizen` continuous improvement principles for systematic debt reduction prioritization.

### Phase 2: Refactoring Planning
*   **Sub-skills:** `superpowers-plan`, `sequential-thinking/sequentialthinking`, `concise-planning`
*   **Action:**
    1. Define the goal, constraints (behavior preservation), and verification checks (existing unit/integration test runs).
    2. Map out refactoring steps (each taking 2–10 minutes) using `sequentialthinking` to verify that no structural breaks occur.
    3. **Ensure a safety harness:** If unit tests do not cover the target logic, write a baseline test before modifying the implementation.
    4. Use `concise-planning` for atomic refactoring checklist generation.

### Phase 3: Incremental Refactoring (TDD/Refactor)
*   **Sub-skills:** `superpowers-tdd`, `ponytail`, `vercel-composition-patterns`, `lint-and-validate`
*   **Action:**
    1. Implement refactoring steps one by one. Run verification tests after each step.
    2. Enforce YAGNI: delete dead flags, inline single-use wrapper classes, and consolidate duplicate helpers.
    3. Replace custom algorithms with standard library or native API equivalents where applicable.
    4. Apply `vercel-composition-patterns` for React component refactoring (compound components, render props, context providers).
    5. Run `lint-and-validate` after each refactoring step to ensure zero regressions.

### Phase 4: Token & Contract Synchronization
*   **Sub-skills:** `ckm:design-system`, `ckm:brand`, `ckm:ui-styling`, `ui-ux-pro-max`, `theme-factory`
*   **Action:**
    1. If refactoring UI/UX components, sync styling variables with `assets/design-tokens.css`.
    2. Ensure clean separation of concerns: controllers should not contain business logic; service layers must remain free of HTTP types.
    3. Apply `ckm:design-system` three-layer token architecture for design token consistency.
    4. Use `theme-factory` for rapid theme application after token restructuring.
    5. Verify brand alignment using `ckm:brand` guidelines.

---

## Cross-Cutting Concerns
*   **Review:** Use `superpowers-review`, `caveman-review`, and `ponytail-review` for post-refactoring code audit.
*   **Research:** Use `tavily-search` and `context7/get-library-docs` for discovering standard library replacements.
*   **Memory:** Use `memory` MCP to persist refactoring decisions and debt reduction progress.
*   **Testing:** Use `ultimate-testing-workflow` for comprehensive post-refactoring test coverage.
*   **Documentation:** Update `ultimate-documentation-workflow` artifacts after significant structural changes.
