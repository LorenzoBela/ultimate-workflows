---
name: ultimate-project-workflow
description: >
  Master workflow for agile project management, scope definition, sprint tracking,
  and walkthrough reporting.
  Coordinates task.md checklists, milestone prioritization, blocker resolution,
  and walkthrough.md generation.
  Triggers on "ultimate project workflow", "/ultimate-project-workflow", or when scoping
  requirements, creating task lists, or documenting final deliverables.
argument-hint: "[task-scoping | sprint-tracking | walkthrough-report]"
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

# Ultimate Project & Task Management Workflow

This workflow drives systematic feature scoping, sprint milestone tracking, blocker resolution, and complete walkthrough reporting to ensure deliverables are clear, prioritized, and fully verified.

---

## The 4-Phase Project Pipeline

### Phase 1: Requirements Scoping & User Stories
*   **Sub-skills:** `superpowers-brainstorm`, `concise-planning`, `sequential-thinking/sequentialthinking`
*   **Action:**
    1. Define the project scope and end goal. List primary constraints, business dependencies, and target audience needs.
    2. Write clear user stories (`As a <role>, I want <feature>, so that <benefit>`).
    3. Establish explicit acceptance criteria for each story before beginning development.
    4. Use `superpowers-brainstorm` for divergent requirement exploration and `concise-planning` for atomic task generation.
    5. Use `sequentialthinking` to trace dependencies between user stories and identify critical path items.

### Phase 2: Milestone Prioritization (MoSCoW)
*   **Sub-skills:** `kaizen`, `ponytail`, `superpowers-plan`
*   **Action:**
    1. Group tasks into logical, incremental milestones (Milestone 1, 2, 3).
    2. Prioritize tasks using the MoSCoW framework:
       *   **Must Have:** Critical tasks that form the Minimum Viable Product (MVP).
       *   **Should Have:** Important but non-blocking tasks.
       *   **Could Have:** Nice-to-have features or polish items.
       *   **Won't Have:** Tasks deferred to future sprints.
    3. Document dependencies between tasks to identify potential blockers early.
    4. Apply `ponytail` YAGNI to ruthlessly prune "Won't Have" items and `kaizen` for continuous scope refinement.
    5. Use `superpowers-plan` for breaking milestones into small, verifiable atomic steps.

### Phase 3: Task Checklist Execution (task.md)
*   **Sub-skills:** `lint-and-validate`, `superpowers-tdd`, `systematic-debugging`
*   **Action:**
    1. Create a dynamic task checklist file at `<appDataDir>/brain/<conversation-id>/task.md` to track execution progress.
    2. Enforce the standard planning-mode notation:
       *   `[ ]` Unstarted task.
       *   `[/]` In-progress task.
       *   `[x]` Completed task.
    3. Update `task.md` continuously at the start and completion of each development task. Keep items atomic (2–10 minutes).
    4. Run `lint-and-validate` after completing each task item.
    5. Apply `superpowers-tdd` for test-driven development on critical path items.
    6. Use `systematic-debugging` for resolving blockers encountered during execution.

### Phase 4: Walkthrough & Deliverables Verification
*   **Sub-skills:** `superpowers-review`, `caveman-review`, `ckm:slides`, `docx`
*   **MCP Tools:** `playwright`, `memory`
*   **Action:**
    1. Conduct a final integration pass against the established acceptance criteria.
    2. Create or update the `walkthrough.md` artifact at `<appDataDir>/brain/<conversation-id>/walkthrough.md` to present results.
    3. Structure the walkthrough to summarize:
       *   **Core Changes:** Exact files modified and new files created.
       *   **Test Results:** Commands run and their outcomes.
       *   **UI/UX Verification:** Embedded screenshots or screen recordings showcasing interface changes.
    4. Use `playwright` MCP for capturing browser screenshots and recording UI verification videos.
    5. Use `superpowers-review` and `caveman-review` for terse, severity-rated final code audit.
    6. Use `ckm:slides` for stakeholder presentation decks and `docx` for formal deliverable documents.
    7. Persist project outcomes and lessons learned to `memory` graph for cross-conversation recall.

---

## Cross-Cutting Concerns
*   **Research:** Use `tavily-search` and `perplexity-ask` for project management methodology research.
*   **Brand:** Use `ckm:brand` for aligning project deliverables with brand guidelines.
*   **Deployment:** Use `ultimate-deployment-workflow` for release engineering integration.
*   **Documentation:** Use `ultimate-documentation-workflow` for maintaining project READMEs and API specs.
