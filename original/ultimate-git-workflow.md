---
name: ultimate-git-workflow
description: >
  Master workflow for version control, branch management, clean staging, conventional
  commits, and pre-release validation.
  Triggers on "ultimate git workflow", "/ultimate-git-workflow", or when staging,
  committing, or pushing changes.
argument-hint: "[commit-message | branch-name]"
---

# Ultimate Git & Release Workflow

This workflow enforces clean version control practices, ensures all commits conform to conventional standards, and runs automated validations before pushing to remote repositories.

---

## The 4-Step Git Pipeline

### Step 1: Pre-Commit Validation
*   **Sub-skills:** `lint-and-validate`, `superpowers-tdd`, `systematic-debugging`
*   **Action:**
    1. Run compilers, builders, and linters (e.g., `npm run build`, `npm run lint`, or custom scripts) to verify the codebase is error-free.
    2. Run the unit and integration test suites.
    3. **No Bad Commits:** Never commit code that breaks compiles, fails linters, or violates test assertions.
    4. Use `systematic-debugging` to resolve any test failures before proceeding.

### Step 2: Atomic Staging
*   **Sub-skills:** `superpowers-review`, `ponytail-review`
*   **Action:**
    1. Run `git status` and `git diff` to review all pending changes.
    2. Stage changes atomically. Group edits by their logical scope (e.g. staging database files separately from UI components). Avoid mass, unrelated "drive-by" staging.
    3. Use `superpowers-review` for severity-rated code review of staged changes.
    4. Apply `ponytail-review` to identify and flag over-engineering before committing.

### Step 3: Conventional Commit (Caveman Commit)
*   **Sub-skills:** `caveman-commit`, `caveman`, `ponytail-caveman`
*   **Action:**
    1. Generate a conventional commit message: `<type>(<scope>): <subject>` (e.g. `feat(auth): add refresh token flow`).
    2. Keep the subject line under 50 characters, starting with a lowercase verb.
    3. Apply **caveman-commit** principles: drop pleasantries, keep sentences ultra-terse, and state "why" in the description only if it is not obvious from the code.
    4. Use `ponytail-caveman` for maximum compression: lazy senior dev code + smart caveman communication.

### Step 4: Branch Management & Remote Push
*   **Sub-skills:** `git-pushing`, `ultimate-deployment-workflow`
*   **MCP Tools:** `memory`
*   **Action:**
    1. Verify you are on the correct branch. Avoid committing directly to `main` or `master` unless explicitly approved.
    2. Push changes safely to the remote branch using `git push` via `git-pushing` skill.
    3. Update the memory graph to track branch states or feature deployment observations.
    4. Coordinate with `ultimate-deployment-workflow` for CI/CD pipeline triggers on push events.

---

## Cross-Cutting Concerns
*   **Research:** Use `tavily-search` for Git workflow best practices and branching strategy documentation.
*   **Monorepo:** Use `ultimate-monorepo-workflow` for multi-package workspace versioning and changeset management.
*   **Security:** Verify no secrets are staged using pre-commit hooks (per `ultimate-security-audit-workflow`).
