# Connected quality routine

Use one task-owned casebook to connect **Research → Plan → Plan Review → Invoke → Debug when needed → Final Code Review**. This upgrades the existing skills and local evidence bookkeeping; it is not an autonomous agent runtime, authorization service, paid API service or truth oracle. Apply existing user scope, stack, authorization and available tool contracts throughout. Local planning/review can use existing evidence without initiating new external research. When external research is invoked, all 15 prescribed inputs and rich-query floors remain mandatory.

## Ownership and linked evidence

Record a stable run ID and schema version, scope, established authority, baseline repository revision, relevant input/content hashes and actual artifacts. Use stable IDs for questions, claims, requirements, assumptions, decisions, interfaces, tasks, hypotheses, experiments, checks, reviews and findings. Links carry IDs/revisions, not just copied descriptions. Keep author/owner/verifier identities distinct where independent verification is required. Do not put credentials, unnecessary personal data or unbounded source/log dumps into the casebook.

The meaningful path is **question → claim/evidence → requirement/assumption → decision → task → check → review/finding**. For example, a retry-safety claim supports a duplicate-request requirement; the requirement and an explicit storage assumption support a deduplication decision; that decision creates an implementation task and a concurrency check. A failing check links back to the requirement and decision, so a design failure can invalidate the right work rather than restarting everything.

Each consequential assumption records its basis, uncertainty, failure consequence and a discriminating experiment. Observed, inferred, failed, unavailable, unverified and superseded evidence remain distinguishable. Empty required fields and syntactically valid links cannot establish semantic support. A local helper checks structure/process receipts; reviewers still judge whether evidence is applicable and checks establish the intended behavior.

## Version binding

The **semantic plan hash** covers structured requirements, decisions, tasks, assumptions, interfaces and acceptance checks. Canonicalize those records; do not hash a Markdown document's formatting as the plan's semantics. Plan review binds to that hash, scope and relevant evidence/input versions. A changed requirement, assumption, interface, decision or check invalidates affected review readiness. A renamed artifact or an old `ready` label is not a current review.

Expected implementation edits and accepted prerequisite outputs advance task/code state while an unchanged plan remains valid. Unrelated repository changes alone do not invalidate everything. Use dependency links and relevant file versions to identify affected evidence. A discovered broken design assumption or changed contract returns the affected decisions/tasks to planning and plan review before their execution resumes.

Code reviews, findings, checks and closure evidence bind to the **exact integrated revision**, plus relevant content hashes for uncommitted changes. A builder's branch or previous passing revision does not prove the integrated result. Recheck fingerprints before dispatch, integration and completion. An affected file changing makes its check stale until rerun or explicitly revalidated with a recorded reason; do not relabel an old execution as a new pass.

## Research output has three separate questions

1. **Collection completeness:** Did all 15 providers actually supply substantive, task-relevant input? Failed/empty/irrelevant/unavailable calls do not count.
2. **Evidence coverage:** For every required question, which applicable claims/sources support, contest or leave its answer unknown? Check original source lineage, dates/versions, independence and disconfirmation. Fifteen engines repeating one old source do not establish 15 corroborations.
3. **Decision readiness:** Are the evidence needed for the next material decisions sufficiently supported, or is there an explicit bounded tradeoff within the user's established requirements? Complete collection may coexist with weak coverage and unready decisions.

Give each provider factual context and distinct questions without declaring the preferred answer proved or showing earlier summaries as authoritative in the independent initial pass. After preserving that pass, investigate material disagreements and actively seek evidence that could refute the leading position. Do not achieve apparent agreement by removing contrary sources. Unknown/contested claims remain visible; a reviewer may accept a bounded product tradeoff only within actual authority. Neither majority vote nor a boolean schema field certifies truth.

The existing provider ledger is [research_state.py](../ultimate-research-workflow/research_state.py). Preserve its checkpoints and public interface; do not maintain a second provider-state ledger in the casebook. Link its run fingerprint, artifacts, claims and readiness assessments into decisions. Research coverage must bind `scope_sha256`, `claims_sha256` and the current report's `evidence_sha256` (canonical latest received provider records). Even changed evidence at the same source URL invalidates old coverage; reassess its semantics instead of merely replacing the recorded hash. Legacy collection/consensus fields describe their documented structural scope; they do not retroactively establish question coverage or product decision readiness.

