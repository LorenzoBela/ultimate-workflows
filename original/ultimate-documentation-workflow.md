---
name: ultimate-documentation-workflow
description: >
  Flawless 10/10 Master Workflow for technical documentation, OpenAPI 3.1 specifications,
  interactive runnable code snippets, Architecture Decision Records (ADRs), and friction-free developer onboarding.
  Triggers on "ultimate documentation workflow", "/ultimate-documentation-workflow", or when
  generating documentation, writing READMEs, or documenting API interfaces.
argument-hint: "[readme-template | api-spec | onboarding-guide | --openapi | --adr]"
---

<!-- INVARIANT_START:ANTI_AI_SLOP -->
## 🛑 HARDENED ANTI-AI SLOP MANDATE: NATURAL PROSE & BESPOKE DESIGN CRAFT
All agent communications, architectural plans, reviews, code comments, and frontend implementations MUST strictly adhere to natural human engineering standards. Both corporate AI prose slop and cookie-cutter "vibecoded" UI slop are strictly banned.

### 1. Zero Prose & Grammar Slop (Natural Human Voice)
- **Banned Lexicon:**
  - *Empty Verbs:* delve, embark, foster, resonate, underscore, leverage, elevate, harness, navigate, empower, illuminate, facilitate, tailor, showcase, unveil.
  - *Corporate Buzz-Adjectives:* testament, tapestry, beacon, cornerstone, robust, seamless, pivotal, crucial, paramount, cutting-edge, vibrant, bespoke, game-changer, journey, realm, landscape, holistic, comprehensive, multifaceted, versatile, transformative.
  - *Formulaic Transitions:* furthermore, moreover, in conclusion, it is worth noting, at the end of the day, without further ado, needless to say.
- **Banned Syntactical Patterns:**
  - **Zero Sycophancy / Pleasantries:** NEVER start responses with "Certainly!", "Great question!", "I'd be happy to help!", "Awesome!", or "Let's dive in!".
  - **Zero Summary Outros:** NEVER end answers with a repetitive paragraph restating earlier points using generic corporate filler.
  - **Zero Formulaic "Rule-of-Three" Bullets:** Do not default to 3-bullet lists where each bullet starts with a bold abstract noun followed by a colon and fluff.
  - **Zero Hedging:** Do not write "You might want to potentially consider checking...". Write "Check X, or Y crashes."
- **Natural Voice Standard:** Speak like a systems developer in terminal, Slack, or GitHub issues: blunt, concise, precise, pragmatic. Code and runnable shell commands come first.

### 2. Zero Visual & UI/UX Design Slop (Bespoke Engineering Craft)
- **Banned Color Clichés:**
  - BAN default AI Blue-to-Indigo/Purple gradients (`bg-gradient-to-r from-blue-600 to-indigo-700` or violet hues).
  - BAN colored ambient glowing shadows (`box-shadow` with >= 24px blur matching accent color).
  - BAN washed-out low-contrast gray text (`text-gray-400` / `text-gray-500` failing WCAG AA 4.5:1).
  - BAN gradient headline text (`bg-clip-text text-transparent bg-gradient-to-r` on H1s).
- **Banned Layout & Component Tropes:**
  - BAN cookie-cutter Bento Grid walls filled with fake stats, empty cards, or generic Lucide icon spam.
  - BAN centered hero boilerplate with a floating pill above H1 (`"✨ New: [Feature]"`).
  - BAN unmodified shadcn/ui defaults (`--radius: 0.5rem`, stock button/card exports without brand styling).
  - BAN tinted circular icon containers (`bg-primary/10 text-primary p-3 rounded-full`).
  - BAN static terminal window mockups with red/yellow/green dots in the hero.
  - BAN raw emojis used as icons (`✨`, `🚀`, `⚡`, `🔒`) in production UI markup.
- **Bespoke Design Standard:**
  - Commit to an intentional aesthetic: brutalist, high-density telemetry, refined editorial, or precision dark-mode.
  - High information density (Linear/Stripe standard), micro-borders (`rgba(255,255,255,0.08)`), and tabular numerals (`tabular-nums`).
  - Every component must implement all 7 states: `Default, Hover, Focus-Visible, Active, Loading (Skeleton), Disabled, Error`.
<!-- INVARIANT_END:ANTI_AI_SLOP -->

<!-- INVARIANT_START:GRAPHIFY -->
## 🧠 HARDENED GRAPHIFY KNOWLEDGE ENGINE GATE (AST-FIRST CODE INTELLIGENCE)
Whenever `graphify-out/graph.json` exists in the repository root, agents MUST interact with the AST knowledge graph. Blind directory traversal and unconstrained multi-file context dumping are strictly banned.

1. **Zero-Blind-Grep Invariant:**
   - Running unstructured grep (`grep -r`, `Select-String *.*`, `ripgrep` across entire project) to locate callers or symbol references is FORBIDDEN when `graph.json` is present.
   - Agents must query Graphify first: `graphify query "<symbol_or_concept>"`.

