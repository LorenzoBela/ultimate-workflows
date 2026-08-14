---
name: ultimate-monorepo-workflow
description: >
  Master workflow for monorepos, multi-package workspaces, shared dependency links,
  and package release pipelines.
  Coordinates Turborepo/Nx settings, pnpm workspaces, semantic versioning, and monorepo builds.
  Triggers on "ultimate monorepo workflow", "/ultimate-monorepo-workflow", or when
  configuring workspaces, link dependencies, or designing monorepo pipeline builds.
argument-hint: "[workspace-setup | package-link | changeset-version]"
---

# Ultimate Monorepo & Multi-Package Workflow

This workflow guides the design, dependency linking, pipeline orchestration, and package publishing rules for multi-package monorepos.

---

## The 4-Phase Monorepo Pipeline

### Phase 1: Workspace Architecture & Package Scoping
*   **Action:**
    1. Organize folders by workspaces (e.g. `apps/` for deployable interfaces, `packages/` for shared libraries, configs, and types).
    2. Configure workspace engines: define package linkages using `package.json` workspaces or `pnpm-workspace.yaml`.
    3. Link shared TypeScript configs (`tsconfig.json`) and linter settings to preserve code quality across sub-packages.
    4. Use `concise-planning` for atomic workspace setup checklists.
    5. Apply `ultimate-architecture-workflow` for domain modeling and bounded context boundaries across packages.

### Phase 2: Pipeline Orchestration (Turborepo / Nx)
*   **Action:**
    1. Define task pipelines in workspace configuration files (e.g. `turbo.json`).
    2. Establish execution dependencies: specify that building an app requires building its linked shared packages first (`"^build"` syntax).
    3. Configure build caches to reuse compile, lint, and test results, minimizing CI build times.
    4. Run Strict Linting & Type Validation across all workspace packages to ensure cross-package type consistency.
    5. Use `Test-Driven Development (Red-Green-Refactor)` for shared package unit testing with isolated test configurations.

### Phase 3: Shared Dependency Management
*   **Action:**
    1. Maintain clean dependency bounds: ensure shared packages declare global utilities and peer dependencies accurately.
    2. Enforce lock-file consistency (using single lock files like `pnpm-lock.yaml` or `yarn.lock` at the root).
    3. Prevent dependency drift: use tools (like `syncpack`) to align package version coordinates across workspaces.
    4. Apply `kaizen` continuous improvement to regularly audit and prune unused cross-package dependencies.
    5. Apply `ponytail` YAGNI principles to prevent speculative shared abstractions.

### Phase 4: Release & Versioning (Changesets / SemVer)
*   **Action:**
    1. Enforce Semantic Versioning (SemVer) rules across all packages.
    2. Manage publishing workflows using Changeset configurations (`.changeset/`). Require changesets for all PR modifications.
    3. Automate npm publishes or Docker image builds triggered by version updates.
    4. Use `Conventional Semantic Git Commits` for terse, conventional commit messages across packages.
    5. Use `git-pushing` for safe remote pushes and `ultimate-deployment-workflow` for CI/CD pipeline integration.

---

## Cross-Cutting Concerns
*   **Research:** Use Web Search and official library documentation for Turborepo/Nx/pnpm workspace documentation.
*   **Memory:** Use Persistent Project Memory / Scratchpad to persist workspace architecture decisions and package relationships.
*   **Documentation:** Use `ultimate-documentation-workflow` for README templates and package API documentation.
*   **Security:** Use `ultimate-security-audit-workflow` for cross-package dependency CVE scanning.