## Review modes and verdicts

`ultimate-review-workflow` has two explicit modes. Infer plan mode for a supplied implementation plan, code mode for a diff/integrated implementation; ask only when inspection leaves both targets plausibly intended. Review is read-only unless fixes are separately authorized. Reviewing a plan does not begin its implementation. A ready assessment is technical readiness, not deployment/publishing permission or a reason to ask for approval already established in the session.

**Plan review** assesses requirements, consequential assumptions, evidence applicability, interfaces, dependency ordering, ownership/resource conflicts, feasible tools/capabilities, meaningful check oracles and recovery. **Code review** compares the actual integrated behavior with the reviewed plan, discovers candidates, then skeptically validates their preconditions, reachability, impact and safe counterexamples. Revisit a proposed fix at its new revision; do not accept the builder's conclusion as the closure oracle.

Return exactly one current verdict, with precedence **blocked > needs_revision > ready**:

| Verdict | Meaning and next action |
|---|---|
| `ready` | Bound scope/fingerprint is current, mandatory outcomes/checks are supported, no unresolved actionable P0/P1 or consequential unknown remains, and nonblocking follow-ups are visible. |
| `needs_revision` | A remediable internal P0/P1 gap or missing decision can be resolved using available evidence/authority. Return it to the relevant owner; do not dispatch its dependent implementation yet. |
| `blocked` | A required capability/evidence source is unavailable, authority is missing, a consequential tradeoff needs the user, or the applicable repair budget is exhausted. Name the exact gap, preserved work and next action. Independent safe work may continue. |

Findings use consequences, not dramatic wording or diff size:

- **P0:** concrete risk of destructive/unauthorized execution, lost work/data, fabricated verification or violation of a mandatory user requirement.
- **P1:** material correctness/feasibility gap, unsupported consequential assumption, incompatible interface/dependency or a check incapable of establishing a required outcome.
- **P2/P3:** nonblocking improvement or low-consequence issue, with rationale and follow-up ownership where useful.

A risk acceptance names the particular consequence, mitigation and scope. It cannot replace a required provider, waive a hard requirement silently or turn an unrun check into a pass. Reassess the finding after the actual decision; do not close it by changing a label. Seek user input only for genuine missing preferences, consequential tradeoffs or authority that cannot be inferred. Preserve existing authorization and continue independent useful work.

## Dispatch and repair loop

1. Dispatch only from the current `ready` plan review, with valid prerequisite outputs, explicit ownership and available supported capabilities. The packet includes linked decision/requirement/check IDs, scope, plan hash, expected code base, constraints and recovery. Expected implementation changes alone do not require renewed plan review.
2. A task/test failure creates an open finding linked to actual inputs, failing check, affected requirement/decision and code revision. Assign one repair owner and bounded resources. Propagate blockage only through affected dependencies; safe independent tasks may continue.
3. Debugger records competing hypotheses, predicted observations, discriminating experiments and counterevidence, including unsuccessful attempts. Apply only authorized repairs. A design-level cause returns affected decisions/tasks to planning and plan review; record the resulting semantic hash and affected invalidation links.
4. A repair claim becomes `resolved-unverified`. Integrate the actual patch and rerun the original failing check, protected adjacent behavior, impacted contracts and required integration checks against the new integrated revision/hashes.
5. An independent verifier reviews the original requirements, acceptance criteria and raw evidence before the builder's conclusions, checks the current repair, and alone establishes `verified-fixed`. A builder cannot self-close a finding by changing a success field. Other findings may be `non-actionable-with-reason` or `blocked`, with evidence and owner.
6. Final code review inspects the integrated revision and reopens this same loop for new actionable findings. Pre-fix tests cannot prove post-fix closure. Repeat affected planning/review if the new finding changes design.

Default bounds are **three repair attempts per task** and **three final-review repair rounds per run**, additionally limited by established time/cost budgets. The initial final code review and read-only re-review are not repair rounds: the first actual repair after a final review starts a round, shared by tasks repaired for that review; at most three such rounds are permitted. Configure any different bounds explicitly before the run; never expand them silently. An attempt starts when a repair experiment/change is executed, not during read-only diagnosis. Required unavailable infrastructure is `blocked`, not three repeated failed repairs. On exhaustion stop affected dependencies, preserve receipts/patches/checkpoints, and report the next discriminating action. Do not spend paid-provider budget without configured capabilities and the established spend limit.

