---
name: ultimate-notebooklm-workflow
description: >
  Organize NotebookLM sources, citation-grounded questions, studio artifacts and resumable research handoffs. Use for requested NotebookLM work when a real connector or documented local client is available.
argument-hint: "[notebook | source-query | studio-artifact]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# NotebookLM sources and grounded research

Use when the user requests NotebookLM and an actual connector or documented local client is available. NotebookLM is a cloud destination: reading local files does not itself authorize uploading them, creating notebooks, extending a corpus or sharing generated material.

## Inputs and preflight

Identify account/profile, target notebook, source-only versus corpus-update scope, source versions, data sensitivity and desired output. Discover the available connector's tools and schemas; if using a CLI, inspect its installed version/help and verify supported commands. Third-party clients differ; this workflow does not prescribe invented universal tool names or response fields.

Verify authentication through the supported client. Keep session cookies/credentials out of logs, source uploads and repository files. On profile conflicts inspect active processes and documented repair steps; never delete the entire auth/profile directory as a default fix. Stop at access challenges and use supported authentication rather than stealth/bypass promises.

## 1. Select notebook and sources

Resolve notebook/account identity using actual listing or provided ID. If multiple matches exist, disambiguate before mutation. Inspect existing source metadata and pending indexing jobs. Create a notebook only within authorized scope; source-only queries do not create or add sources.

For each proposed upload record title, source location, version/date, content hash, sensitivity, authorization and intended destination. Exclude credentials, private customer information and unrelated code/config; redact or obtain necessary scope before uploading. Discover actual size/type limits from the selected product/client rather than universal 10MB/2MB assumptions.

Normalize content only as needed. Preserve headings, tables, page/section locations and links required for citations. Use a source manifest to prevent duplicate uploads and identify stale versions. A URL's changed contents require a freshness check, not trust in its unchanged title.

## 2. Ingest and index when authorized

Use only discovered supported arguments. Persist returned notebook/source/job identifiers immediately; distinguish accepted upload, indexing, ready and failed states. Poll with bounded backoff, deadline and cancellation. On timeout retain job identity and resume polling rather than re-uploading the same source.

For Drive-backed sources verify sync support and whether manual resync is required. Content hash/version changes trigger intentional refresh; do not claim cloud documents automatically synchronize. Record ingestion errors and leave failed sources unsatisfied.

## 3. Grounded questions

Ask the actual notebook query capability with explicit source scope and requested answer format. A tool named “research” may search the web rather than answer from notebook sources; verify its semantics first.

Require material claims to map to source ID/title/version, citation location and supported text. Inspect citations against actual source content. Distinguish exact quotation from paraphrase and respect quotation limits. Citation presence alone does not establish the claim is supported.

For source-only questions, report missing evidence explicitly and offer the needed source/next action without silently expanding the corpus. If external research is authorized, follow `ultimate-research-workflow` with all 15 substantive provider inputs and the rich query floors. Keep external findings distinct from notebook evidence, resolve contradictions and ingest only authorized, reviewed additions. Missing engine input remains incomplete research.

## 4. Studio artifacts

Generate audio, guides or other assets only when requested. Discover supported artifact types/parameters. Persist job ID, artifact type, source set/version and request timestamp; use bounded status polling. A started job is not a finished artifact. On completion verify the returned artifact is accessible through supported preview/download tools; do not invent a download URL or duration.

## 5. Handoff and recovery

Return grounded answer/artifact, source provenance, real citation evidence, indexing/generation status, actual checks and known gaps. Retain source/job manifest and next action for interrupted work. Store only relevant non-sensitive summaries locally or in optional memory with authorization, source versions and uncertainty intact.

Acceptance scenarios: source-only missing-data question causes zero uploads; duplicate ingestion is detected; wrong account is caught before mutation; timeout resumes the same job; stale citation is flagged; malformed or unsupported tool schema fails before execution. A mock client cannot prove a live account or NotebookLM output was verified.
