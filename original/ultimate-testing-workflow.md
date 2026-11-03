---
name: ultimate-testing-workflow
description: "Choose regression, integration, concurrency, browser and other tests according to the actual failure and project tooling. Verify meaningful outcomes and report evidence limits."
argument-hint: "[test-suite | mock-payload | e2e-plan | --mutation | --fuzz | --e2e]"
---

# Test and verification workflow

Identify the behavior at risk, affected contracts, available runners, baseline and required checks. Choose the smallest set that can distinguish a broken implementation from a correct one. Preserve test and infrastructure failures as separate outcomes.

| Risk | Check |
|---|---|
| Specific regression or boundary | Exercise the public path with the failing case and relevant neighbors. Compare against baseline when feasible. |
| Contract or data migration | Exercise representative callers and persisted state, including mixed versions, partial failure and restart where relevant. |
| Concurrent or retried mutation | Synchronize overlapping requests or inject the retry condition. Inspect persisted effects and reconciliation, including duplicate and changed-payload cases. |
| Browser or accessibility | Use representative user journeys and viewport/device coverage. Check focus, keyboard and other applicable manual criteria alongside automation. |
| Many valid input combinations or weak assertions | Use property or mutation testing if it answers a material question and fits the project. Apply configured thresholds and inspect equivalent, uncovered and timed-out mutants. |

Use existing runners and representative fixtures. Choose seams where they preserve the relevant behavior and verify integration separately when mocked. A rollback fixture works only if tested operations share the transaction; otherwise isolate worker databases or schemas. Keep resource ownership explicit and validate cleanup independently. Synchronize on observable events rather than fixed sleeps. Record intermittent outcomes and give quarantined tests an owner and expiry.

Report exact commands, target, pass/fail/unrun checks and baseline issues. Verify what matters, such as actual side-effect counts, rather than substituting coverage percentages or matching response IDs.

## Role and handoffs

**Verification engineer.** Own outcome assertions and failure coverage. Use [ultimate-review-workflow](../ultimate-review-workflow/SKILL.md) and [ultimate-debugging-workflow](../ultimate-debugging-workflow/SKILL.md) when they own the next decision or check, and return the result and evidence to the task owner. Use the [workflow organization](../ultimate-project-workflow/resources/ultimate-organization/role-map.md) for cross-specialty work.

## Representative acceptance case

Run a baseline regression and inject a duplicate side effect. The same suite must verify normal behavior and fail on the injected duplicate by checking persisted state.
