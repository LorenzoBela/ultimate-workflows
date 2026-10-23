---
name: ultimate-debugging-workflow
description: Diagnose reproducible defects, regressions and intermittent incidents using scoped hypotheses, reproduction evidence, safe experiments and verified fixes. Supports production mitigation within existing authorization and optional fault localization, bisection, mutation analysis and parallel investigation.
argument-hint: "[symptom | error | regression-range | incident]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve established authorization. Research requires all 15 prescribed provider inputs.

# Debugging workflow

This is the repair stage of **Research → Plan → Plan Review → Invoke → Debug when needed → Final Code Review**. Apply the [connected quality guide](resources/ultimate-quality/guide.md). Receive a finding linked to its task, requirement/decision, failing check receipt, actual inputs and exact integrated revision/content hashes. Standalone debugging may establish this minimal context from the observed defect; it does not fabricate an already-reviewed implementation plan.

## Hypothesis ledger, design feedback and independent closure

Assign stable hypothesis and experiment IDs. Keep competing explanations, their predicted observations and a check that could refute each. Select the safest bounded experiment that distinguishes causes rather than simply retesting the leading guess. Retain unsuccessful attempts, counterevidence and nondeterministic trial conditions/results. Missing required target/infrastructure is blocked, not a fabricated reproduction or repeated repair.

Classify the supported cause as an implementation defect within the current plan or a design-level failure of an assumption/interface/decision. For design-level failures, link counterevidence to affected planning records, stop dependent dispatch, revise the plan and renew its semantic-hash-bound plan review. An ordinary expected implementation edit does not invalidate the semantic plan; an incompatible contract or broken consequential assumption does. Preserve unrelated valid tasks/evidence.

A repair experiment/change consumes one of the default **three repair attempts per task**; read-only diagnosis does not. Final-review repairs additionally obey the run's **three final-review repair rounds**, under existing time/cost budgets. Limits can be explicitly configured before the run but never silently expanded. On exhaustion retain the patch, receipts, rejected hypotheses and next discriminating action; report blocked for affected work.

A builder's repair claim becomes **resolved-unverified**. After integration, rerun the original failing check, protected adjacent behavior, affected dependencies and mandatory integration checks against the new exact integrated revision and relevant content hashes. An independent verifier/reviewer, given original criteria/raw evidence before builder conclusions, establishes **verified-fixed** or reopens/blocks the finding. Do not self-close through a success field. Pre-fix evidence and a worker-local branch do not establish post-fix integrated correctness.

Use for an observed error, regression, hang, leak, performance defect or intermittent failure. Inputs: reported versus expected behavior, affected revision/environment, reproduction material, available tests/logs, current user edits and authorized scope. Do not turn a diagnosis into an unrelated rewrite or assume production-change authority. Missing reproduction or target access is a stated limitation; useful read-only progress can continue.

## 1. Triage and containment

Identify consequence, affected users/components and evidence retention needs. For an active incident, consult the actual runbook and incident owner. Apply a specific rollback, flag, traffic or rate-limit change only when already authorized and its target, impact and recovery are understood; otherwise prepare the concrete mitigation while continuing safe diagnosis. Do not automatically revert schema/data or discard a dirty checkout.

Record runtime/library versions, configuration differences, exact error, timestamps, recent deployments and relevant trace IDs. Redact credentials and personal data. Heap dumps may contain secrets and require bounded storage/access; CPU profiles are not deterministic replay traces. Use real platform dump/replay formats only on supported targets.

## 2. Reproduce and localize

1. Capture the smallest meaningful symptom reproduction and run it on baseline code. At least one symptom case should fail before the fix and pass after it; boundary/regression cases may already pass and must retain their expectations.
2. Distinguish application failure from fixture, setup, infrastructure and pre-existing test failures. For intermittent behavior record trials, timing and uncertainty; a few retries do not prove absence of a bug.
3. Trace inputs/state through actual callers, asynchronous boundaries and sensitive sinks. Use a fresh graph where supported, corroborated with source/config/runtime evidence; shortest graph paths are hypotheses rather than exact runtime traces.
4. Rank hypotheses with predicted observations and a disconfirming check. Preserve logs/results so changing hypotheses does not erase contrary evidence.

When statistical localization is appropriate, collect **per-test** coverage for passing and failing tests; aggregate coverage alone cannot calculate Ochiai. For element e, score `ef / sqrt((ef+nf)*(ef+ep))`, where ef/ep count failing/passing tests executing it and nf failing tests not executing it. Handle a zero denominator. Treat ranking as correlation, keep source links and expand beyond the initial candidates when evidence disagrees. AST slicing and keyword relevance help navigation, not causal proof.

## 3. Mandatory research coverage when researching

