# Ultimate Workflows (34 Master AI Agent Workflows)

A production-grade collection of **34 master engineering workflows** designed for autonomous AI agents and pair-programming assistants. Built with battle-tested standards, mathematical precision, anti-slop rules, and rigorous checklists.

Compatible with **Claude Code**, **Cursor**, **Windsurf**, **Cline**, **GitHub Copilot**, **Antigravity**, and any LLM agent environment.

---

## 📦 Repository Structure

This repository provides two complete editions of all 34 workflows:

```text
ultimate-workflows/
├── original/     # Full-ecosystem editions (integrated with custom sub-skills, tool bindings, & MCP hooks)
└── universal/    # Standalone editions (zero external skill dependencies, 100% portable for any agent)
```

- **[`universal/`](./universal/)** *(Recommended for general use)*: Self-contained workflows with standard CLI commands, native tool instructions, and zero vendor lock-in.
- **[`original/`](./original/)**: Advanced workflows containing references to specialized sub-skills, brand design manuals, and MCP server bridges.

---

## 🚀 Quick Setup & Installation

### Option A: Cursor IDE (`.cursor/rules`)
Copy desired workflows into your project's `.cursor/rules/` directory or paste into `.cursorrules`:
```bash
mkdir -p .cursor/rules
cp universal/ultimate-frontend-workflow.md .cursor/rules/
```

### Option B: Claude Code (`.claude/skills/` or project root)
Copy the universal workflows into your project's skill directory:
```bash
mkdir -p .claude/skills
cp -r universal/* .claude/skills/
```

### Option C: Antigravity / OpenHands / Cline
Point your workspace workflows or custom skills directory to `universal/`:
```bash
mkdir -p .agent/workflows
cp universal/*.md .agent/workflows/
```

---

## 📚 Workflow Catalog (34 Workflows)

### AI & Autonomous Agent Engineering

| Workflow | Universal Link | Original Link | Summary |
| :--- | :---: | :---: | :--- |
| **`ultimate-agent-dev-workflow`** | [Universal](./universal/ultimate-agent-dev-workflow.md) | [Original](./original/ultimate-agent-dev-workflow.md) | Master workflow for designing, configuring, implementing, and orchestrating autonomous AI agents and multi-agent systems using the Google Antigravity (AGY) SDK. Triggers on "ultimate agent dev workflow", "/ultimate-agent-dev-workflow", or when building custom AGY agents, hooking API runtimes, or delegating tasks to subagents.
argument-hint: "[agent-config | custom-tool | multi-agent]" |
| **`ultimate-agent-workflow`** | [Universal](./universal/ultimate-agent-workflow.md) | [Original](./original/ultimate-agent-workflow.md) | Master workflow for prompt engineering, token caching, memory organization, and subagent delegation. Coordinates task decomposition, spawning cavecrew subagents, and compressing tool outputs to extend context limits. Triggers on "ultimate agent workflow", "/ultimate-agent-workflow", or when spawning subagents, managing agent context, or organizing memory graphs.
argument-hint: "[delegate-task | memory-sync | context-save]" |
| **`ultimate-notebooklm-workflow`** | [Universal](./universal/ultimate-notebooklm-workflow.md) | [Original](./original/ultimate-notebooklm-workflow.md) | Master workflow for managing notebooks, ingesting sources, running AI research, and generating studio audio overviews using Google NotebookLM and its MCP server. Triggers on "ultimate notebooklm workflow", "/ultimate-notebooklm-workflow", or when using NotebookLM tools to research or summarize source documents.
argument-hint: "[notebook-name | action-type]" |

### System Architecture & Planning

