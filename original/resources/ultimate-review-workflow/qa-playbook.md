# Risk-based QA and release review

Use for a consequential feature, regression, integrated change, or requested QA assessment. Apply the sections that can reveal a material failure in the actual scope. Use the current review verdict and severity contract.

This guide adapts the pinned source snapshots below. Its test design, coverage and evidence rules govern the local review. Tool commands in upstream snapshots require verification against the installed version and existing user authorization.

## Build the QA basis

Record the review target/revision and environment, accepted behavior and baseline, relevant user roles, data states, changed interfaces, setup/cleanup ownership and available checks. Establish which journeys and negative cases can reveal consequential defects. A small low-risk change can use a focused checklist. A release-affecting change needs a mapping from its material requirements to checks and open risks.

Use a compact coverage row when it helps a handoff:

| Requirement/risk | Scenario and precondition | Action | Expected visible/persisted result | Method and owner | Actual receipt/status |
|---|---|---|---|---|---|
| Referenced ID | Concrete input class, role and state | Public entry point | Assertion that detects the defect | Existing runner or manual method, required/optional | Pending until observed |

## Choose cases that can find a defect

| Technique | Apply when | Example outcome to inspect |
|---|---|---|
| Equivalence classes and boundaries | Validation, parsing, ranges, pagination or rounding changed | Empty, minimal, maximal and just-outside supported inputs have the required result and no unintended effect |
| Decision and role matrix | Behavior depends on permissions, flags or several conditions | Allowed combinations work and denied combinations preserve data |
| State transitions | Login, checkout, editor state or asynchronous workflow changed | Retry, back/cancel, refresh and re-entry preserve the intended state |
| Failure and concurrency sequence | Side effects, external calls, retries or migrations changed | Duplicate/overlapping requests, dependency outage and interruption have correct persisted effects and recovery |
| Compatibility | Schema, API, generated client or independently deployed consumer changed | Representative old and new consumers still satisfy the declared contract |
| Exploratory charter | A user journey has unknown interaction risks | A bounded session records its mission, data, actions, observations, defects and untested questions |

Choose pairwise combinations only when they address an actual interaction risk. Use full decision coverage where a critical invariant requires it. Keep risk reasoning and remaining gaps visible.

## Separate requirement coverage from implementation quality

First check whether the public behavior satisfies requirements, including reasonable boundary behavior implied by supported inputs and callers. Then assess the implementation and integration for consequences such as authorization bypass, resource leaks, duplicate writes, broken compatibility or unmaintainable failure paths. Record design-level issues separately so they return to planning.

A green suite is limited to its exercised scope. Inspect whether tests assert the actual outcome. A test that checks only HTTP status can miss a forbidden persisted write. A screenshot can miss a broken interaction. Use real integration where needed and existing supported fixtures. Mark mocked providers, unavailable browsers and target-only behavior explicitly.

## Browser and UI evidence

Use the host-supported browser or existing project runner. Inspect the rendered page before choosing locators or actions. Wait on the required visible state or response using supported assertions and bounded waits. Apps with polling or streaming may never become network-idle, so that state is not a universal readiness gate. Fixed sleeps can conceal timing defects.

Exercise the applicable primary journey, visible validation/error recovery, keyboard/focus behavior and role-dependent access. Collect screenshots for visible states and console/network evidence or a trace for relevant failures. Check the resulting persisted state or server effect when the flow mutates data. Mocked UI success alone cannot close an integration requirement.

Record viewport, user role, seeded state, build/revision, runner/browser version and reproducible steps where they matter. Capture traces from before the failure when available. Traces can include credentials and personal data, so use scoped test data, restricted artifacts and necessary retention. Close only sessions and processes owned by the run. Discover installed commands rather than assuming an upstream CLI or helper exists.

## Defect and regression handoff

For a supported finding, provide the current location, environment/preconditions, minimal steps or exact command, expected versus actual behavior, user/data consequence, evidence locator and smallest corrective direction. Keep impact severity separate from scheduling priority. Distinguish new regressions from baseline defects and exploratory observations.

After a repair, rerun the original failure and the relevant neighboring contracts on the integrated revision. Apply required independent closure and existing attempt budgets. A rerun that succeeds intermittently still needs the timing and original failure recorded. Do not lower the assertion to hide a product failure.

## Exit assessment

Report the existing typed verdict with actual coverage, executed/failed/unrun checks, open findings and residual risks. For mandatory missing evidence, name the gate, owner and next action. For nonblocking gaps, state their consequence and follow-up. A code review verdict does not grant merge or release authority.

## Pinned sources and adaptations

- [Superpowers code reviewer](upstream/obra-superpowers/code-reviewer.txt), [verification before completion](upstream/obra-superpowers/verification-before-completion.txt), and [MIT license](upstream/obra-superpowers/LICENSE.txt). Adapted review handoffs, scope, specific findings and fresh verification.
- [Anthropic webapp-testing](upstream/anthropics-skills/webapp-testing.txt) and [Apache-2.0 license](upstream/anthropics-skills/LICENSE.txt). Adapted rendered-state reconnaissance and browser evidence. Fixed delays, unconditional network-idle waits and mandatory Python/browser choices are replaced with host-supported, state-based checks.
- [Microsoft Playwright test debugging](upstream/microsoft-playwright-cli/playwright-tests.txt), [tracing](upstream/microsoft-playwright-cli/tracing.txt), and [Apache-2.0 license](upstream/microsoft-playwright-cli/LICENSE.txt). Adapted reproduction, trace collection and rerunning the failed test. The import installs no browser dependency and makes no external comments.
- [Import manifest](upstream/manifest.json) records exact commits, source paths and hashes. Snapshots preserve upstream text with LF line endings as attribution/audit material, loaded only when investigating the adaptation.

The local workflow retains its own severity, output, authorization and independent-review rules. The imports do not prescribe a model, arbitrary review counts, automatic cleanup or additional approval.
