---
name: ultimate-research-workflow
description: "Investigate technical questions with primary evidence, comparative source analysis, or an explicitly requested full 15-provider run. Track claim provenance, conflicts and collection gaps."
argument-hint: "[focused | comparative | full]"
---

# Technical research

Choose the smallest mode that satisfies the question and any explicit source requirements.

| Mode | Use when | Completion |
|---|---|---|
| Focused lookup | A version, definition, API behavior, or other narrow fact is at issue. | Cite the applicable authoritative source and identify any version or applicability limitation. One source can suffice. |
| Comparative research | Evaluating alternatives, uncertain behavior, or a consequential decision. | Map each material claim to applicable sources, seek independent corroboration or counterevidence, and expose unresolved conflicts. |
| Full provider run | The user requests the full 15-provider process. | Obtain substantive inputs from every roster entry. List missing inputs and keep the collection incomplete when any are missing. Assess evidence and decision readiness separately. |

## Collect and evaluate

1. State the question, target version/date, operating conditions, required sources and decision at stake. Identify what evidence would change the answer. Use the tools actually available and inspect their schemas.
2. Retrieve underlying sources and cite the relevant location. Prefer primary documentation, specifications, source code or reproducible observations. Search results and model summaries help locate evidence. Keep version, publication or retrieval date, URL and source lineage where relevant.
3. In comparisons, maintain a short claim ledger with support, counterevidence, applicability and status (supported, contested or unknown). Deduplicate mirrors and syndicated copies. Resolve conflicts by comparing source authority, date, version and conditions. Run a bounded experiment if the remaining uncertainty is consequential and the environment supports it.
4. Report the answer and material limitations. For longer runs keep provider attempts and evidence references so work can resume. Honor time, cost and data-sharing constraints. Retry transient failures within a budget and retain partial evidence.

## Explicit full mode

The required IDs are tavily, context7, you, exa, jina, serpdive, linkup, parallel, serpapi, github, firecrawl, crawleo, brightdata, apify and brave. Tailor each query to the provider and the target, include relevant constraints and ask for evidence that could disconfirm the leading claim. The full-run helper retains query word floors for you (150), exa (100), linkup (200), parallel (100) and jina (80). Ordinary modes have no word floors.

An empty, irrelevant or failed result is a gap. Keep the provider status and the useful sources already collected. The number of provider responses measures collection coverage. Assess supported questions and readiness for each decision separately.

## Optional local checkpoints

Use [research_state.py](resources/ultimate-research-workflow/research_state.py) for resumable collection or structured validation. A focused answer can simply cite its source. The helper validates supplied records and has no access to providers.

- Initialize with `init --run-dir DIR --question TEXT --registry FILE --mode focused|comparative|full`. Omitted mode defaults to focused. Registry JSON maps provider IDs to objects with `tool` and `query`. Full mode requires the exact roster. Version 1 checkpoints retain their full-run semantics.
- Record each attempt with `record --run-dir DIR --provider ID --input FILE`. Result fields are `status` (received, empty, failed, unavailable or cancelled), timezone-aware `observed_at` and `artifact`. Received results include `summary` and `sources` with `url`, `evidence` and optional `content_sha256`. Other statuses include `reason`.
- Run `report --run-dir DIR --claims FILE [--coverage FILE --require-ready]`. Claims contain `id`, `text`, `positions` and `review`. Positions match received providers in ordinary modes and the full roster in full mode. Each position records `stance` (support, contradict or insufficient), `rationale` and cited `sources`. Review records `conclusion`, `reasoning` and `disagreement` (resolved or unresolved) for conflicting evidence.
- Coverage binds `scope_sha256`, `claims_sha256` and `evidence_sha256` to the assessed records. Questions contain `id`, `required`, `status`, claim IDs, a freshness assessment with status and rationale, and, for comparative/full runs, a disconfirmation query, outcome and source list. Decisions contain `id`, `rationale` and question IDs. Use the helper's `claims_digest` canonicalization for claims. Report status 2 means the requested structured assessment is incomplete. Review source applicability and unresolved claims yourself.

## Role and handoffs

**Evidence analyst.** Own source applicability and disputed claims. Use [ultimate-planning-workflow](../ultimate-planning-workflow/SKILL.md) and [ultimate-brainstorm-workflow](../ultimate-brainstorm-workflow/SKILL.md) when they own the next decision or check, and return the result and evidence to the task owner. Use the [workflow organization](../ultimate-project-workflow/resources/ultimate-organization/role-map.md) for cross-specialty work.

## Representative acceptance case

Answer a versioned lookup from its primary source. If a second source disagrees, resolve version and applicability or return a contested claim with its decision impact.