| Workflow | Universal Link | Original Link | Summary |
| :--- | :---: | :---: | :--- |
| **`ultimate-architecture-workflow`** | [Universal](./universal/ultimate-architecture-workflow.md) | [Original](./original/ultimate-architecture-workflow.md) | Master workflow for systems architecture design, domain modeling, and technical specification. Guides the creation of Mermaid diagrams, database schemas, microservice boundaries, and Architecture Decision Records (ADRs). Triggers on "ultimate architecture workflow", "/ultimate-architecture-workflow", or when designing systems, mapping out data models, or drafting ADRs.
argument-hint: "[architecture-diagram | database-model | adr-draft]" |
| **`ultimate-brainstorm-workflow`** | [Universal](./universal/ultimate-brainstorm-workflow.md) | [Original](./original/ultimate-brainstorm-workflow.md) | Master workflow for structured brainstorming, architectural design spikes, alternative evaluation, and risk mitigation. Coordinates goal definition, constraint mapping, option matrices, recommendations, and acceptance criteria. Triggers on "ultimate brainstorm workflow", "/ultimate-brainstorm-workflow", or when initiating complex feature designs, architectural spikes, or design sprints.
argument-hint: "[design-spike | feature-brainstorm | risk-assessment]" |
| **`ultimate-planning-workflow`** | [Universal](./universal/ultimate-planning-workflow.md) | [Original](./original/ultimate-planning-workflow.md) | Master workflow for technical planning, design brainstorming, architecture specification, and task sequence generation. Combines structured brainstorming, step-by-step logic exploration, risk mapping, and verification design. Triggers on "ultimate planning workflow", "/ultimate-planning-workflow", or when initiating complex or multi-file code changes.
argument-hint: "[feature-description | refactor-target]" |
| **`ultimate-project-workflow`** | [Universal](./universal/ultimate-project-workflow.md) | [Original](./original/ultimate-project-workflow.md) | Master workflow for agile project management, scope definition, sprint tracking, and walkthrough reporting. Coordinates task.md checklists, milestone prioritization, blocker resolution, and walkthrough.md generation. Triggers on "ultimate project workflow", "/ultimate-project-workflow", or when scoping requirements, creating task lists, or documenting final deliverables.
argument-hint: "[task-scoping | sprint-tracking | walkthrough-report]" |

### Fullstack & Application Engineering

| Workflow | Universal Link | Original Link | Summary |
| :--- | :---: | :---: | :--- |
| **`ultimate-api-workflow`** | [Universal](./universal/ultimate-api-workflow.md) | [Original](./original/ultimate-api-workflow.md) | Master workflow for API design, gateway management, GraphQL, gRPC, and reverse proxies. Coordinates Nginx/Traefik configurations, GraphQL resolvers, Protobuf specs, and API versioning. Triggers on "ultimate api workflow", "/ultimate-api-workflow", or when designing gRPC, GraphQL, Nginx routes, or planning API gateway policies.
argument-hint: "[graphql-schema | grpc-proto | gateway-config]" |
| **`ultimate-frontend-workflow`** | [Universal](./universal/ultimate-frontend-workflow.md) | [Original](./original/ultimate-frontend-workflow.md) | Unified master workflow for building premium, production-grade frontend interfaces. Synthesizes brand alignment, token systems, copywriting, local assets, utility-first styling, fluid motion, and strict UX/accessibility quality checks. Triggers on "ultimate frontend workflow", "/ultimate-frontend-workflow", or when coordinating high-fidelity UI/UX projects.
argument-hint: "[page | component | dashboard]" |
| **`ultimate-fullstack-workflow`** | [Universal](./universal/ultimate-fullstack-workflow.md) | [Original](./original/ultimate-fullstack-workflow.md) | Master workflow for building full-stack applications and backend services. Coordinates database schemas, REST/GraphQL APIs, auth middleware, CORS, real-time sync, and API client integrations. Triggers on "ultimate fullstack workflow", "/ultimate-fullstack-workflow", or when initiating backend, full-stack, or API integration tasks.
argument-hint: "[api-spec | database-schema | fullstack-feature]" |
| **`ultimate-serverless-workflow`** | [Universal](./universal/ultimate-serverless-workflow.md) | [Original](./original/ultimate-serverless-workflow.md) | Master workflow for configuring, deploying, and managing serverless backend platforms (Supabase/Firebase) and ORM systems (Prisma) using Model Context Protocol (MCP) integrations. Triggers on "ultimate serverless workflow", "/ultimate-serverless-workflow", or when configuring database schemas, deploying Edge/Cloud functions, or writing RLS security rules.
argument-hint: "[supabase-deploy | firebase-rules | prisma-migrate]" |
| **`ultimate-monorepo-workflow`** | [Universal](./universal/ultimate-monorepo-workflow.md) | [Original](./original/ultimate-monorepo-workflow.md) | Master workflow for monorepos, multi-package workspaces, shared dependency links, and package release pipelines. Coordinates Turborepo/Nx settings, pnpm workspaces, semantic versioning, and monorepo builds. Triggers on "ultimate monorepo workflow", "/ultimate-monorepo-workflow", or when configuring workspaces, link dependencies, or designing monorepo pipeline builds.
argument-hint: "[workspace-setup | package-link | changeset-version]" |

