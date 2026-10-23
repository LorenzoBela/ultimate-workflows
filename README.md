# ⚡ Ultimate Workflows: 38 AI Engineering Workflows

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Workflows: 38](https://img.shields.io/badge/Workflows-38%20Total-brightgreen.svg)](./universal/)
[![Compatibility](https://img.shields.io/badge/Supports-Codex%20%7C%20Cursor%20%7C%20Claude%20Code%20(CC)%20%7C%20Antigravity%20(AGY)%20%7C%20Windsurf%20%7C%20Cline%20%7C%20VS%20Code-orange.svg)](#-one-line-installers)

A suite of **38 engineering workflows** crafted for autonomous AI agents, coding assistants, and pair-programming environments.

Workflow instructions cover scoped execution, domain-specific decisions, evidence, failure recovery, and verification. Runnable examples have targeted checks; device, production-service, visual, and live-provider results require their own evidence.

---

## ⚡ One-Line Installers (Instant Setup)

Install into your current project repository. Commands replace matching workflow files and bundle resources; updates refuse conflicting local customizations:

### Codex (desktop app, CLI, and IDE extension)

**1. Install.** Open a terminal in the project where you want to use the workflows. With Node.js/npm and Git installed, run this in PowerShell, macOS, or Linux:

```sh
npx github:LorenzoBela/ultimate-workflows codex
```

The command installs all 38 universal workflows and their linked resources into the current project. It creates one folder per skill, preserving the workflow's `name` and `description`:

```text
your-project/
└── .agents/
    └── skills/
        ├── ultimate-debugging-workflow/
        │   └── SKILL.md
        ├── ultimate-planning-workflow/
        │   └── SKILL.md
        └── ...
```

**2. Open the project in Codex.** Codex discovers skills in `.agents/skills/`. If newly installed skills do not appear, restart Codex. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

**3. Use a workflow.** Name the skill in your prompt, or use `$` to select it:

```text
Use $ultimate-planning-workflow to plan email sign-in for this project.
```

```text
Use $ultimate-debugging-workflow to investigate why login fails after a refresh.
```

For an explicit parallel run, request `$ultimate-multi-agent-invoker` with a current technically ready plan review. Existing user authorization still governs execution. Installing these files supplies workflow instructions; it does not install the external tools, other skills, or MCP connections referenced by a workflow.

**Updating:** rerun the install command from the same project. It updates files matching their recorded installation hashes. Modified or unowned conflicting files cause an error before any files are written; back up and reconcile them first. Commit `.agents/skills/` if teammates should use the same workflows. Avoid installing duplicate copies at both project and user scope.

**Already cloned this repository?** Run the installer from your target project's terminal using the path to the clone:

```sh
node /path/to/ultimate-workflows/scripts/install.js codex
```

The clone also includes PowerShell and Bash entry points; both use the same Node.js installer. Run either command from the target project, replacing the example path with your clone's location:

```powershell
& 'C:\path\to\ultimate-workflows\scripts\install.ps1' -Target codex
```

```sh
bash /path/to/ultimate-workflows/scripts/install.sh codex
```

---

### 🎯 Cursor IDE (`.cursor/rules/*.mdc`)
```bash
# Node / npx
npx github:LorenzoBela/ultimate-workflows cursor

# Bash (macOS / Linux)
bash /path/to/ultimate-workflows/scripts/install.sh cursor

# PowerShell (Windows)
& 'C:\path\to\ultimate-workflows\scripts\install.ps1' -Target cursor
```

---

### 🟣 Claude Code (`.claude/skills/<name>/SKILL.md`)
```bash
# Node / npx
npx github:LorenzoBela/ultimate-workflows claude

# Bash (macOS / Linux)
bash /path/to/ultimate-workflows/scripts/install.sh claude

# PowerShell (Windows)
& 'C:\path\to\ultimate-workflows\scripts\install.ps1' -Target claude
```

---

### 🚀 Google Antigravity / AGY (`.agent/workflows/`)
```bash
# Node / npx
npx github:LorenzoBela/ultimate-workflows agy

# Bash (macOS / Linux)
bash /path/to/ultimate-workflows/scripts/install.sh agy

# PowerShell (Windows)
& 'C:\path\to\ultimate-workflows\scripts\install.ps1' -Target agy
```

---

### 🌊 Windsurf / Cascade (`.windsurfrules`)
```bash
# Node / npx
npx github:LorenzoBela/ultimate-workflows windsurf

# Bash (macOS / Linux)
bash /path/to/ultimate-workflows/scripts/install.sh windsurf

# PowerShell (Windows)
& 'C:\path\to\ultimate-workflows\scripts\install.ps1' -Target windsurf
```

---

### 🤖 Cline / Roo-Code (`.clinerules`)
```bash
# Node / npx
npx github:LorenzoBela/ultimate-workflows cline

# Bash (macOS / Linux)
bash /path/to/ultimate-workflows/scripts/install.sh cline

# PowerShell (Windows)
& 'C:\path\to\ultimate-workflows\scripts\install.ps1' -Target cline
```

---

### 💻 VS Code / GitHub Copilot (`.github/copilot-instructions.md`)
```bash
# Node / npx
npx github:LorenzoBela/ultimate-workflows copilot

# Bash (macOS / Linux)
bash /path/to/ultimate-workflows/scripts/install.sh copilot

# PowerShell (Windows)
& 'C:\path\to\ultimate-workflows\scripts\install.ps1' -Target copilot
```

---

### 📦 Install All Targets at Once
```bash
npx github:LorenzoBela/ultimate-workflows all
```

Includes Codex's `.agents/skills/<name>/SKILL.md` folders alongside the other IDE targets.

---

## 📑 Table of Contents

- [Codex setup and usage](#codex-desktop-app-cli-and-ide-extension)
- [What Are Ultimate Workflows?](#-what-are-ultimate-workflows)
- [Two Editions: Universal vs. Original](#-two-editions-universal-vs-original)
- [Complete 38-Workflow Catalog](#-complete-38-workflow-catalog)
  - [1. AI & Autonomous Agent Engineering](#1-ai--autonomous-agent-engineering)
  - [2. System Architecture & Technical Planning](#2-system-architecture--technical-planning)
  - [3. Fullstack & Application Engineering](#3-fullstack--application-engineering)
  - [4. Data Systems, Database & Caching](#4-data-systems-database--caching)
  - [5. Hardware, Embedded & IoT Engineering](#5-hardware-embedded--iot-engineering)
  - [6. Quality Assurance, Security, Operations & Debugging](#6-quality-assurance-security-operations--debugging)
  - [7. UX, Automation & Document Intelligence](#7-ux-automation--document-intelligence)
- [Workflow Chaining & Pipelines](#-workflow-chaining--pipelines)
- [Shared quality rules](#shared-quality-rules)
- [License](#-license)

---

## 🧠 What Are Ultimate Workflows?

Standard AI code generation often suffers from "vibecoding": generic UI defaults (such as indigo gradients, uniform `rounded-2xl`, wash-out grey text), unhandled loading/error states, missing accessibility, brittle database queries, and missing edge-case handling.

**Ultimate Workflows solve this by embedding production-grade senior engineering constraints directly into the agent's context window:**

1. **Phased Execution Pipelines:** Every workflow guides the agent through structured phases (Research → Architecture → Implementation → Validation → Review).
2. **Applicable quality targets:** Accessibility requirements, measured performance budgets, existing brand rules and meaningful verification suited to the task.
3. **Concrete quality guidance:** Avoid unsupported boilerplate, preserve established conventions and justify decisions with evidence.
4. **Actionable Checklists:** Concrete pre-flight verification items before declaring code done.

---

## 📦 Two Editions: Universal vs. Original

The `original/` edition is the review surface for Gemini-authored workflow updates. `scripts/build.py` exports the same reviewed instructions and required resources to `universal/`, recording each bundle in `workflow-manifest.json`. Host installations use discoverable skill bundles or flat rule files with adjacent resources. Shared execution rules load from a linked reference. Research's mandatory 15-provider coverage is identical across editions.

```text
ultimate-workflows/
├── universal/    # 🌟 Recommended: Portable adaptations for supported agents/IDEs
├── original/     # Advanced: Includes custom sub-skill links and MCP server hooks
├── scripts/      # Automated multi-IDE installer scripts (Node, Bash, PowerShell)
└── README.md     # Documentation & quickstart index
```

| Edition | Contents | Role |
|---|---|---|
| `original/` | Reviewed instructions and resources | Gemini authoring mirror and review surface |
| `universal/` | Deterministic export of the reviewed bundles | Input to all three installers |
| Installed skill bundle | `SKILL.md` plus linked resources | Codex and Claude Code discovery |
| Installed rule file | Markdown/MDC plus adjacent resources | Cursor, Antigravity, Windsurf, Cline and Copilot |

---

## 📚 Complete 38-Workflow Catalog

### 1. AI & Autonomous Agent Engineering

| Workflow | Universal File | Summary |
| :--- | :---: | :--- |
| **Multi-Agent Invoker** | [`ultimate-multi-agent-invoker.md`](./universal/ultimate-multi-agent-invoker.md) | Use process exit status and structured verification; retain raw logs; remove forced cleanup defaults; enforce ownership/dirty-state checks; connect budgets to actual runtime usage and persist task states. |
| **Agent Development** | [`ultimate-agent-dev-workflow.md`](./universal/ultimate-agent-dev-workflow.md) | Provider-preserving adapters, schema validation, canonical path boundaries, real execution budgets and side-effect control. |
| **Agent Orchestration** | [`ultimate-agent-workflow.md`](./universal/ultimate-agent-workflow.md) | Durable handoffs and versioned memory; configurable deadlines; preserve user artifacts. |
| **NotebookLM Research** | [`ultimate-notebooklm-workflow.md`](./universal/ultimate-notebooklm-workflow.md) | Verify actual connector contracts; source provenance; authorized corpus updates and bounded jobs. |

---

### 2. System Architecture & Technical Planning

| Workflow | Universal File | Summary |
| :--- | :---: | :--- |
| **Graphify Code Intelligence** | [`ultimate-graphify-workflow.md`](./universal/ultimate-graphify-workflow.md) | Source-content freshness, extractor version, uncertain/dynamic edges and reachability corroboration. |
| **System Architecture** | [`ultimate-architecture-workflow.md`](./universal/ultimate-architecture-workflow.md) | Proportionate boundaries; monolith baseline; complete outbox, deduplication and evolution guidance when applicable. |
| **Brainstorming & Scoping** | [`ultimate-brainstorm-workflow.md`](./universal/ultimate-brainstorm-workflow.md) | Include incremental/do-nothing baselines; separate evidence from estimated scores; test sensitivity to assumptions. |
| **Implementation Planning** | [`ultimate-planning-workflow.md`](./universal/ultimate-planning-workflow.md) | Consequence-based planning, explicit assumptions and acceptance criteria, realistic platform constraints and recovery. |
| **Project & Sprint Tracking** | [`ultimate-project-workflow.md`](./universal/ultimate-project-workflow.md) | Portable task ledger with stable IDs, owners, blockers, scope decisions and evidence links. |

---

### 3. Fullstack & Application Engineering

| Workflow | Universal File | Summary |
| :--- | :---: | :--- |
| **API Engineering** | [`ultimate-api-workflow.md`](./universal/ultimate-api-workflow.md) | Request-scoped authorized loaders; explicit ordering and missing-item handling; operation-specific idempotency and concurrency rules. |
| **Frontend Engineering** | [`ultimate-frontend-workflow.md`](./universal/ultimate-frontend-workflow.md) | Framework-aware boundaries, consistent performance metrics, accessible interaction and existing brand preservation. |
| **Fullstack Development** | [`ultimate-fullstack-workflow.md`](./universal/ultimate-fullstack-workflow.md) | Stack-aware vertical slices, transactional idempotency, concurrent/offline conflicts and schema compatibility. |
| **Serverless Platforms** | [`ultimate-serverless-workflow.md`](./universal/ultimate-serverless-workflow.md) | Actual provider limits, production-safe migrations, trusted claims and event redelivery handling. |
| **Monorepo Architecture** | [`ultimate-monorepo-workflow.md`](./universal/ultimate-monorepo-workflow.md) | Correct cache inputs, workspace boundaries, consumer tarball checks and resumable release manifests. |

---

### 4. Data Systems, Database & Caching

| Workflow | Universal File | Summary |
| :--- | :---: | :--- |
| **Caching Architectures** | [`ultimate-caching-workflow.md`](./universal/ultimate-caching-workflow.md) | Unique lock ownership and atomic conditional release; bounded waits and cancellation; documented stale/fallback policy and tenant key scope. |
| **Data Pipelines & ETL** | [`ultimate-data-workflow.md`](./universal/ultimate-data-workflow.md) | Correct stream error forwarding, byte/record bounds, transactional checkpoints and replay. |
| **Database Engineering** | [`ultimate-database-workflow.md`](./universal/ultimate-database-workflow.md) | Guard executing diagnostics; remove blanket scan/index heuristics; identify actual blockers; define migration compatibility and restoration evidence. |

---

### 5. Hardware, Embedded & IoT Engineering

| Workflow | Universal File | Summary |
| :--- | :---: | :--- |
| **Embedded Programming** | [`ultimate-embedded-programming-workflow.md`](./universal/ultimate-embedded-programming-workflow.md) | Safe byte decoding, supported atomics/queues, target-specific timing and watchdog verification. |
| **Hardware PCB Design** | [`ultimate-hardware-design-workflow.md`](./universal/ultimate-hardware-design-workflow.md) | Chemistry/BOM-specific charging/protection, topology-specific termination, stackup and rating checks. |
| **IoT Hardware & Firmware** | [`ultimate-iot-hardware-workflow.md`](./universal/ultimate-iot-hardware-workflow.md) | Inactive-partition updates, real image signatures, configured rollback and health acknowledgement. |
| **IoT Software & Cloud** | [`ultimate-iot-software-workflow.md`](./universal/ultimate-iot-software-workflow.md) | Scoped identity lifecycle, telemetry deduplication, ordered/versioned state and safe command replay handling. |

---

### 6. Quality Assurance, Security, Operations & Debugging

| Workflow | Universal File | Summary |
| :--- | :---: | :--- |
| **Engineering Best Practices** | [`ultimate-best-practices-workflow.md`](./universal/ultimate-best-practices-workflow.md) | Framework/version routing and workload-based performance checks. |
| **Systematic Debugging** | [`ultimate-debugging-workflow.md`](./universal/ultimate-debugging-workflow.md) | Correct bisect return codes and shell visibility; restore checkout on errors; require actual reproduction and verification commands; label or replace print-only orchestration. |
| **Production Deployment** | [`ultimate-deployment-workflow.md`](./universal/ultimate-deployment-workflow.md) | Immutable release identity, bounded probes/draining, compatible schema and tested recovery. |
| **Git & Release Operations** | [`ultimate-git-workflow.md`](./universal/ultimate-git-workflow.md) | Preserve dirty/index state; scoped staging; shared-history safeguards and repository-native checks. |
| **Code Cleanup** | [`ultimate-code-cleaner.md`](./universal/ultimate-code-cleaner.md) | Entry-point manifest, dynamic consumers, source/runtime corroboration and actual cycle detection. |
| **Code Refactoring** | [`ultimate-refactoring-workflow.md`](./universal/ultimate-refactoring-workflow.md) | Frozen characterization corpus, dynamic caller checks, scoped experiment recovery and safe shadow comparisons. |
| **Code Review Standards** | [`ultimate-review-workflow.md`](./universal/ultimate-review-workflow.md) | Risk precedence, validated analysis rules, evidence-preserving inspection and realistic false-positive checks. |
| **Security Auditing (SAST)** | [`ultimate-security-audit-workflow.md`](./universal/ultimate-security-audit-workflow.md) | Scope-aware probes, exposure/reachability triage, redacted findings and authorized remediation boundaries. |
| **Application Security** | [`ultimate-security-workflow.md`](./universal/ultimate-security-workflow.md) | Context-aware authentication/CSRF, object authorization and provider-specific webhook verification. |
| **Automated Testing & QA** | [`ultimate-testing-workflow.md`](./universal/ultimate-testing-workflow.md) | Replace pooled raw transaction examples with scoped transaction clients or isolated per-worker resources; verify cleanup independently; distinguish baseline failures and flakes. |

---

### 7. UX, Automation & Document Intelligence

| Workflow | Universal File | Summary |
| :--- | :---: | :--- |
| **Scripting & Automation** | [`ultimate-automation-workflow.md`](./universal/ultimate-automation-workflow.md) | Apply the same lock fix; scope destructive targets regardless of object count; await async command actions; define interruption/startup recovery. |
| **Document Intelligence** | [`ultimate-document-intelligence-workflow.md`](./universal/ultimate-document-intelligence-workflow.md) | Parser contracts, layout-aware OCR, resource limits and source-coordinate provenance. |
| **Document Engineering** | [`ultimate-document-workflow.md`](./universal/ultimate-document-workflow.md) | Tool discovery, OOXML preservation, accurate revision attribution and rendered-page inspection. |
| **Natural English** | [`ultimate-natural-english-workflow.md`](./universal/ultimate-natural-english-workflow.md) | Semantic preservation and calibrated uncertainty instead of mechanical word bans. |
| **Technical Documentation** | [`ultimate-documentation-workflow.md`](./universal/ultimate-documentation-workflow.md) | Correct OpenAPI operations, parameters, responses and schema references; fix nested fences; validate quickstart examples and attribution. |
| **Deep Research Strategy** | [`ultimate-research-workflow.md`](./universal/ultimate-research-workflow.md) | Mandatory 15-engine inputs, checkpointed collection, source deduplication, claim-level consensus, and disagreement review. |
| **User Experience (UX) Audit** | [`ultimate-ux-workflow.md`](./universal/ultimate-ux-workflow.md) | Correct standards versus design targets, current scanner scope, manual accessibility and focus lifecycle checks. |

---

## 🔄 Workflow Chaining & Pipelines

Select relevant stages for the actual scope. These example chains do not authorize unrelated refactoring, production mutations, uploads, or releases:

### Example A: Building a New Feature
```text
ultimate-planning-workflow
       ↓
ultimate-architecture-workflow
       ↓
ultimate-frontend-workflow  +  ultimate-api-workflow
       ↓
ultimate-testing-workflow
       ↓
ultimate-review-workflow
       ↓
ultimate-git-workflow
```

### Example B: Resolving a Production Bug
```text
ultimate-debugging-workflow (Root Cause Isolation)
       ↓
ultimate-testing-workflow (Red: Add failing regression test)
       ↓
[Apply minimal fix]
       ↓
ultimate-testing-workflow (Green: Verify test passes)
       ↓
ultimate-refactoring-workflow (Clean up surrounding debt)
       ↓
ultimate-git-workflow (Conventional commit)
```

---

## Shared quality rules

The workflows share scoped execution and evidence guidance. They preserve user
work, distinguish observed results from assumptions, report unavailable checks,
and define recovery for partial failures. Design rules apply to the requested
interface and existing brand; prose rules preserve facts and uncertainty.
Graph guidance accounts for freshness and incomplete dynamic reachability.
Research always retains all 15 required provider inputs.

---

## 📄 License

Distributed under the [MIT License](./LICENSE). Free for personal, commercial, and enterprise open-source use.

## Mandatory 15-engine research

Every research invocation requires substantive inputs from Tavily, Context7, You.com,
Exa, Jina, SERPdive, Linkup, Parallel Search, SerpApi, GitHub, Firecrawl, Crawleo,
Bright Data, Apify, and Brave Search. Configure their actual tools before running.
An unavailable/failed/empty input means **incomplete consensus**, not success with a
smaller subset. Rich per-engine prompts and the existing 100-word neural/LLM query
floor remain. Duplicate articles do not become independent corroboration because
several engines found them. A complete collection may still report unresolved
claim disagreements.

The packaged `research_state.py` helper records provider attempts, evidence and
claim matrices locally. It makes no provider calls, cannot authenticate submitted
records, and does not establish truth. Its tests use explicitly synthetic inputs.

## Connected quality routine (v4)

Use **Research → Plan → Plan Review → Invoke → Debug when needed → Final Code
Review**. The same five workflow names now share a local
[casebook and usage guide](original/resources/ultimate-quality/guide.md):

- Research keeps all 15 substantive provider inputs and adds question coverage,
  disconfirmation and separate collection, evidence and decision-readiness states.
- Planning connects evidence to requirements, decisions, tasks and meaningful checks.
- Review supports plan and code modes with `ready`, `needs_revision` and `blocked`
  gates. Plan review follows the semantic plan; code review follows exact code state.
- Invoker checks prerequisites, assigns ownership and requires independent evidence
  before integration and closure.
- Debugger records competing hypotheses and distinguishing experiments, then verifies
  the fix and protected behavior. Design defects return to planning.

Repair defaults are three attempts per task and three final-review repair rounds.
The helper records actual check exits and artifacts; it does not authenticate
people/provider calls, grant authorization or prove semantic correctness. Existing
research checkpoints remain readable; without new bound coverage they are
`not_assessed` for decision readiness, even when collection and consensus are complete.

The [v4 evaluation corpus](evaluations/v4/README.md) provides 70 cases and explicit
oracles. Local fixture tests establish contract behavior. Comparative quality gains
remain unmeasured until actual baseline/candidate runs and independent grading exist.

## Validation and migration

```sh
python -m pip install -r requirements-dev.txt
python scripts/build.py
npm test
```

The build exports 38 bundles and SHA-256 provenance; validation checks metadata,
resource links and edition parity. Tests cover checkpoint/consensus behavior,
corrected examples where executable, and isolated installer/update behavior.
See [v4 verification status](docs/verification-v4.md) and the
[v3 evidence record](docs/verification.md) for executed and unrun checks.

Version 3 installs Claude Code into `.claude/skills/<name>/SKILL.md`; older flat
`.claude/skills/ultimate-*.md` copies are retained to protect customizations. Inspect
and reconcile those legacy copies manually if they cause duplicate discovery.
Codex's directory layout is unchanged, with bundled resources now included. Bash/PowerShell entry points require Node.js 18+ and a full clone: a downloaded installer alone has no
adjacent workflow files. Node.js 18+ supports the Node installer; Python 3.11+ runs
the development helpers/tests. External providers and specialist tools are separate.

Gemini/Codex user-level synchronization is a separate guarded operation using
`scripts/sync-installed.py` and a private baseline manifest. Dry run is default;
changed local files are rejected for reconciliation. No user configuration,
credentials, other skills, or UI metadata are overwritten.

All installer entry points use one guarded writer and record owned hashes in `.ultimate-workflows-install.sha256`. Keep this receipt to enable safe updates. A v2 installation without a receipt must be backed up/reconciled if its existing files differ; no force-overwrite shortcut is provided. Existing directory/symlink destinations are rejected.
