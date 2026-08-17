---
name: ultimate-git-workflow
description: >
  Flawless 10/10 Master Workflow for version control, stacked diffs (Meta standard),
  conventional commits (Caveman Commit), interactive rebase sanitization, and pre-release branch protection.
  Triggers on "ultimate git workflow", "/ultimate-git-workflow", or when staging,
  committing, or pushing changes.
argument-hint: "[commit-message | branch-name | --stacked | --rebase | --push]"
---

# Ultimate Git & Release Workflow (10/10 Master Engine)

This workflow enforces surgical version control hygiene, stacked atomic diffs, conventional commit standards, pre-commit validation gates, and clean branch releases.

```
                                      [UNCOMMITTED WORKSPACE CHANGES]
                                                     │
                          ┌──────────────────────────┴──────────────────────────┐
                          ▼                                                     ▼
              [STEP 1: PRE-COMMIT VERIFICATION GATE]                [STEP 2: ATOMIC SCOPE STAGING]
              ├─ Strict TypeScript Compile (tsc)                    ├─ Group by Domain (Contracts -> UI)
              ├─ Linter (ESLint 0 Warnings)                         ├─ Discard Unrelated Edits
              └─ Unit & Integration Tests Pass                      └─ Stacked Diff Decomposition (Meta)
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 STEP 3: CONVENTIONAL COMMIT (CAVEMAN FORMAT)                │
        │  • <type>(<scope>): <subject <=50 chars> • Terse "Why" Body • No Fluff      │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [STEP 4: BRANCH PROTECTION & REMOTE PUSH]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🔀 REBASE    │           │ 🔐 GPG SIGN  │           │ 🚀 GIT PUSH  │
            │ Clean History│           │ Verified Line│           │ Upstream PR  │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Version Control

1. **No Broken Commits on Main**: Every commit must compile cleanly and pass 100% of tests.
2. **One Logical Change Per Commit**: Staging must be atomic. Never combine unrelated UI tweaks, database migrations, and refactorings into a single monolithic commit.
3. **Conventional Commits**: Commit messages must follow `<type>(<scope>): <subject>` where `<type>` is `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `chore`.
4. **Subject Length Limit ($\le 50$ chars)**: Subject must be concise, written in imperative present tense ("add", "fix", not "added", "fixes").
5. **No Secrets in History**: Pre-commit hooks (`gitleaks`) must actively prevent staging `.env` files, API keys, or private certificates.
6. **Stacked Diffs (Meta Standard)**: Large features must be split into sequential, small pull requests ($\sim 35 - 100$ lines) building upon one another.

---

## 🔬 The 4-Step Git Pipeline

### Step 1: Pre-Commit Compilation & Quality Gate
- Run `npx tsc --noEmit` and `npm run test` before staging.
- Ensure 0 errors, 0 unresolved merge conflicts, and 0 linter warnings.

### Step 2: Atomic Staging & Stacked Diffs
- Inspect status via `git status` and `git diff`.
- Stage related files together:
  ```bash
  # Stage contract first
  git add src/types/payment.ts src/schema/payment.prisma
  ```

### Step 3: Conventional Commit (Caveman Commit)
- Format:
  ```text
  feat(billing): enforce idempotency key on charge endpoint
  ```
- If explanation is necessary, keep body ultra-terse:
  ```text
  feat(billing): enforce idempotency key on charge endpoint

  Prevents double-charging customers during transient network retries.
  Caches UUIDv4 keys in Upstash Redis for 24h.
  ```

### Step 4: Rebase & Push
- Rebase on latest upstream main before pushing:
  ```bash
  git fetch origin
  git rebase origin/main
  git push origin feature/my-feature-branch
  ```
