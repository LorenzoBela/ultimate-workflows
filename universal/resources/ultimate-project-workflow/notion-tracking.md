# Strict Notion project tracking

The [Notion specialist](../../../ultimate-notion-workflow/SKILL.md) owns this procedure. Apply on every invocation of the project orchestrator that plans, implements, reviews or changes project work. This is the user's chosen tracking policy. Read-only discovery needed to establish tracking can proceed before a binding exists.

## Resolve the current project

1. Honor an explicitly supplied project URL or previously confirmed project binding. Fetch the actual target and verify its identity before updating it.
2. For repository work, identify the repository actually affected by the task, using its files and remote. An incidental generated chat directory is not the project identity. If a task spans repositories, retain the corresponding project bindings instead of choosing the first folder. Determine the canonical Git remote and consult the private binding registry. Use the bundled helper with an actual installed Python runner:
   - `python resources/ultimate-project-workflow/notion_project.py identify --repo REPO`
   - `python resources/ultimate-project-workflow/notion_project.py resolve --repo REPO`
3. The helper uses origin when present, otherwise a sole remote. Use `--remote NAME` for an explicitly selected alternative. SSH and HTTPS remotes for a GitHub repository share a key. Separate worktrees and branches remain the same project; tasks retain their own run, scope and revision. A monorepo product or fork can require an explicit separate binding.
4. Without a binding, use supported Notion discovery to search the canonical repository URL/key and known project context. Inspect candidate pages and existing collections. Match identity from the repository, existing project metadata or an explicit user selection. A similar title, the current working-directory name, a branch name or a search snippet alone is insufficient.
5. Reuse one clear matching project. If multiple candidates remain plausible, ask the one project-selection question and continue read-only discovery. If none matches, follow the available Notion project-setup skill. Use a private draft when no shared destination has been selected. Create only collections needed for the requested work and preserve other projects and their schemas.

For non-repository work, use the explicitly identified artifact/project and its saved Notion binding. When the project cannot be inferred, resolve it before changing a tracker. Confirm the project URL in the initial progress update for coordinated work so a mistaken match is visible.

## Private binding

The shared registry is `%LOCALAPPDATA%/UltimateWorkflows/notion-projects.json` on Windows. On other hosts it is `$XDG_STATE_HOME/ultimate-workflows/notion-projects.json`, or `~/.local/state/ultimate-workflows/notion-projects.json` when XDG_STATE_HOME is unset. An explicit `--registry` path overrides the default.

Store schema_version 1 with a projects object keyed by canonical repository identity. Each binding contains project_page_id, project_url, tasks_data_source_url, docs_data_source_url and tracking_mode set to strict. Additional stored task/document IDs should reference actual successful writes. Preserve unrelated mappings and replace the file atomically after checking for concurrent changes. Never publish this private registry in the workflow repository.

The helper reads local identity and binding data only. A resolved binding is not proof that Notion is reachable or that a page still belongs to the project. Fetch the project, check tool access when availability is unknown, and inspect the actual data-source schemas before use. Apply current tool restrictions and the connector's Markdown specification.

## Required progress checkpoints

| When | Required Notion state before advancing |
|---|---|
| Intake or resume | Resolve and fetch the correct project; inspect current tasks/plan and reconcile pending updates before new implementation |
| New plan or scope decision | Create or update the plan/spec and affected acceptance criteria; retain its version/hash and task links |
| Before implementation | Reuse or create the actual task record with scope, dependencies, acceptance and owner when known; persist its in-progress status |
| Meaningful state change | Update the task's progress, blocker/next action, review requirement or changed scope before advancing dependent work |
| Verification | Attach actual check results, revision/artifact identity and unrun limits; retain required reviews and findings |
| Commit, publication or delivery | Record the actual commit/PR/artifact and release result when observed; preparation, push and deployment retain separate authority |
| Completion or interruption | Synchronize the final result or checkpoint, open blockers and next action; mark done only after required outcome evidence and tracking writes succeed |

Every changed project deliverable must be linked to a task or existing work item. A Direct change may use one compact task and a short plan/acceptance section. Group shell commands, incidental edits and repeated checks under that work item. A project-related question can update the current work item only when it adds a decision or material evidence. General chat creates no project work.

Reuse existing status vocabulary, relation targets, task/plan IDs and source-of-truth integrations. Do not duplicate a tracker already owned elsewhere; record the authorized Notion mirror and external issue links. Map blocked explicitly to the supported property or record the blocker in the body if no such option exists. Leave unknown people and dates unset.

## Reliable writes and interruption

- The orchestrator is the single writer for project progress. Workers return evidence and proposed updates to it. Delegate tracker writes only with explicit non-overlapping record ownership.
- Use a stable project key, run ID, task/document key and event ID across retries. Store successful object IDs immediately. Find or fetch the matching record before creating a replacement.
- Persist a pending tracking event locally before a state-changing Notion call when it may need recovery. Keep event_id, project_key, target IDs, task/plan revision, intended state, evidence references and pending/applied/conflict status in the existing durable task state or a private outbox.
- On timeout or cancellation, read the original target and reconcile the intended event before replay. Search may lag recent writes, so prefer retained IDs. An uncertain create is not permission for a duplicate.
- Fetch content before a targeted edit unless it is already current in context. Preserve human changes, child pages, relations and other projects. A conflicting newer edit requires a scoped merge or an explicit blocker.
- Use the write result when it establishes success. Fetch to resolve warnings, ambiguity or a later step's exact-state need. Never label a failed or unobserved write synced.
- If access is missing or Notion is unavailable, strict tracking blocks new implementation mutations, release and full completion. Read-only diagnosis, local checkpointing and recovery to a safe boundary can continue. If an operation already happened, preserve its actual result and pending update, then reconcile before the next dependent action. Only an explicit user waiver can temporarily relax tracking; record its scope and expiry.
- On resume, drain pending updates in dependency order before new changes. Keep implementation state and tracking state distinct so a failed update never causes a repeated code/deployment side effect.

## Scope of automation

These checkpoints execute while an agent applies this workflow through available connected tools. They do not establish a background daemon, Git hook or continuous Notion sync. Check the current host, including Gemini, for actual connector access. A shared local binding does not provide credentials or tool support. Retain missing-capability blockers honestly.

Before finishing, report the project/task link and any pending sync gap. The same project identity and saved IDs must be reused on the next run.
