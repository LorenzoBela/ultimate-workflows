---
name: ultimate-best-practices-workflow
description: >
  Master workflow for engineering best practices across React, Next.js, Expo,
  Android Native, and general clean code.
  Coordinates compound composition, RSC boundaries, Hermes engine optimizations, Jetpack Compose,
  and senior-level software craftsmanship.
  Triggers on "ultimate best practices", "/ultimate-best-practices-workflow", or when
  initiating component refactoring or multi-platform native development.
argument-hint: "[react | nextjs | expo | android-native | clean-code]"
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

# Ultimate Engineering Best Practices Workflow

This workflow enforces production-grade engineering standards and platform-native conventions across React, Next.js, Expo/React Native, Android Native, and general software architecture.

---

## 1. Core React & Composition Patterns
*   **Sub-skills:** `vercel-composition-patterns`, `vercel-react-best-practices`
*   **Best Practices:**
    1. **Avoid Boolean Prop Proliferation:** Do not customize component behavior by adding endless boolean flags. Use Compound Components (with shared context) to compose complex children.
    2. **State Management:** Decouple state management logic. Keep context interfaces generic with clear state and action boundaries.
    3. **React 19 Standards:** (If using React 19) Avoid `forwardRef`; pass refs as standard props. Use the `use()` hook for consuming context or promises dynamically.
    4. **Separate Logic from Render:** Extract complex logic, API queries, or event handlers into custom hooks (e.g. `useOrderDetails`) to keep rendering components clean.
    5. **Performance:** Apply `useMemo`, `useCallback`, and `React.memo` judiciously. Profile with React DevTools before optimizing.

## 2. Next.js (App Router) Best Practices
*   **Sub-skills:** `next-best-practices`, `vercel-react-best-practices`
*   **Best Practices:**
    1. **Server vs. Client Components (RSC):** Default all components to React Server Components (RSC) for faster page loads. Move interactive behaviors (inputs, buttons, hooks) to leaf-level Client Components using `"use client"`.
    2. **Data Fetching:** Fetch data at the component level using native async/await. Avoid nesting multiple fetches that block rendering (waterfalls); run independent fetches in parallel (`Promise.all`).
    3. **Route Handlers:** Write REST endpoints in `route.ts`. Return structured JSON with consistent error formats and HTTP status codes.
    4. **Metadata & SEO:** Use the `generateMetadata` export for dynamic page titles, descriptions, and Open Graph tags.
    5. **Image & Font:** Use `next/image` with explicit width/height to prevent CLS. Use `next/font` for zero-layout-shift font loading.

## 3. Expo & React Native Best Practices
*   **Sub-skills:** `vercel-react-native-skills`, `react-native-best-practices`, `react-native-best-practices-callstack`
*   **Best Practices:**
    1. **Performance Tuning:** Keep the JS thread free of heavy operations. Memoize expensive computations (`useMemo`) and callbacks (`useCallback`) to avoid unnecessary re-renders.
    2. **Virtual Lists:** For lists containing 50+ elements, use `FlashList` (Shopify) instead of `FlatList` to recycle item views and prevent frame drops.
    3. **Mobile Layout Constraints:** Respect top/bottom safe areas (Dynamic Island, navigation bars). Use `KeyboardAvoidingView` with correct behavioral offsets to prevent input fields from being covered by the keyboard.
    4. **Touch Targets:** Verify all tap targets are at least 44×44pt. Use `hitSlop` to extend tap ranges on smaller UI icons.
    5. **Hermes Engine:** Optimize for Hermes bytecode compilation. Avoid `eval()`, dynamic `require()`, and Proxy objects.
    6. **Animations:** Use Reanimated for 60fps UI thread animations. Never animate on the JS thread for gestures or scroll-driven effects.

