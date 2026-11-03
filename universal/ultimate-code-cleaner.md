---
name: ultimate-code-cleaner
description: "Remove demonstrably unused code or resolve consequential dependency cycles while preserving public, configured and dynamic entry points. Use static analysis as candidate evidence."
argument-hint: "[target-path | --dry-run | --exports-only | --cycles | --full-purge]"
---

# Remove unused code safely

1. Establish the cleanup scope, baseline build/tests and user edits. Map entry points from package exports, framework routing, CLI scripts, external consumers, build/test config, conditional exports, plugins, reflection/DI, dynamic imports, generated registries and side-effect registrations.
2. Gather candidates using the installed compiler, Knip, Graphify or source search. Check tool freshness and coverage. Trace reachability from real entry points and distinguish type-only edges from runtime edges. Preserve uncertain/public candidates until a consumer check resolves the uncertainty. For cycles, capture the complete runtime path and observable consequence before choosing a fix.
3. Record each supported removal with evidence and affected consumers. For a broad cleanup, inspect the inventory before editing. Remove small coherent batches. Keep cycle-breaking and boundary work scoped to the requested consequence.
4. Run relevant baseline-equivalent and consumer checks on the resulting state. Verify a dynamic plugin can still load, external exports resolve, and registration side effects still happen where applicable. Compare actual results and report baseline failures or unrun checks. Restore only the affected batch if verification fails.

A graph with fewer nodes is a bookkeeping result. The acceptance condition is that every removed symbol is demonstrably out of use and protected behaviors still work.

## Role and handoffs

**Code maintenance specialist.** Own evidence-backed removal and runtime reachability. Use [ultimate-graphify-workflow](../ultimate-graphify-workflow/SKILL.md) and [ultimate-refactoring-workflow](../ultimate-refactoring-workflow/SKILL.md) when they own the next decision or check, and return the result and evidence to the task owner. Use the [workflow organization](../ultimate-project-workflow/resources/ultimate-organization/role-map.md) for cross-specialty work.

## Representative acceptance case

Keep a runtime plugin, external export, and side-effect registration while removing a demonstrably unused private helper. Exercise the protected entry points after removal.