### Data Engineering, Database & Caching

| Workflow | Universal Link | Original Link | Summary |
| :--- | :---: | :---: | :--- |
| **`ultimate-caching-workflow`** | [Universal](./universal/ultimate-caching-workflow.md) | [Original](./original/ultimate-caching-workflow.md) | Master workflow for caching architectures and runtime performance tuning. Coordinates cache strategies (Redis, memory, HTTP), TTL design, list virtualization, and bundle size optimization. Triggers on "ultimate caching workflow", "/ultimate-caching-workflow", or when designing application caching or resolving latency bottlenecks.
argument-hint: "[cache-strategy | latency-issue]" |
| **`ultimate-data-workflow`** | [Universal](./universal/ultimate-data-workflow.md) | [Original](./original/ultimate-data-workflow.md) | Master workflow for data pipeline engineering, ETL scripting, and data analysis. Coordinates data extraction, cleansing, structured transformation, and loading. Triggers on "ultimate data workflow", "/ultimate-data-workflow", or when designing batch pipelines, parser scripts, database aggregations, or data transformations.
argument-hint: "[etl-pipeline | parser-script | database-aggregation]" |
| **`ultimate-database-workflow`** | [Universal](./universal/ultimate-database-workflow.md) | [Original](./original/ultimate-database-workflow.md) | Master workflow for database schema design, query optimization, indexing strategies, and transaction planning. Integrates Postgres/Supabase best practices, query plan analysis (EXPLAIN), and connection management. Triggers on "ultimate database workflow", "/ultimate-database-workflow", or when designing SQL schemas or optimizing slow queries.
argument-hint: "[table-schema | slow-query]" |

### Hardware, Firmware & IoT Engineering

| Workflow | Universal Link | Original Link | Summary |
| :--- | :---: | :---: | :--- |
| **`ultimate-embedded-programming-workflow`** | [Universal](./universal/ultimate-embedded-programming-workflow.md) | [Original](./original/ultimate-embedded-programming-workflow.md) | Master workflow for bare-metal registers, RTOS scheduling, interrupt handling, and exception fault diagnostics. |
| **`ultimate-hardware-design-workflow`** | [Universal](./universal/ultimate-hardware-design-workflow.md) | [Original](./original/ultimate-hardware-design-workflow.md) | Master workflow for schematic entry, high-speed PCB routing, signal integrity, and manufacturing assembly. |
| **`ultimate-iot-hardware-workflow`** | [Universal](./universal/ultimate-iot-hardware-workflow.md) | [Original](./original/ultimate-iot-hardware-workflow.md) | Master workflow for schematic design, C++ firmware architectures, memory safety, and OTA updates. |
| **`ultimate-iot-software-workflow`** | [Universal](./universal/ultimate-iot-software-workflow.md) | [Original](./original/ultimate-iot-software-workflow.md) | Master workflow for MQTT design, mTLS auth, high-speed telemetry ingestion, device twins, and OTA rollouts. |

### Quality, Security, Operations & Debugging

