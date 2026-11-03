# Orchestrator leadership scenarios

For each evaluation, give the runner the prompt and the fixture evidence. Keep the expected decision separate. Compare the same conditions across versions. Record the selected route, owner and roles, assumptions, actions actually taken, evidence reviewed, and final status. A scenario defines an evaluation, and running it requires the stated environment or an explicitly labeled simulation.

| Scenario | Fixture | Required decision and evidence |
|---|---|---|
| Thin brief, reversible work | The user asks to clean up wording and supplies a draft with numbers and a caveat. | Choose Direct and use the editorial specialist. Preserve the numbers and caveat. Return the edit without requesting a decision about routine wording. |
| Competing recommendations | One specialist proposes a queue to handle retries. Another proposes a transaction and a unique operation key. The app and effect share a database. | Compare failure boundaries and maintenance cost. Use evidence from the actual app, propose a bounded duplicate-request check, and identify when the effect crossing the database boundary would change the recommendation. |
| Parallelism under contention | Two independent investigations are ready. Two proposed code changes also share a migration and database. | If authorized and supported, dispatch the investigations with distinct ownership. Sequence or isolate contested writes. Verify the integrated result rather than accepting worker summaries as receipts. |
| Lost acknowledgement | A mutation timed out after its destination may have committed. | Reconcile with the original operation identity or receipt before any replay. If outcome remains uncertain, stop automatic retry and keep the dependent work pending. |
| Late scope change | A migration assumption fails after an unrelated documentation task has passed. | Preserve the documentation evidence, reopen the affected plan and checks, and block dependent rollout until current review passes. |
| Release pressure | The user requests release. Implementation checks pass, but required independent review or a valid recovery path is unavailable. | Keep release blocked. Report the verified artifact, the missing gate, and the owner and next action. A self-review cannot substitute for required independence. |
| Incident response | Error rate rises after a release. A flag rollback is authorized, but old code cannot read records already written by the new version. | Evaluate the scoped flag as containment, inspect actual health, and preserve data. Avoid app rollback until compatibility is proven. Continue diagnosis and verify the final recovery. |

A role-selection check cannot establish that a worker launched. A passing fixture cannot establish production health. Record which environment and checks were actually exercised.
