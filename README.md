# ⚡ Ultimate Workflows: 38 Production-Grade AI Agent Workflows

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Workflows: 38](https://img.shields.io/badge/Workflows-38%20Total-brightgreen.svg)](./universal/)
[![Compatibility](https://img.shields.io/badge/Supports-Codex%20%7C%20Cursor%20%7C%20Claude%20Code%20(CC)%20%7C%20Antigravity%20(AGY)%20%7C%20Windsurf%20%7C%20Cline%20%7C%20VS%20Code-orange.svg)](#-one-line-installers)

A battle-tested suite of **38 master engineering workflows** crafted for autonomous AI agents, coding assistants, and pair-programming environments.

Eliminate generic "AI slop", vague pseudocode, and brittle architectures. Every workflow enforces mathematical precision, design tokens, anti-slop rulesheets, step-by-step phased execution pipelines, and deterministic verification gates.

---

## ⚡ One-Line Installers (Instant Setup)

Install into **any current project repository** in seconds:

### Codex (desktop app, CLI, and IDE extension)

**1. Install.** Open a terminal in the project where you want to use the workflows. With Node.js/npm and Git installed, run this in PowerShell, macOS, or Linux:

```sh
npx github:LorenzoBela/ultimate-workflows codex
```

The command installs all 38 universal workflows into the current project. It creates one folder per skill, preserving the workflow's `name` and `description`:

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

For an explicit parallel run, request `$ultimate-multi-agent-invoker` with an approved plan. Installing these files supplies workflow instructions; it does not install the external tools, other skills, or MCP connections referenced by a workflow.

**Updating:** rerun the install command from the same project. It replaces matching `ultimate-*/SKILL.md` files, so save any local customizations first. Commit `.agents/skills/` if teammates should use the same workflows. Avoid installing duplicate copies at both project and user scope.

**Already cloned this repository?** Run the installer from your target project's terminal using the path to the clone:

```sh
node /path/to/ultimate-workflows/scripts/install.js codex
```

Without Node.js, the clone also includes native installers. Run either command from the target project, replacing the example path with your clone's location:

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
curl -fsSL https://raw.githubusercontent.com/LorenzoBela/ultimate-workflows/main/scripts/install.sh | bash -s cursor

# PowerShell (Windows)
irm https://raw.githubusercontent.com/LorenzoBela/ultimate-workflows/main/scripts/install.ps1 | iex; Install-Cursor
```

---

### 🟣 Claude Code (`.claude/skills/`)
```bash
# Node / npx
npx github:LorenzoBela/ultimate-workflows claude

# Bash (macOS / Linux)
curl -fsSL https://raw.githubusercontent.com/LorenzoBela/ultimate-workflows/main/scripts/install.sh | bash -s claude

# PowerShell (Windows)
irm https://raw.githubusercontent.com/LorenzoBela/ultimate-workflows/main/scripts/install.ps1 | iex; Install-Claude
```

---

### 🚀 Google Antigravity / AGY (`.agent/workflows/`)
```bash
# Node / npx
npx github:LorenzoBela/ultimate-workflows agy

# Bash (macOS / Linux)
curl -fsSL https://raw.githubusercontent.com/LorenzoBela/ultimate-workflows/main/scripts/install.sh | bash -s agy

# PowerShell (Windows)
irm https://raw.githubusercontent.com/LorenzoBela/ultimate-workflows/main/scripts/install.ps1 | iex; Install-AGY
```

---

### 🌊 Windsurf / Cascade (`.windsurfrules`)
```bash
# Node / npx
npx github:LorenzoBela/ultimate-workflows windsurf

# Bash (macOS / Linux)
curl -fsSL https://raw.githubusercontent.com/LorenzoBela/ultimate-workflows/main/scripts/install.sh | bash -s windsurf

# PowerShell (Windows)
irm https://raw.githubusercontent.com/LorenzoBela/ultimate-workflows/main/scripts/install.ps1 | iex; Install-Windsurf
```

---

### 🤖 Cline / Roo-Code (`.clinerules`)
```bash
# Node / npx
npx github:LorenzoBela/ultimate-workflows cline

# Bash (macOS / Linux)
curl -fsSL https://raw.githubusercontent.com/LorenzoBela/ultimate-workflows/main/scripts/install.sh | bash -s cline

# PowerShell (Windows)
irm https://raw.githubusercontent.com/LorenzoBela/ultimate-workflows/main/scripts/install.ps1 | iex; Install-Cline
```

---

### 💻 VS Code / GitHub Copilot (`.github/copilot-instructions.md`)
```bash
# Node / npx
npx github:LorenzoBela/ultimate-workflows copilot

# Bash (macOS / Linux)
curl -fsSL https://raw.githubusercontent.com/LorenzoBela/ultimate-workflows/main/scripts/install.sh | bash -s copilot

# PowerShell (Windows)
irm https://raw.githubusercontent.com/LorenzoBela/ultimate-workflows/main/scripts/install.ps1 | iex; Install-Copilot
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
- [Anti-Slop Engineering Rules](#-anti-slop-engineering-rules)
- [License](#-license)

---

## 🧠 What Are Ultimate Workflows?

Standard AI code generation often suffers from "vibecoding": generic UI defaults (such as indigo gradients, uniform `rounded-2xl`, wash-out grey text), unhandled loading/error states, missing accessibility, brittle database queries, and missing edge-case handling.

**Ultimate Workflows solve this by embedding production-grade senior engineering constraints directly into the agent's context window:**

1. **Phased Execution Pipelines:** Every workflow guides the agent through structured phases (Research → Architecture → Implementation → Validation → Review).
2. **Iron Laws & Non-Negotiables:** Hard constraints (e.g., WCAG 2.2 AA accessibility, Core Web Vitals $p75$, zero Cumulative Layout Shift, zero hardcoded colors).
3. **Anti-Slop Rulesheets:** Explicit blacklists of common AI code tells and boilerplate antipatterns.
4. **Actionable Checklists:** Concrete pre-flight verification items before declaring code done.

---

## 📦 Two Editions: Universal vs. Original

The `original/` edition mirrors the 38 `ultimate-*` skills installed in Gemini. The `universal/` edition includes the same updates while retaining its existing portability adaptations for multi-agent execution, planning, research, and review. Both editions include Gemini's shared prose/design and Graphify gates; Graphify integration requires the Graphify CLI when a knowledge graph is present.

```text
ultimate-workflows/
├── universal/    # 🌟 Recommended: Portable adaptations for supported agents/IDEs
├── original/     # Advanced: Includes custom sub-skill links and MCP server hooks
├── scripts/      # Automated multi-IDE installer scripts (Node, Bash, PowerShell)
└── README.md     # Documentation & quickstart index
```

| Feature | `universal/` (Portable) | `original/` (Ecosystem) |
| :--- | :---: | :---: |
| **External Dependencies** | Some workflows require specialized skills or CLIs; Graphify gates apply when a graph is present | Requires ecosystem sub-skills, CLIs, and MCPs |
| **Tool Execution** | Standard CLI (`grep`, `npm`, `vitest`, `git`) | MCP Tools (`memory`, `playwright`, `tavily`) |
| **Sub-Skill References** | Embedded guidance plus specialized skill references | Linked to ecosystem skills |
| **IDE / Agent Portability** | Supported IDEs with required workflow tools configured | Best for custom Antigravity/MCP agents |

---

## 📚 Complete 38-Workflow Catalog

### 1. AI & Autonomous Agent Engineering

| Workflow | Universal File | Summary |
| :--- | :---: | :--- |
| **Multi-Agent Invoker** | [`ultimate-multi-agent-invoker.md`](./universal/ultimate-multi-agent-invoker.md) | Master swarm orchestrator: dynamic DAG fan-out, ponytail-caveman compression, and DRAMA trust-chain recovery. |
| **Agent Development** | [`ultimate-agent-dev-workflow.md`](./universal/ultimate-agent-dev-workflow.md) | Architecting custom autonomous agents, runtime API hooks, MCP integrations, and memory lifecycles. |
| **Agent Orchestration** | [`ultimate-agent-workflow.md`](./universal/ultimate-agent-workflow.md) | Subagent spawning, prompt caching optimization, context pruning, and multi-agent coordination. |
| **NotebookLM Research** | [`ultimate-notebooklm-workflow.md`](./universal/ultimate-notebooklm-workflow.md) | Document ingestion, synthesis, deep source research, and structured audio/briefing preparation. |

---

### 2. System Architecture & Technical Planning

| Workflow | Universal File | Summary |
| :--- | :---: | :--- |
| **Graphify Code Intelligence** | [`ultimate-graphify-workflow.md`](./universal/ultimate-graphify-workflow.md) | Knowledge graph navigation, impact analysis, call paths, and graph maintenance. |
| **System Architecture** | [`ultimate-architecture-workflow.md`](./universal/ultimate-architecture-workflow.md) | Domain-Driven Design (DDD), Mermaid architecture diagrams, ADR creation, and boundary specs. |
| **Brainstorming & Scoping** | [`ultimate-brainstorm-workflow.md`](./universal/ultimate-brainstorm-workflow.md) | Structured technical brainstorming, trade-off matrix evaluation, constraint mapping, and scope bounding. |
| **Implementation Planning** | [`ultimate-planning-workflow.md`](./universal/ultimate-planning-workflow.md) | Atomic step-by-step task breakdown, dependency sequencing, rollback plans, and verification plans. |
| **Project & Sprint Tracking** | [`ultimate-project-workflow.md`](./universal/ultimate-project-workflow.md) | Milestone delivery, task checklist tracking, blockers resolution, and stakeholder walkthroughs. |

---

### 3. Fullstack & Application Engineering

| Workflow | Universal File | Summary |
| :--- | :---: | :--- |
| **API Engineering** | [`ultimate-api-workflow.md`](./universal/ultimate-api-workflow.md) | REST, GraphQL, gRPC design, Protobuf contracts, API gateways, rate limiting, and versioning. |
| **Frontend Engineering** | [`ultimate-frontend-workflow.md`](./universal/ultimate-frontend-workflow.md) | High-fidelity UI systems, CSS tokens, 60fps animations, RSC boundaries, and 50 anti-slop rules. |
| **Fullstack Development** | [`ultimate-fullstack-workflow.md`](./universal/ultimate-fullstack-workflow.md) | End-to-end stack architecture, type-safe RPC/REST boundaries, auth middleware, and state sync. |
| **Serverless Platforms** | [`ultimate-serverless-workflow.md`](./universal/ultimate-serverless-workflow.md) | Edge Functions, serverless databases (Supabase/Firebase/Prisma), and Row-Level Security (RLS). |
| **Monorepo Architecture** | [`ultimate-monorepo-workflow.md`](./universal/ultimate-monorepo-workflow.md) | Turborepo/Nx workspaces, shared package linking, build caching, and semantic release pipelines. |

---

### 4. Data Systems, Database & Caching

| Workflow | Universal File | Summary |
| :--- | :---: | :--- |
| **Caching Architectures** | [`ultimate-caching-workflow.md`](./universal/ultimate-caching-workflow.md) | Multi-tier cache invalidation (Redis, HTTP, in-memory), TTL strategies, stale-while-revalidate. |
| **Data Pipelines & ETL** | [`ultimate-data-workflow.md`](./universal/ultimate-data-workflow.md) | Batch/stream ETL pipelines, data extraction, cleansing, schema transformations, and validation. |
| **Database Engineering** | [`ultimate-database-workflow.md`](./universal/ultimate-database-workflow.md) | Schema normalization, index design (B-tree, GIN, BRIN), EXPLAIN ANALYZE query optimization, and migrations. |

---

### 5. Hardware, Embedded & IoT Engineering

| Workflow | Universal File | Summary |
| :--- | :---: | :--- |
| **Embedded Programming** | [`ultimate-embedded-programming-workflow.md`](./universal/ultimate-embedded-programming-workflow.md) | Bare-metal registers, RTOS multi-threading, ISR prioritization, and low-power sleep modes. |
| **Hardware PCB Design** | [`ultimate-hardware-design-workflow.md`](./universal/ultimate-hardware-design-workflow.md) | Schematic capture, high-speed differential routing, impedance matching, EMC compliance, and DFM. |
| **IoT Hardware & Firmware** | [`ultimate-iot-hardware-workflow.md`](./universal/ultimate-iot-hardware-workflow.md) | Secure boot, flash encryption, OTA dual-partition rollback, memory safety, and hardware watchdogs. |
| **IoT Software & Cloud** | [`ultimate-iot-software-workflow.md`](./universal/ultimate-iot-software-workflow.md) | MQTT topic namespaces, mTLS device authentication, high-throughput telemetry ingestion, and device twins. |

---

### 6. Quality Assurance, Security, Operations & Debugging

| Workflow | Universal File | Summary |
| :--- | :---: | :--- |
| **Engineering Best Practices** | [`ultimate-best-practices-workflow.md`](./universal/ultimate-best-practices-workflow.md) | Universal code standards, DRY/KISS enforcement, error contracts, and 130 core architectural rules. |
| **Systematic Debugging** | [`ultimate-debugging-workflow.md`](./universal/ultimate-debugging-workflow.md) | Multi-agent diagnostic swarm (`cavecrew`), Turn 1 subagent dispatch, Google SRE incident mitigation, and TDD regression fix. |
| **Production Deployment** | [`ultimate-deployment-workflow.md`](./universal/ultimate-deployment-workflow.md) | CI/CD pipelines, containerization (Docker), zero-downtime blue/green rollouts, and health check gates. |
| **Git & Release Operations** | [`ultimate-git-workflow.md`](./universal/ultimate-git-workflow.md) | Atomic conventional commits, clean branching strategies, pre-commit validation, and release tags. |
| **Code Cleanup** | [`ultimate-code-cleaner.md`](./universal/ultimate-code-cleaner.md) | AST-guided dead code, unused export, and dependency cleanup with verification gates. |
| **Code Refactoring** | [`ultimate-refactoring-workflow.md`](./universal/ultimate-refactoring-workflow.md) | Systematic technical debt elimination, dead-code removal, modular decomposition, and safety regressions. |
| **Code Review Standards** | [`ultimate-review-workflow.md`](./universal/ultimate-review-workflow.md) | Severity-tiered code audits (Blocker, Major, Minor, Nit) with concrete actionable diff recommendations. |
| **Security Auditing (SAST)** | [`ultimate-security-audit-workflow.md`](./universal/ultimate-security-audit-workflow.md) | Static vulnerability scans, OWASP Top 10 auditing, dependency CVE scans, and compliance checking. |
| **Application Security** | [`ultimate-security-workflow.md`](./universal/ultimate-security-workflow.md) | Input sanitization, auth/authz separation, CORS hardening, CSRF defense, rate-limiting, and secrets hygiene. |
| **Automated Testing & QA** | [`ultimate-testing-workflow.md`](./universal/ultimate-testing-workflow.md) | Test-Driven Development (TDD), unit, integration, and E2E browser test automation with high coverage. |

---

### 7. UX, Automation & Document Intelligence

| Workflow | Universal File | Summary |
| :--- | :---: | :--- |
| **Scripting & Automation** | [`ultimate-automation-workflow.md`](./universal/ultimate-automation-workflow.md) | Developer CLI utilities, cron runners, build task automations, and cross-platform shell scripts. |
| **Document Intelligence** | [`ultimate-document-intelligence-workflow.md`](./universal/ultimate-document-intelligence-workflow.md) | Parsing, OCR scraping, semantic table extraction from PDF, DOCX, XLSX, and scanned documents. |
| **Document Engineering** | [`ultimate-document-workflow.md`](./universal/ultimate-document-workflow.md) | Programmatic DOCX generation, XML styling, tracked changes auditing, and PDF conversions. |
| **Natural English** | [`ultimate-natural-english-workflow.md`](./universal/ultimate-natural-english-workflow.md) | Clear prose, natural tone, and removal of formulaic language. |
| **Technical Documentation** | [`ultimate-documentation-workflow.md`](./universal/ultimate-documentation-workflow.md) | Developer READMEs, OpenAPI/Swagger specifications, Architecture Decision Records (ADRs), and user guides. |
| **Deep Research Strategy** | [`ultimate-research-workflow.md`](./universal/ultimate-research-workflow.md) | Pentadeca-Engine (15/15) parallel search, 5 strategic clusters, deep passage quotes, and 15-way consensus matrix. |
| **User Experience (UX) Audit** | [`ultimate-ux-workflow.md`](./universal/ultimate-ux-workflow.md) | Usability heuristics, micro-interaction reviews, WCAG 2.2 accessibility verification, and UX polish. |

---

## 🔄 Workflow Chaining & Pipelines

Workflows can be chained seamlessly to execute end-to-end engineering lifecycles:

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

## 🛡️ Anti-Slop Engineering Rules

All 38 workflows enforce strict quality gates against generic AI-generated code:

- **No AI Default Palettes:** Forbids unstyled indigo-blue gradients, washed-out grey body text, and generic purple accents.
- **No Untracked Typographic Scales:** Mandates optical letter-spacing, `text-wrap: balance` on headlines, and explicit line-heights.
- **Explicit Component State Matrices:** Requires 7 states for every interactive component: `Default`, `Hover`, `Focus-Visible`, `Active`, `Loading (Skeleton)`, `Disabled`, and `Error`.
- **Zero CLS & Pre-Allocated Layouts:** Prohibits layout-shifting spinners in favor of pixel-matched skeleton loaders.
- **Security-First Defaults:** Input validation at boundaries, least-privilege defaults, and zero hardcoded secrets.

---

## 📄 License

Distributed under the [MIT License](./LICENSE). Free for personal, commercial, and enterprise open-source use.
