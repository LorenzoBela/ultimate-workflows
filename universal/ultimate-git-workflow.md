---
name: ultimate-git-workflow
description: >
  Workflow for version control, stacked diffs (Meta standard),
  conventional commits (Caveman Commit), interactive rebase sanitization, and pre-release branch protection.
  Triggers on "ultimate git workflow", "/ultimate-git-workflow", or when staging,
  committing, or pushing changes.
argument-hint: "[commit-message | branch-name | --stacked | --rebase | --push]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate Git and Release Workflow

## Inputs and preservation baseline

Identify operation, repo/worktree root, branch/HEAD/upstream, remote, shared/private history and existing edits. Inspect `git status --short`, unstaged/staged diffs and untracked paths. Preserve unrelated tracked, untracked and staged content; never discard it for clean status. Record baseline before checkout/staging/history changes. Existing authorization does not authorize unrelated commits/remote mutations.

## Reviewable changes and checks

1. Follow repository conventions. Keep one logical change with required contract/schema/UI pieces; don't split coherent changes merely for a line-count quota.
2. Inspect changes/staged diff for conflict markers, credentials, generated artifacts and unrelated edits. Use available repository secret scanning without printing secrets.
3. Run stack/change-appropriate existing checks, not `npx tsc` on every repo. Record baseline failures/skips/dependency gaps accurately; filtered success is not all-tests success.
4. Stage explicit paths/reviewed hunks. Preserve already-staged unrelated content without silently including it in the task's commit. Use a reviewed index/worktree isolation method; if separation cannot be verified, stop dependent commit action. Do not default to `git add .`.
5. Inspect `git diff --cached` immediately before commit and verify commit content afterward. Commit only when authorized. Message format/length/signing follow project policy rather than universal numeric requirements.

## Synchronization and conflicts

Verify intended remote/upstream; never assume origin/main. Choose merge/rebase by history ownership/project policy. Do not rewrite shared history without explicit authorization; dirty work does not authorize reset/force-stash.

Before integration record start commit/branch and preservation method. Prefer an isolated worktree for risky operations. Resolve conflicts by understanding both sides and retest behavior. If blocked, matching `rebase --abort`/`merge --abort` may restore an operation this task started; verify baseline restoration. Never automatically abort someone else's existing operation.

Authorized private rebases may require lease-protected push; plain force is not default. Verify remote expectation before rewriting. Never reset unrelated branches for experiment recovery. Reflog does not back up untracked files.

## Push, review and release

Check target remote/branch, final diff and tests before authorized push/PR creation. Use established branch prefix/template. Describe behavior, evidence and limitations. A read-only review does not authorize push.

Release/tag/publication needs authorized scope and compatible data/recovery plan. Record commit/tag/artifact identity. Git revert changes code history; it cannot undo database writes, publication or external effects.

## Completion evidence

Report branch/commit/remote status from actual commands, relevant checks and remaining local changes. Verify unrelated content and staged state survived. Test preservation/conflict recovery in disposable repos when modifying automation; never use the user's dirty repo as a destructive fixture. Claim pushed/signed/clean only when observed.
