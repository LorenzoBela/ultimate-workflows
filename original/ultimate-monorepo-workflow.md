---
name: ultimate-monorepo-workflow
description: >
  Flawless 10/10 Master Workflow for monorepos, multi-package workspaces, dependency boundary enforcement,
  Turborepo/Nx caching pipelines, Syncpack version alignment, and Changesets multi-package releases.
  Triggers on "ultimate monorepo workflow", "/ultimate-monorepo-workflow", or when
  configuring workspaces, link dependencies, or designing monorepo pipeline builds.
argument-hint: "[workspace-setup | package-link | changeset-version | --turbo | --syncpack]"
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

# Ultimate Monorepo & Multi-Package Architecture Workflow (10/10 Master Engine)

This workflow guides the structure, dependency boundary isolation, computational cache reuse (Turborepo/Nx), dependency version unification (Syncpack), and atomic versioned publishing (Changesets) across multi-package workspaces.

```
                                      [MONOREPO ROOT WORKSPACE]
                                                  │
                       ┌──────────────────────────┴──────────────────────────┐
                       ▼                                                     ▼
           [PHASE 1: WORKSPACE ARCHITECTURE]                     [PHASE 2: PIPELINE ORCHESTRATION]
           ├─ apps/ (Deployable Services)                        ├─ Turborepo / Nx Task Graphs
           ├─ packages/ (Shared Types, UI, Config)               ├─ Remote Computation Caching
           └─ Strict pnpm-workspace.yaml Isolation               └─ Topological Task Ordering (^build)
                       │
                       ▼
     ┌─────────────────────────────────────────────────────────────────────────────┐
     │                 PHASE 3: DEPENDENCY UNIFICATION & BOUNDARY ENFORCEMENT       │
     │  • Syncpack Version Alignment • Zero Phantom Dependencies • Shared TSConfigs │
     └──────────────────────────────────────┬──────────────────────────────────────┘
                                            ▼
                               [PHASE 4: MULTI-PACKAGE RELEASES & CHANGESETS]
                 ┌──────────────────────────┼──────────────────────────┐
                 ▼                          ▼                          ▼
         ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
         │ 📦 CHANGESET │           │ 🏷️ SEMVER    │           │ 🚀 ATOMIC    │
         │ PR Markdown  │           │ Major/Min/Pat│           │ Publish Gate │
         └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Monorepo Architecture

1. **Explicit Package Boundaries**: No package may import from another package without declaring it in its `package.json` `dependencies` or `devDependencies`.
2. **Zero Phantom Dependencies**: All builds must run with strict package managers (pnpm or Yarn Berry) that isolate unhoisted dependencies.
3. **Deterministic Task Graphs**: Tasks defined in `turbo.json` or `nx.json` must declare explicit dependencies (`"^build"`, `"$TURBO_DEFAULT$"`).
4. **Unified Dependency Coordinates**: All packages in the monorepo must share identical major/minor versions of third-party libraries (`syncpack`).
5. **Atomic Changeset Publishing**: Every pull request that modifies code in a publishable package must include a corresponding Changeset file (`.changeset/*.md`).

---

## 🔬 The 4-Phase Monorepo Pipeline

### Phase 1: Workspace Architecture & Directory Layout
```text
monorepo-root/
├── apps/
│   ├── web/               # Next.js 15 App Router
│   ├── mobile/            # React Native / Expo
│   └── api/               # Express / Fastify / Node
├── packages/
│   ├── ui/                # Shared React Design Tokens & Components
│   ├── database/          # Prisma schema, migrations, and Supabase client
│   ├── tsconfig/          # Base TypeScript configurations
│   └── eslint-config/     # Shared ESLint & Prettier rules
├── pnpm-workspace.yaml
├── turbo.json
└── package.json
```

### Phase 2: Pipeline Orchestration (`turbo.json`)
```json
{
  "$schema": "https://turbo.build/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**", "!.next/cache/**"]
    },
    "lint": {
      "dependsOn": ["^build"]
    },
    "test": {
      "dependsOn": ["^build"],
      "outputs": ["coverage/**"]
    },
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}
```

### Phase 3: Dependency Unification with Syncpack
- Run `npx syncpack list-mismatches` to detect conflicting dependency versions across workspace packages.
- Fix mismatches using `npx syncpack fix-mismatches` to ensure uniform dependency versions.

### Phase 4: Atomic Multi-Package Release with Changesets
- Add a changeset: `npx changeset` (prompts for patch/minor/major and description).
- Version packages: `npx changeset version` (updates package.jsons and changelogs).
- Publish packages: `npx changeset publish` (publishes packages in topological dependency order).
