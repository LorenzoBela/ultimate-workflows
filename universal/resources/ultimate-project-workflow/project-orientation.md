# Project orientation and evidence-driven routing

The owner must apply this guide for an unfamiliar codebase, a feature spanning boundaries, a consequential unknown, or resumption after relevant inputs change. Keep the resulting brief inside the existing project record or task context. Read the sections that resolve the next decision.

## Inspect sources by the question they can answer

| Question | Inspect relevant sources | Establish |
|---|---|---|
| What does the user need? | Request, accepted requirements, current artifacts and supplied examples | Observable outcome, fixed constraints, existing authority and acceptance checks |
| Which local rules apply? | Applicable project instructions, contribution guidance and actual working state | Scope, allowed commands, user edits, branch/revision and task-owned resources |
| What runs here? | Manifests, lockfiles, build scripts, configuration references and supported host capabilities | Actual stack and versions, executable checks and required environment; inspect names and structure without dumping secret values |
| How does the behavior work? | Public entry points, actual callers, contracts, data model and representative tests | The affected path, invariants and consumers, including relevant dynamic or externally configured callers |
| What evidence already exists? | Current check receipts, issue reproduction, inspected artifacts and operational observations | Baseline behavior, known failures, applicable results and evidence that became stale |
| What can change safely? | Deployment topology, migration history, external effects, recovery procedures and ownership | Compatibility, uncertainty after partial effects, review/release gates and recovery limits |

Follow pointers through the actual affected flow until its material interfaces and failure boundaries have an owner and a feasible check. Use a repository search or supported graph where useful, corroborating graph freshness. Prefer supported connectors for account-held requirements or documents. Only seek external evidence when the decision requires it.

## Compact working brief

Store facts with a source locator and version or observation time where freshness matters. A brief may be a paragraph for a small task or a short table for coordinated work.

- **Outcome and constraints** — who benefits, expected behavior, non-negotiable values, scope and authority.
- **Current system** — relevant stack, entry points, affected interfaces/data, consumers and baseline.
- **Evidence and uncertainty** — observed facts, proposed assumptions, conflicts, inaccessible sources, and each consequential unknown's owner, impact and next check.
- **Coverage and next action** — requirement or boundary, responsible specialist, usable tool, acceptance check, current dependency and recovery.

A proposed assumption remains distinct from an observed fact. Keep secrets and raw transcripts out of the brief. Link current receipts and source locations instead of repeating entire files.

## Select a complete team for the actual task

Use metadata for broad awareness, then load selected instructions. Review the complete visible skill catalog, including skills outside the Ultimate directory. The [organization map](../ultimate-organization/role-map.md) provides ownership and handoffs for the bundled roles. Host discovery determines which additional skills and tools can actually be used now.

For each material requirement, interface, failure risk and mandatory check, establish ownership and a usable capability. One specialist can cover several needs. Add another when a distinct expertise or independent judgment is needed. Review these boundary prompts where applicable:

- Client behavior, keyboard/focus, loading or recovery need Frontend/UX and a supported browser or device check.
- Identity and object/tenant access need the API/domain owner, relevant Security input and negative authorization cases.
- Persisted invariants, duplicate requests and concurrent updates need Database/Data/API ownership and assertions on actual effects.
- Schema or provider changes need Planning, the domain owner, compatibility checks and a viable release/recovery path.
- Defect investigation needs Debugging and a discriminating reproduction, with Review or Testing when they own the next check.
- Documents, extraction, spreadsheets, devices, editorial work or connected source libraries need their own actual domain skills. Use host artifact and connector capabilities as applicable.

These prompts guide discovery. Select from the current catalog by the outcome and evidence needed. The project owner retains responsibility for gaps between specialties and for integration.

## Decide when to act or investigate more

Proceed with the next bounded action only when the outcome, authority, current inputs, owner and check are clear and its consequential assumptions are supported or explicitly bounded with a safe recovery. If a missing fact could materially change data safety, authorization, compatibility or the chosen contract, obtain discriminating evidence before dependent implementation.

Continue safe independent work while a specific gap is unresolved. Ask the user only for a decision or fact that authorized sources and reasonable reversible assumptions cannot supply. Name the choice, recommendation and concrete consequence.

Expand discovery when a new caller, boundary, failure, conflicting source or unavailable capability appears. Reuse evidence while the relevant scope, versions, artifacts and authority remain applicable. Before repeating a search, state which unresolved question or changed input warrants it. Stop orientation once it supports the next decision and its required check.

On resume, compare the current artifact and environment with the brief, refresh affected facts and rediscover capabilities that are no longer available. Reassign ownership or choose a supported equivalent as needed. Preserve unaffected progress, repair counts and still-current evidence.
