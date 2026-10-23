# Behavioral benchmark protocol

The v4 upgrade adds a separate [70-case corpus and result contract](../evaluations/v4/README.md)
for research, planning, invoker, debugging, review and their connected routine.
It freezes baseline `9d8e606`, separates 58 development and 12 held-out cases,
and compares three actual repetitions per case/edition/available host. The result
consumer checks artifacts, comparability and per-workflow regressions; it does not
execute agents or providers. Synthetic calibration cannot pass the behavioral
acceptance gate. No measured v4 quality improvement is claimed without those runs.

The older broad corpus below remains a specification set for the other workflows.

`evaluations/scenarios.json` defines 152 base evaluation specifications, four for
each of 38 workflows. These are authored task/oracle specifications, **not executed
benchmark results or a ready-made environment**. Bind each to a realistic domain
fixture, pinned model/runtime/tool versions and a reproducible initial state before
running. Negative routing and untrusted-input templates deliberately remain shared
cross-workflow cases; they do not establish domain coverage by themselves.

Run baseline and candidate on the same fixture, retain traces and actual usage,
repeat trials and keep held-out cases. Grade observed completion, data/work
preservation, unauthorized writes, false success/findings, recovery, required
provider coverage, latency, tool errors and available token/cost records. Record
unknown metrics and skipped checks explicitly. Do not grade by headings, prescribed
phrases or exact tool sequence when alternative correct behavior is possible.

For research, provide actual access to all 15 engines and task-relevant source
fixtures. Synthetic state records only exercise the bookkeeping helper. No reduced
provider mode can receive a complete consensus grade. Compare source dates,
versions, independent provenance and material contradictions, not raw vote count.

The current local regression suite covers specific corrected examples and
packaging/state contracts. It is not this 152-scenario end-to-end benchmark.
Hardware/OTA, electrical, DB/Redis, visual/accessibility and real SDK checks need
the corresponding disposable service, target device or human inspection setup.
