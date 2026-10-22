---
name: ultimate-brainstorm-workflow
description: >
  Explore technical alternatives, constraints, evidence uncertainty, decision sensitivity and bounded design spikes. Use when a feature or architecture choice is genuinely unsettled.
argument-hint: "[decision | design-spike | feature]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Technical brainstorming and decision spikes

Use when meaningful design uncertainty exists. An already-settled implementation does not need invented alternatives. Preserve user constraints and stack; brainstorming does not authorize cloud provisioning or production experiments.

## Inputs

Establish the user outcome, existing behavior, hard constraints, preferences, known source evidence and the decision that needs resolving. State unknowns. If research is invoked, follow `ultimate-research-workflow` with all 15 substantive inputs and its rich context floors; a small brainstorming scope does not waive research coverage.

## Diverge and compare

1. Include the do-nothing/current approach or an incremental extension as a baseline.
2. Generate genuinely different feasible options, normally two to four; explain why an option violates a hard constraint rather than scoring it as merely less attractive.
3. For each viable option record mechanism, integration/operational cost, failure modes, migration/reversibility, performance evidence and unknowns. O(1), fewer dependencies or managed hosting do not establish superiority by themselves.
4. Use a decision matrix only if it clarifies tradeoffs. Choose weights from user priorities, label each score measured/estimated/unknown, and show confidence. Unknown performance remains unknown until an appropriate benchmark.
5. Check sensitivity: vary plausible weights or assumptions and disclose if the winner changes. A narrow numerical lead is not decisive evidence.
6. Recommend an option with explicit accepted tradeoffs, rejected alternatives and the conditions that would change the decision.

## Risk and spike protocol

List credible risks, not a mandatory invented count. For significant risks define a concrete mitigation, owner, observable trigger and recovery. A short pre-mortem can expose missed failures; avoid an elaborate SEV-1 narrative for a routine change.

When one uncertainty decides the outcome, design a bounded spike in an isolated workspace. Record the question, input dataset/environment, time/cost limit and success/failure criterion first. Exercise a realistic integration, capture actual results and limitations, and preserve useful findings. Do not merge exploratory shortcuts without review. Remove only owned disposable code after capturing evidence; preserve user changes and requested artifacts.

## Output and handoff

Deliver goal/constraints, evidence and unknowns, options, decision/rationale, risks, testable acceptance criteria and next implementation steps. Record an ADR when the decision has lasting architectural consequence; a short note is sufficient otherwise. Do not manufacture benchmark gains, testimonial quotes or certainty through numeric scoring.