## Completion, recovery and measurement

Complete only with current final review, satisfied mandatory requirements/checks at the current integrated revision, and no actionable P0/P1 finding remaining. Missing required checks mean incomplete/blocked; optional checks remain explicitly unrun. Report exact scope, plan hash, code revision/content hashes, check/review/finding IDs, observed outcomes, remaining limits and retained recovery paths.

Use atomic serialized casebook updates with conflict detection and actual artifact hashes; preserve old checkpoints and superseded findings rather than rewriting history. A timeout or lost worker does not erase uncertain external effects. Inspect and reconcile them before retrying. This guide does not promise a runtime lock, tool permission boundary or semantic evaluator simply because it describes one.

Structural helper tests, simulated/recorded-provider fixtures and live end-to-end runs are separate evidence categories. A released workflow/helper may have behavioral benchmarking pending; do not claim quality gates or measured uplift from schema tests. Research live evaluation needs all 15 actual substantive inputs; unavailable access remains incomplete. Preserve the grading baseline, expected defects/safe alternatives, forbidden actions and observed results for any evaluation.

## Local casebook CLI and typed records

The packaged helper is [casebook.py](casebook.py). Run these from the installed skill bundle root (the directory containing SKILL.md), or adjust the helper paths for the source checkout. These are **command templates**, not a claim that a run/review/check has occurred. Substitute actual paths, IDs and the integer `N` from the most recent helper output. Inspect/authorize commands before storing or executing them. `record-check` actually launches the defined command; `put`, `review`, `task` and `finding` record local state and do not launch agents, implement changes or grant permission.

```text
python resources/ultimate-quality/casebook.py init --run-dir CASEBOOK_DIR --repo REPO_PATH --run-id RUN_ID --scope SCOPE_TEXT --authorization EXISTING_AUTHORITY --inputs INPUT_PATH --repair-limit 3 --review-limit 3
python resources/ultimate-quality/casebook.py validate --run-dir CASEBOOK_DIR
python resources/ultimate-quality/casebook.py put --run-dir CASEBOOK_DIR --expect-generation N --record RECORD_JSON
python resources/ultimate-quality/casebook.py record-check --run-dir CASEBOOK_DIR --expect-generation N --check-id CHECK_ID --actor VERIFIER_ID
python resources/ultimate-quality/casebook.py review --run-dir CASEBOOK_DIR --expect-generation N --id PLAN_REVIEW_ID --mode plan --actor REVIEWER_ID --verdict ready
python resources/ultimate-quality/casebook.py task --run-dir CASEBOOK_DIR --expect-generation N --id TASK_ID --action dispatch --actor BUILDER_ID
python resources/ultimate-quality/casebook.py task --run-dir CASEBOOK_DIR --expect-generation N --id TASK_ID --action complete --actor BUILDER_ID --evidence RECEIPT_ID
python resources/ultimate-quality/casebook.py review --run-dir CASEBOOK_DIR --expect-generation N --id CODE_REVIEW_ID --mode code --actor REVIEWER_ID --verdict ready --evidence RECEIPT_ID
python resources/ultimate-quality/casebook.py report --run-dir CASEBOOK_DIR
```

Do not copy `ready` without performing the review. Both review modes also accept `needs_revision` or `blocked`; use the actual assessment. `--evidence` accepts one or more **receipt IDs** returned in `.receipt.id` by `record-check`, not check-definition IDs. Each successful mutation advances `generation`; reread it rather than assuming every attempted operation advanced state. Mutations require `--expect-generation`; `validate` and `report` are read-only and do not. Use unique immutable review/finding IDs and preserve old evidence. The helper rejects missing/future revision links and protected transitions rather than migrating checkpoints silently. Historical links remain recorded when a source record advances, with prior typed record snapshots retained in `history[id]` by contiguous revision; ready-plan gates block stale affected links until dependents are explicitly relinked/reviewed. This permits design-feedback replanning without rewriting earlier evidence.

