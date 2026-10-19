---
name: ultimate-git-workflow
description: >
  Flawless 10/10 Master Workflow for version control, stacked diffs (Meta standard),
  conventional commits (Caveman Commit), interactive rebase sanitization, and pre-release branch protection.
  Triggers on "ultimate git workflow", "/ultimate-git-workflow", or when staging,
  committing, or pushing changes.
argument-hint: "[commit-message | branch-name | --stacked | --rebase | --push]"
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

# Ultimate Git & Release Workflow (10/10 Master Engine)

This workflow enforces surgical version control hygiene, stacked atomic diffs, conventional commit standards, pre-commit validation gates, and clean branch releases.

```
                                      [UNCOMMITTED WORKSPACE CHANGES]
                                                     │
                          ┌──────────────────────────┴──────────────────────────┐
                          ▼                                                     ▼
              [STEP 1: PRE-COMMIT VERIFICATION GATE]                [STEP 2: ATOMIC SCOPE STAGING]
              ├─ Strict TypeScript Compile (tsc)                    ├─ Group by Domain (Contracts -> UI)
              ├─ Linter (ESLint 0 Warnings)                         ├─ Discard Unrelated Edits
              └─ Unit & Integration Tests Pass                      └─ Stacked Diff Decomposition (Meta)
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 STEP 3: CONVENTIONAL COMMIT (CAVEMAN FORMAT)                │
        │  • <type>(<scope>): <subject <=50 chars> • Terse "Why" Body • No Fluff      │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [STEP 4: BRANCH PROTECTION & REMOTE PUSH]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🔀 REBASE    │           │ 🔐 GPG SIGN  │           │ 🚀 GIT PUSH  │
            │ Clean History│           │ Verified Line│           │ Upstream PR  │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Version Control

1. **No Broken Commits on Main**: Every commit must compile cleanly and pass 100% of tests.
2. **One Logical Change Per Commit**: Staging must be atomic. Never combine unrelated UI tweaks, database migrations, and refactorings into a single monolithic commit.
3. **Conventional Commits**: Commit messages must follow `<type>(<scope>): <subject>` where `<type>` is `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `chore`.
4. **Subject Length Limit ($\le 50$ chars)**: Subject must be concise, written in imperative present tense ("add", "fix", not "added", "fixes").
5. **No Secrets in History**: Pre-commit hooks (`gitleaks`) must actively prevent staging `.env` files, API keys, or private certificates.
6. **Stacked Diffs (Meta Standard)**: Large features must be split into sequential, small pull requests ($\sim 35 - 100$ lines) building upon one another.

---

## 🔬 The 4-Step Git Pipeline

### Step 1: Pre-Commit Compilation & Quality Gate
- Run `npx tsc --noEmit` and `npm run test` before staging.
- Ensure 0 errors, 0 unresolved merge conflicts, and 0 linter warnings.

### Step 2: Atomic Staging & Stacked Diffs
- Inspect status via `git status` and `git diff`.
- Stage related files together:
  ```bash
  # Stage contract first
  git add src/types/payment.ts src/schema/payment.prisma
  ```

### Step 3: Conventional Commit (Caveman Commit)
- Format:
  ```text
  feat(billing): enforce idempotency key on charge endpoint
  ```
- If explanation is necessary, keep body ultra-terse:
  ```text
  feat(billing): enforce idempotency key on charge endpoint

  Prevents double-charging customers during transient network retries.
  Caches UUIDv4 keys in Upstash Redis for 24h.
  ```

### Step 4: Rebase & Push
- Rebase on latest upstream main before pushing:
  ```bash
  git fetch origin
  git rebase origin/main
  git push origin feature/my-feature-branch
  ```