## 4. Android Native Development Best Practices
*   **Sub-skills:** `android-native-dev`
*   **Best Practices:**
    1. **Jetpack Compose:** Use declarative layout structures. Host state in ViewModels and hoist state parameters to keep UI composables stateless and testable.
    2. **Concurrency:** Execute async and IO actions on background threads using Kotlin Coroutines with appropriate dispatchers (`Dispatchers.IO` for storage/network).
    3. **Architecture:** Enforce Clean Architecture with a strict separation between UI layers (Composables, ViewModels), Domain layers (UseCases, Entities), and Data layers (Repositories, DB/API).
    4. **Material Design 3:** Use official M3 components and token scales for colors, typography shapes, and transitions.

## 5. Senior-Level Craftsmanship (Clean Code)
*   **Sub-skills:** `kaizen`, `ponytail`, `superpowers-review`
*   **Best Practices:**
    1. **Single Responsibility:** A module or function should do exactly one thing and do it completely. If a function exceeds 50 lines, evaluate splitting it.
    2. **Fail Fast:** Validate inputs and configurations early. Raise descriptive, operational exceptions immediately instead of allowing null values to propagate.
    3. **YAGNI (You Ain't Gonna Need It):** Do not write code, abstractions, or configurations for speculative future requirements. Keep code bases minimal.
    4. **Self-Documenting Code:** Write clean, intention-revealing variable and function names. Use comments only to explain *why* a specific tradeoff or limitation exists, not *what* the code does.
    5. **Continuous Improvement:** Apply `kaizen` principles for iterative code quality improvements. Use `superpowers-review` for structured severity-rated code audits.

## 6. Design System & UI Quality
*   **Sub-skills:** `ui-ux-pro-max`, `ckm:design-system`, `ckm:ui-styling`, `web-design-guidelines`, `web-artifacts-builder`, `theme-factory`
*   **Best Practices:**
    1. **Token Architecture:** Build three-layer design tokens (Primitive → Semantic → Component) and sync to CSS variables.
    2. **Accessibility:** WCAG 4.5:1 contrast, `aria-label` on icon buttons, visible focus rings, `prefers-reduced-motion` compliance.
    3. **Responsive:** Test at 375px / 768px / 1024px / 1440px breakpoints. No content hidden behind fixed elements.
    4. **Theming:** Use `theme-factory` for pre-set theme application. Support light/dark modes via token-driven contrast.

## 7. Validation & Linting
*   **Sub-skills:** `lint-and-validate`, `systematic-debugging`, `superpowers-tdd`
*   **Best Practices:**
    1. Run linters, type-checkers, and formatters after every code change.
    2. Use `systematic-debugging` for any test failure or unexpected behavior before proposing fixes.
    3. Enforce strict TypeScript mode with no `any` types unless explicitly justified.
    4. Apply `superpowers-tdd` test-driven development for all critical path logic (Red → Green → Refactor).

## 8. Code Review & Audit
*   **Sub-skills:** `superpowers-review`, `caveman-review`, `ponytail-review`, `ponytail-audit`, `ponytail-debt`
*   **Best Practices:**
    1. Use `superpowers-review` for severity-rated code quality audits (Blocker / Major / Minor / Nit).
    2. Use `caveman-review` for terse, one-line-per-finding review feedback.
    3. Use `ponytail-review` to flag over-engineering, speculative abstractions, and unnecessary wrappers.
    4. Use `ponytail-audit` and `ponytail-debt` to scan for deferred technical debt and code bloat.

---

## Cross-Cutting Concerns
*   **Research:** Use `tavily-search`, `context7/get-library-docs`, and `perplexity-ask` for best-practice research and framework documentation.
*   **Memory:** Use `memory` MCP to persist best-practice decisions and code quality standards across conversations.
*   **Security:** Apply `ultimate-security-workflow` and `ultimate-security-audit-workflow` for security-first development practices.
*   **Documentation:** Use `ultimate-documentation-workflow` for maintaining best-practice guides and code standards documentation.
*   **Deployment:** Use `ultimate-deployment-workflow` for CI/CD pipeline best practices and pre-release validation.