An author-submitted record contains `id`, `type`, `data` and optional `links`, each link shaped `{ "id": "existing-id", "revision": 1 }`. Stored revisions are assigned by the helper; do not submit a fabricated revision or mutate the saved state. Supported types are question, claim, requirement, assumption, decision, interface, task, hypothesis, experiment, check, finding and helper-created review. Create checks before tasks, then requirements that reference them; link existing records with their current exact revision. Keep richer source provenance and semantic arguments in applicable `data` fields/artifacts, not only in IDs.

| Type | Relevant `data` fields |
|---|---|
| check | `argv` nonempty argument strings, `cwd` repo-relative directory, `timeout_seconds` (positive, at most 300), `max_output_bytes` (1..10485760), `mandatory` boolean, `inputs` repo-relative file paths |
| task | `owner`, concrete `recovery`, owned file `paths`, check-definition IDs in `checks`, task IDs in `dependencies` |
| requirement | observable `text`, `hard` boolean, referenced task IDs in `tasks`, check-definition IDs in `checks` |
| assumption | `consequential` boolean, `status` (`supported`, `unknown`, `accepted-bounded`); bounded acceptance also records `decision` and `mitigation` |
| finding | `mode` (`plan`, `code`), `severity` (`P0`..`P3`), concrete `reason`, related check IDs in `checks`, affected `paths`; code findings also require the task ID in `task` |

Illustrative check-definition JSON, to adapt to the actual discovered test runner and real file paths:

```json
{
  "id": "check-retry",
  "type": "check",
  "data": {
    "argv": ["python", "-m", "unittest", "discover", "-s", "tests", "-p", "test_retry.py"],
    "cwd": ".",
    "timeout_seconds": 60,
    "max_output_bytes": 1048576,
    "mandatory": true,
    "inputs": ["src/retry.py", "tests/test_retry.py"]
  },
  "links": []
}
```

A check receipt records actual argv, actor label, time, exit code, bounded stdout/stderr artifacts and hashes, duration, check-definition revision and start/end code stamps. Receipt status is `passed`, `failed`, `timeout`, `output_limit` or `failed_to_start`; overall command output is `recorded` or `incomplete` accordingly. A process `passed` still needs a meaningful assertion oracle and evidence review. No assertion count, tool result or semantic outcome is invented by validating JSON.

On failure, record the finding and task state with their actual links. Task actions are `dispatch`, `repair`, `complete`, `fail` and `block`. `dispatch` starts only a pending task. A failed or blocked task cannot bypass attempt limits through block→dispatch: resumption uses the explicit bounded `repair` action only when an actual repair experiment/change will execute. Read-only diagnosis, capability polling and waiting do not call repair or consume attempts. If required infrastructure is unavailable, keep the task blocked; after restoration, start the justified experiment/change through repair. The helper does not provide a separate infrastructure-only resume state; its narrower transition contract is not an excuse to fabricate attempts or repeatedly retry unavailable tools. Finding actions are `resolved-unverified`, `verified-fixed`, `non-actionable-with-reason` and `blocked`; the latter two require `--reason TEXT`. For example, a repair claim and subsequent independent verification use:

```text
python resources/ultimate-quality/casebook.py finding --run-dir CASEBOOK_DIR --expect-generation N --id FINDING_ID --action resolved-unverified --actor BUILDER_ID
python resources/ultimate-quality/casebook.py finding --run-dir CASEBOOK_DIR --expect-generation N --id FINDING_ID --action verified-fixed --actor VERIFIER_ID --evidence CURRENT_RECEIPT_ID
```

Record original criteria and affected required checks before closure. The final code reviewer and a finding's closing verifier must actually be independent of the builder; different invented actor strings cannot create that independence. The helper cannot authenticate identities, permissions, source truth or check adequacy. Review the current integrated patch and receipts, not merely its transition result.

Exit status **0** means the requested valid operation was recorded/validated (or the report is complete); **2** means incomplete/blocked; **1** means invalid, stale/conflicting or corrupt input. Inspect explicit JSON status and gaps as well as the process exit. Structural `valid` is not end-to-end `complete` or a reviewed `ready`. Preserve locked/interrupted state; never steal an active lock. Inspect actual process ownership and artifacts before an explicitly controlled recovery. Keep raw logs/redacted artifacts until their consumers are done.
