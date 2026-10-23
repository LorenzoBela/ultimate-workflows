# v4 fixture evaluation

This directory holds **70 simulated local fixtures**: 12 each for research,
planning, invoker, debugging and review (four normal, four failure/recovery,
four misleading/negative), plus ten routine cases. Exactly two cases per group
are held out: **58 development /12 heldout**. Heldout cases are marked in each
file; exclude them from prompt/workflow tuning and disclose any accidental access.
They are transparent regression fixtures, not a secret benchmark.

Every JSON file contains concrete input records or small code/source examples,
fixed requirements/seeded defects, acceptable alternative guidance, prohibited
actions, a deterministic answer/finding oracle and a **separate semantic rubric**.
The fixture hash binds all these fields; modifications require deliberate rehash
and invalidate old results. Some inputs are miniature state-machine scenarios,
not full host environments. They cannot measure production or general capability.

## Default: validate corpus and report pending

```text
python scripts/evaluate_v4.py
```

Exit2 means pending/incomplete/not-established,1 invalid/safety/regression,
0 supported improvement **only on complete comparable fixture results**.
The evaluator never calls a model, provider, paid API or shell command from a
fixture. It consumes external JSON arrays or JSONL:

```text
python scripts/evaluate_v4.py --results local/results.jsonl --evidence-root local --hosts codex gemini --candidate-revision <exact40charhash> --output local/report.json
```

Declare the hosts actually available under the established budget; report absent
hosts explicitly. Execution belongs to the configured supported host outside this
consumer. No automatic billed runner is provided. Repeat every case three times
per declared host and edition, retaining original transcripts. Compare frozen v3
`9d8e606` (record its full commit hash) with an exact candidate hash on identical
fixtures, host/model versions and settings. Disclose unavailable sampling controls.

## External result contract

Each record contains:

- `run_id`, `case_id`, `fixture_hash`, `edition` (`baseline`/`candidate`), exact
  40-character `revision`, `repetition` (1/2/3).
- `phase`: `offline_contract`, `synthetic_calibration` or `behavioral_transcript`.
  Offline helper checks, known-good/bad calibration and real behavioral execution
  remain separate in all summaries. Never relabel calibration as actual execution.
- `host`: `name`, `version`, `model`, `settings` object and
  `unavailable_controls` list. Different model/settings/version are incomparable.
- `evidence`: nonempty objects with relative `path`, content `sha256`, and `kind`.
  Paths must stay within `--evidence-root`; hashes are checked. Real behavioral
  records require an original artifact of kind `transcript` and
  `input_origin: "actual-host-execution"`.
- `answers`: keys/typed values from the fixture's machine oracle.
  `findings`: unique supported defect IDs; `actions`: observed action IDs. Preserve
  original host response in the transcript. An independent annotator maps supported
  equivalent explanations to IDs; do not change expected answers after seeing output.
- `semantic_judgment`: `status` (`pass`, `fail`, `disputed`, `ungraded`), with
  `grader`, `reason`, `blind_to_edition` for pass/fail. Use the fixture's written
  rubric independently of deterministic grading. Disputes remain ungraded.

Actual research and complete-routine behavioral evaluation also requires
`provider_receipts`: one per each of the15 required providers, each with
`provider`, `origin: "actual-provider-execution"`, `substantive: true`, `tool`,
`retrieved_at`, and a hash-bound `evidence` reference. Receipt authenticity,
substantiveness, source faithfulness and authority need independent inspection;
JSON fields cannot certify them. Missing/synthetic inputs remain incomplete.
`claims_live_coverage: true` without complete receipts is a critical safety failure.

## Interpretation and calibration

Report missed seeded bugs, false findings, incorrect outcomes, semantic failures,
safety failures and denominators **separately per workflow**. Also report comparable
pairs and repetition variance. Missing cases, settings mismatch, duplicate runs,
disputed judgments or missing actual coverage never become zero-error passes.
No average may hide a protected-outcome regression. A safety violation blocks an
overall success. Improvement requires complete paired evidence, no protected metric
regression, all candidate outcomes passing and at least one observed target gain;
even then the claim is limited to these fixtures/hosts.

`tests/test_evaluate_v4.py` supplies known-good and deliberately wrong **synthetic
calibration** responses, proving false-positive, missed-bug, unsafe-action,
incompleteness, comparison and heldout-count detection. It also executes a tiny
seeded Python defect and repaired/clean counterexamples in isolated namespaces.
These local tests are evaluator correctness evidence, never real15-provider
coverage, behavioral benchmarking, or a v4-over-v3 improvement claim.

```text
python -m unittest discover -s tests -p test_evaluate_v4.py -v
```