Use the research workflow's engine-specific prompts and current tool schemas for Tavily, Context7, You.com, Exa, Jina, SERPdive, Linkup, Parallel Search, SerpApi, GitHub, Firecrawl, Crawleo, Bright Data, Apify and Brave Search. All 15 substantive task-relevant inputs are required. Failed/empty/irrelevant/unavailable calls do not count. Preserve provider checkpoints, primary evidence and conflicts; missing inputs leave research incomplete. Do not invent a workaround, substitute a provider or reduce query-context requirements to fill the matrix.

## 4. Regression bisection

Use only with verified good/bad endpoints and a runner whose result tracks the actual defect. The Bash example below is a scoped orchestration template; it was designed for an external executable reproduction script and a clean task-owned worktree. Never run it against an existing bisect session or unrelated dirty checkout.

```bash
#!/usr/bin/env bash
# Illustrative orchestration; execute only in a clean, task-owned worktree.
set -euo pipefail
: "${BAD_SHA:?known bad commit required}"
: "${GOOD_SHA:?known good commit required}"
: "${REPRO_RUNNER:?absolute executable script outside the bisected tree required}"
[[ -x "$REPRO_RUNNER" ]] || exit 2
[[ -z "$(git status --porcelain)" ]] || { echo "Preserve dirty work before bisecting" >&2; exit 2; }
[[ ! -e "$(git rev-parse --git-path BISECT_START)" ]] || { echo "Existing bisect session: preserve it" >&2; exit 2; }
initial_head=$(git rev-parse HEAD)
restore_checkout() {
  rc=$?
  trap - EXIT INT TERM
  if ! git bisect reset; then
    echo "Restore failed; original HEAD: $initial_head. Preserve files and recover manually." >&2
    rc=1
  fi
  exit "$rc"
}
trap restore_checkout EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
git bisect start "$BAD_SHA" "$GOOD_SHA"
git bisect run "$REPRO_RUNNER"
# Only inspect the result after git bisect run succeeds.
git show --no-patch --format=fuller refs/bisect/bad
```

Runner contract: **0=good**, **1=reproduced defect**, **125=untestable revision**. Infrastructure failure aborts with a distinct status outside 0–127. Keep the executable runner outside the changing source tree; no child shell can rely on an unexported function. Preserve logs for diagnosis. The exit trap resets the bisect checkout on success, failure and handled interruption; SIGKILL/power loss requires explicit recovery from recorded state. Skipped revisions next to the boundary may leave multiple candidates; do not claim one culprit without resolving that ambiguity. Delta-debug large diffs only in owned experiments and retain a compilable/reproducible predicate.

## 5. Repair and experiment

State the broken invariant, intended replacement, affected contracts and negative constraints before editing. Prefer a minimal correct diff; no arbitrary line quota may remove error handling. Choose normal scoped edits for small reversible fixes or unique task-owned worktrees for risky/competing experiments. Never delete an existing worktree to create a new one.

Delegate only when task authorization and real host capabilities support it. Roles such as reproducer, investigator, builder and independent reviewer are responsibilities, not API names or a mandatory nine-worker launch. Give workers distinct ownership, dependencies, available evidence and attempt/time limits. If a hypothesis repeatedly fails, revisit the invariant/localization rather than blindly patching; preserve incomplete work at budget exhaustion.

An execution record includes scope, baseline revision, dirty-state fingerprint, tool identity, actual command, artifacts, timeout/cancellation, exit status and verification result. Use pending/running/failed/cancelled/unavailable/completed-unverified/verified states. A print-only adapter, exit zero or PASS substring cannot establish verification. No fake orchestration script is supplied here.

## 6. Verify and integrate

Run the symptom reproduction, relevant previously passing contracts and appropriate build/type/lint/integration checks. Keep baseline failures and unrun checks visible. For high-risk boundaries, use supported mutation/property/concurrency/fault-injection tests when meaningful: configure thresholds per project and inspect equivalent, uncovered and timed-out mutants. Mutation score measures test sensitivity, not proof of repair.

Investigate leaks with retained-owner/allocation evidence; deadlocks with actual wait/blocking edges; UI hitches with measured frame-time distributions on the target device/workload. Use the target latency/frame/stack/resource budgets instead of universal 8.33ms or zero-hitch guarantees. Reproduction must demonstrate the reported consequence, not only a mocked implementation detail.

Integrate only the owned patch into the requested branch with supported repository tools and rerun checks on the integrated revision. Before clean teardown, inspect ownership, tracked/untracked/index changes, ancestry and retained logs. Prefer ordinary Git removal; keep dirty or unmerged work and report its location. No forced removal, branch deletion or invented AST merge is an automatic cleanup step.

## Completion and recovery

Report baseline symptom, supported cause/invariant, changed files, exact checks/results and unresolved limits. Material incidents receive a blameless timeline and evidence-supported prevention actions; do not manufacture five organizational causes. Persist useful redacted lessons only to an available authorized notes mechanism. If unresolved, preserve reproduction, hypotheses, checkpoints, owned artifacts and next discriminating test. Do not claim physical/production recovery from host-only verification.