2. **Blast Radius Gate (`graphify explain "<symbol>"`):**
   - Before modifying, refactoring, or deleting any shared interface, model, route, or function, the agent MUST run `graphify explain "<symbol>"`.
   - If incoming edge count > 0, every caller surfaced by Graphify MUST be explicitly enumerated in the task DAG or implementation plan before touching code.

3. **Call-Path Fault Tracing (`graphify path "<source>" "<target>" --undirected`):**
   - When debugging multi-hop failures (e.g. UI -> API -> DB), the agent must run `graphify path` to map the exact shortest call chain between entry point and crash sink before reading source code.

4. **Leiden Community Worktree Partitioning:**
   - When spawning parallel subagents in `ultimate-multi-agent-invoker`, tasks MUST be partitioned by Leiden community clusters (from `graphify-out/graph.json`).
   - If two tasks share a God Node (identified in `graphify-out/GRAPH_REPORT.md`), they CANNOT run concurrently without explicit file-level mutex locks.

5. **Subagent Context Clamp (70% Token Reduction):**
   - Never dump entire raw source files into subagent prompts. Inject only the scoped subgraph from `graphify query "<task_scope>"`.

6. **Post-Commit AST Synchronization (`graphify update .`):**
   - After completing code modifications or merging Git worktrees, the agent MUST run `graphify update .` (local AST delta update, 2s runtime, 0 API tokens) to maintain graph synchronization.
<!-- INVARIANT_END:GRAPHIFY -->

# Ultimate Technical Documentation & Onboarding Workflow (10/10 Master Engine)

This workflow guides the creation of high-clarity technical documentation, interactive OpenAPI 3.1 specifications, immutable Architecture Decision Records (ADRs), and 5-minute developer onboarding runbooks.

```
                                      [TECHNICAL DOCUMENTATION INITIATIVE]
                                                       │
                          ┌────────────────────────────┴────────────────────────────┐
                          ▼                                                         ▼
              [PHASE 1: MASTER REPOSITORY README]                       [PHASE 2: OPENAPI 3.1 & SDK SPECS]
              ├─ 30-Second Elevator Pitch & Architecture Map            ├─ Interactive Request/Response Schemas
              ├─ 1-Line Prerequisites & Copy-Paste Setup                ├─ Error Code Matrix (RFC 7807)
              └─ Environment Variable Matrix (.env.example)             └─ Auto-Generated Typed Client Snippets
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: ARCHITECTURE DECISION RECORDS (ADR)                │
        │  • docs/adr/ • Context • Invariants • Rejected Alternatives • Trade-offs    │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: 5-MINUTE ONBOARDING & RUNBOOKS]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🚀 1-CMD RUN │           │ 🧪 SEED DB   │           │ 📊 ARCH DIAG │
            │ npm run dev  │           │ Mock Data    │           │ Mermaid C4   │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Technical Documentation

1. **Code Explains HOW, Docs Explain WHY**: Never restate what obvious code lines do; document the constraints, domain invariants, and tradeoffs that forced the implementation.
2. **Copy-Paste Runnable Examples**: Every code snippet in documentation must be syntactically valid and runnable without undisclosed dependencies.
3. **The 5-Minute Developer Onboarding Law**: A new engineer must be able to clone the repo, run one setup command, seed the test database, and pass unit tests within 5 minutes.
4. **Strictly Synchronized `.env.example`**: Every environment variable referenced in `process.env` must have an annotated placeholder entry in `.env.example`.
5. **No Undocumented Public Endpoints**: 100% of HTTP endpoints must have corresponding OpenAPI 3.1 entries with request/response/error schemas.

---

## 🔬 The 4-Phase Documentation Pipeline

### Phase 1: Master Repository README Template
```markdown
# Project Name

> High-impact 1-sentence value proposition.

## 🚀 Quickstart (Under 3 Minutes)

```bash
git clone https://github.com/org/repo.git && cd repo
cp .env.example .env.local
pnpm install
pnpm db:seed
pnpm dev
```

## 🏗️ Architecture & Core Domains
- `apps/web`: Next.js 15 App Router Frontend
- `packages/database`: PostgreSQL schema & Supabase migrations
- `packages/ui`: Shared React design token components

## 🔑 Environment Variables
| Variable | Description | Default / Example | Required |
|---|---|---|---|
| `DATABASE_URL` | PgBouncer pooled connection | `postgresql://...:6543/postgres` | Yes |
```

### Phase 2: OpenAPI 3.1 Interactive Endpoint Spec
```yaml
openapi: 3.1.0
info:
  title: Core Billing API
  version: 2026-08-15
paths:
  /api/v1/charges:
    post:
      summary: Create an idempotent charge
      headers:
        Idempotency-Key:
          schema:
            type: string
            format: uuid
          required: true
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChargeRequest'
```

### Phase 3: Architecture Decision Record (ADR)
- Maintain sequential Markdown files under `docs/adr/0001-title.md` detailing Status, Context, Decision, Alternatives Considered, and Consequences.