| Workflow | Universal Link | Original Link | Summary |
| :--- | :---: | :---: | :--- |
| **`ultimate-best-practices-workflow`** | [Universal](./universal/ultimate-best-practices-workflow.md) | [Original](./original/ultimate-best-practices-workflow.md) | Master workflow for engineering best practices across React, Next.js, Expo, Android Native, and general clean code. Coordinates compound composition, RSC boundaries, Hermes engine optimizations, Jetpack Compose, and senior-level software craftsmanship. Triggers on "ultimate best practices", "/ultimate-best-practices-workflow", or when initiating component refactoring or multi-platform native development.
argument-hint: "[react | nextjs | expo | android-native | clean-code]" |
| **`ultimate-debugging-workflow`** | [Universal](./universal/ultimate-debugging-workflow.md) | [Original](./original/ultimate-debugging-workflow.md) | Master workflow for troubleshooting, isolating, and resolving technical issues. Integrates root-cause tracing, sequential hypothesis testing, border instrumentation, and TDD regression protection. Triggers on "ultimate debugging workflow", "/ultimate-debugging-workflow", or when debugging runtime/compile errors.
argument-hint: "[error-message | bug-description]" |
| **`ultimate-deployment-workflow`** | [Universal](./universal/ultimate-deployment-workflow.md) | [Original](./original/ultimate-deployment-workflow.md) | Master workflow for CI/CD, environments setup, builds, deployment pipelines, monitoring, and rollback engineering. Coordinates GitHub Actions, Docker packaging, staging/production boundaries, health check diagnostics, and serverless/edge functions deployments. Triggers on "ultimate deployment workflow", "/ultimate-deployment-workflow", or when handling releases, Dockerfiles, CI configurations, or service deployments.
argument-hint: "[ci-config | dockerfile | deploy-target]" |
| **`ultimate-git-workflow`** | [Universal](./universal/ultimate-git-workflow.md) | [Original](./original/ultimate-git-workflow.md) | Master workflow for version control, branch management, clean staging, conventional commits, and pre-release validation. Triggers on "ultimate git workflow", "/ultimate-git-workflow", or when staging, committing, or pushing changes.
argument-hint: "[commit-message | branch-name]" |
| **`ultimate-refactoring-workflow`** | [Universal](./universal/ultimate-refactoring-workflow.md) | [Original](./original/ultimate-refactoring-workflow.md) | Master workflow for refactoring and code cleanup. Guides the systematic simplification of codebases, dependency reduction, YAGNI enforcement, and design token synchronization. Triggers on "ultimate refactoring workflow", "/ultimate-refactoring-workflow", or when refactoring or restructuring code.
argument-hint: "[target-component | refactor-goal]" |
| **`ultimate-review-workflow`** | [Universal](./universal/ultimate-review-workflow.md) | [Original](./original/ultimate-review-workflow.md) | Master workflow for CodeRabbit-style AI code reviews and PR audits. Combines executive summaries, Mermaid sequence/flowchart diagrams, 1-click suggestion diff blocks, multi-pass security/correctness/performance audits, automated test generation, code smell signatures, typescript safety, and ponytail complexity pruning. Triggers on "ultimate review workflow", "/ultimate-review-workflow", "review pr", "code review", or when asked to act like CodeRabbit.
argument-hint: "[diff-file | branch-name | --incremental | --summarize | --generate-tests]" |
| **`ultimate-security-audit-workflow`** | [Universal](./universal/ultimate-security-audit-workflow.md) | [Original](./original/ultimate-security-audit-workflow.md) | Master workflow for security vulnerability audits, static code analysis (SAST), dependency CVE scans, and regulatory compliance. Triggers on "ultimate security audit workflow", "/ultimate-security-audit-workflow", or when auditing dependencies, setting up SAST, checking compliance, or verifying OWASP.
argument-hint: "[cve-scan | compliance-check | sast-audit]" |
| **`ultimate-security-workflow`** | [Universal](./universal/ultimate-security-workflow.md) | [Original](./original/ultimate-security-workflow.md) | Master workflow for securing and hardening applications. Coordinates input sanitization, authentication architectures, secure HTTP headers, CORS controls, rate limiting, and database Row-Level Security (RLS). Triggers on "ultimate security workflow", "/ultimate-security-workflow", or when handling authentication, user data, cryptographic functions, or production hardening.
argument-hint: "[security-audit | auth-flow | rls-policy]" |
| **`ultimate-testing-workflow`** | [Universal](./universal/ultimate-testing-workflow.md) | [Original](./original/ultimate-testing-workflow.md) | Master workflow for testing, verification, and QA automation. Coordinates unit, integration, end-to-end (E2E) browser testing, API mocking, and coverage monitoring. Triggers on "ultimate testing workflow", "/ultimate-testing-workflow", or when authoring test suites, debugging test failures, or validating release quality.
argument-hint: "[test-suite | mock-payload | e2e-plan]" |

### UX, Automation & Document Intelligence

| Workflow | Universal Link | Original Link | Summary |
| :--- | :---: | :---: | :--- |
| **`ultimate-automation-workflow`** | [Universal](./universal/ultimate-automation-workflow.md) | [Original](./original/ultimate-automation-workflow.md) | Master workflow for scripting, cron tasks, task runners, build automations, and developer CLI utilities. Triggers on "ultimate automation workflow", "/ultimate-automation-workflow", or when writing local automation scripts, build flows, or CLI utilities.
argument-hint: "[cli-script | build-automation | task-runner]" |
| **`ultimate-document-intelligence-workflow`** | [Universal](./universal/ultimate-document-intelligence-workflow.md) | [Original](./original/ultimate-document-intelligence-workflow.md) | Master workflow for parsing, OCR scraping, semantic mapping, and data extraction from PDF, DOCX, PPTX, XLSX, and images. |
| **`ultimate-document-workflow`** | [Universal](./universal/ultimate-document-workflow.md) | [Original](./original/ultimate-document-workflow.md) | Master workflow for creating, parsing, editing, and converting Word documents (.docx files). Coordinates JS docx-builder setups, XML unpacking/repacking, tracked changes auditing, comment injections, and PDF conversions. Triggers on "ultimate document workflow", "/ultimate-document-workflow", or when manipulating Word docs, templates, tracked changes, or exporting docx to PDF.
argument-hint: "[docx-generate | xml-edit | pdf-export]" |
| **`ultimate-documentation-workflow`** | [Universal](./universal/ultimate-documentation-workflow.md) | [Original](./original/ultimate-documentation-workflow.md) | Master workflow for project documentation, API specifications, and developer onboarding. Coordinates project READMEs, API Swagger/OpenAPI mappings, Architecture Decision Records (ADRs), and setup guides. Triggers on "ultimate documentation workflow", "/ultimate-documentation-workflow", or when generating documentation, writing READMEs, or documenting API interfaces.
argument-hint: "[readme-template | api-spec | onboarding-guide]" |
| **`ultimate-research-workflow`** | [Universal](./universal/ultimate-research-workflow.md) | [Original](./original/ultimate-research-workflow.md) | Master workflow for technical research, document mining, API checks, and dependency validation. Combines dual-engine search (Tavily + Exa executed simultaneously), sequential query decomposition, and memory graph persistence. Triggers on "ultimate research workflow", "/ultimate-research-workflow", or when researching libraries, APIs, or system designs.
argument-hint: "[research-topic | search-query]" |
| **`ultimate-ux-workflow`** | [Universal](./universal/ultimate-ux-workflow.md) | [Original](./original/ultimate-ux-workflow.md) | Master workflow for User Experience (UX) audits, usability engineering, accessibility verification, and platform design compliance. Triggers on "ultimate ux workflow", "/ultimate-ux-workflow", or when conducting usability audits, reviewing interactive flows, or validating accessibility.
argument-hint: "[ux-audit | accessibility-check | component-flow]" |

---

## 🛡️ Core Tenets & Anti-Slop Discipline

Every workflow enforces:
1. **Mathematical Precision & System Tokens:** No hardcoded arbitrary numbers or colors.
2. **Zero-Fluff / Anti-Slop Rules:** Elimination of generic AI clichés, unstyled defaults, and filler prose.
3. **Iron Laws & Quality Gates:** Strict validation (WCAG 2.2 AA, Core Web Vitals $p75$, strict type safety, zero layout shifts).
4. **Deterministic Protocols:** Every workflow features step-by-step phased execution pipelines with verification gates.

---

## 📄 License

[MIT License](./LICENSE) - Free for personal and commercial open-source use.
