---
name: ultimate-testing-workflow
description: >
  Flawless 10/10 Master Workflow for testing, verification, and QA automation.
  Coordinates Test-Driven Development (TDD), Stryker mutation testing (MSI >= 90%),
  property-based testing (fast-check), Playwright E2E browser automation, visual regression diffing,
  API contract testing, Chaos fault injection, and CI coverage gates.
  Triggers on "ultimate testing workflow", "/ultimate-testing-workflow", or when
  authoring test suites, debugging test failures, or validating release quality.
argument-hint: "[test-suite | mock-payload | e2e-plan | --mutation | --fuzz | --e2e]"
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

# Ultimate Testing & QA Automation Workflow (10/10 Master Engine)

This workflow is the definitive 10/10 testing and quality assurance system. It unites the test-first discipline of **TDD (Red/Green/Refactor)**, the mutation verification of **Stryker (MSI $\ge 90\%$)**, the mathematical robustness of **Property-Based Testing (`fast-check`)**, the browser automation of **Playwright**, the fault tolerance of **Chaos Engineering**, and zero-flakiness **CI coverage gates**.

```
                                      [CODE UNDER TEST / NEW FEATURE]
                                                     │
                          ┌──────────────────────────┴──────────────────────────┐
                          ▼                                                     ▼
              [PHASE 1: TEST STRATEGY & TDD]                        [PHASE 2: CONTRACT & INTEGRATION]
              ├─ Equivalence Partitioning & Boundaries              ├─ DB Transactions & RLS Isolation
              ├─ Property-Based Fuzzing (`fast-check`)              ├─ MSW Mocking & WireMock
              └─ Red -> Green -> Refactor Loop                      └─ OpenAPI / gRPC Contract Tests
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: E2E BROWSER AUTOMATION & VISUAL QA                 │
        │  • Playwright Browser Automation • Visual Snapshot Diffing • AXE A11y Tests │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: MUTATION & CHAOS RESILIENCE]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🧬 STRYKER   │           │ 💥 CHAOS MONK│           │ 🎯 CI GATE   │
            │ MSI >= 90%   │           │ Latency/Drop │           │ 0 Flaky & 80%│
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Testing & QA

1. **Tests Are First-Class Code**: Test code must adhere to the exact same clean code, typing, and readability standards as production code.
2. **Deterministic Tests Only**: Flaky tests are bugs in the test suite. Any test that passes intermittently must be quarantined and resolved immediately.
3. **Test Behavior, Not Implementation Details**: Avoid asserting internal private state or mock interaction order unless sequencing is a business requirement.
4. **Red-Green-Refactor Discipline (TDD)**: Always write a failing test first, make it pass with the minimal `ponytail` code, then refactor.
5. **Mutation Score Indicator (MSI $\ge 90\%$)**: Unit tests must kill boundary mutants (`>` to `>=`, `&&` to `||`, statement removals). Tests that pass when code is mutated are incomplete.
6. **Property-Based Fuzzing for Critical Logic**: Financial calculations, serialization algorithms, and state machines MUST be validated using generative property testing (`fast-check` / `Hypothesis`).
7. **Transactional Isolation**: Database integration tests MUST run within transactions rolled back at teardown or within isolated ephemeral database containers.
8. **No Unhandled Async / Race Conditions**: Never use arbitrary `sleep(1000)` in tests. Use explicit event/condition polling (`await waitFor(...)`, Playwright auto-wait).

---

## 🔬 The 4-Phase Testing Pipeline

### Phase 1: Test Strategy, Vector Identification & TDD
*   **Sub-skills:** `superpowers-tdd`, `concise-planning`, `superpowers-brainstorm`
*   **Action:**
    1. **Equivalence Partitioning & Boundary Value Analysis (BVA):**
       - Test exact boundary limits: $0, 1, \text{MAX\_INT}, \text{MIN\_INT}, \text{null}, \text{undefined}, \text{""}, \text{special characters}$.
    2. **Property-Based Generative Testing (`fast-check`):**
       ```typescript
       import fc from 'fast-check';
       import { calculateDiscount } from './pricing';

       test('discount calculation preserves invariant: 0 <= finalPrice <= originalPrice', () => {
         fc.assert(
           fc.property(fc.nat(100000), fc.integer({ min: 0, max: 100 }), (priceInCents, discountPercent) => {
             const finalPrice = calculateDiscount(priceInCents, discountPercent);
             return finalPrice >= 0 && finalPrice <= priceInCents;
           })
         );
       });
       ```
    3. **Mocking Boundaries:**
       - Mock ONLY at external system boundaries (network calls, Stripe API, third-party webhooks) using MSW (Mock Service Worker).
       - Never mock internal domain services.

### Phase 2: Unit & Integration Testing
*   **MCP Tools:** `supabase-mcp-server/execute_sql`, `prisma-mcp-server/Prisma-Studio`
*   **Action:**
    1. **Integration Test DB Rollback Pattern:**
       ```typescript
       beforeEach(async () => {
         await prisma.$executeRawUnsafe('BEGIN');
       });
       afterEach(async () => {
         await prisma.$executeRawUnsafe('ROLLBACK');
       });
       ```
    2. **Postgres RLS Policy Testing:**
       - Verify Tenant A cannot read Tenant B's records under authenticated Supabase context.
    3. **Idempotency & Concurrent Conflict Testing:**
       - Dispatch two parallel mutating requests with identical `Idempotency-Key` headers; assert exact single-execution semantics.

### Phase 3: E2E Browser Testing & Visual Regression (Playwright)
*   **MCP Tools:** `playwright` (all tools)
*   **Action:**
    1. **Automated User Journeys:**
       - Test critical funnel: Unauthenticated $\rightarrow$ Sign In $\rightarrow$ Dashboard $\rightarrow$ Action $\rightarrow$ Verify State.
    2. **Playwright Resilient Selector Strategy:**
       - Use user-facing accessible locators: `page.getByRole('button', { name: 'Submit' })`, `page.getByLabel('Email')`, `page.getByTestId('checkout-card')`.
       - Ban fragile XPath and DOM hierarchy paths (`div > div:nth-child(2)`).
    3. **Visual Snapshot Testing:**
       - Capture screenshot baselines and perform pixel-differential checks across 375px, 768px, and 1280px viewports.
    4. **Automated Accessibility Testing (axe-playwright):**
       - Run axe accessibility scan on all rendered pages; fail build on WCAG AA violations.

### Phase 4: Mutation Hardening (Stryker) & CI Quality Gates
*   **Action:**
    1. **Mutation Testing Execution (Stryker):**
       - Run Stryker against test suites to verify mutants are killed.
       - Target Mutation Score Indicator: $\text{MSI} \ge 90\%$.
    2. **Simulated Fault Injection (Chaos Engineering):**
       - Intercept network calls via Playwright or MSW: inject 500ms latency, simulate 503 Service Unavailable, assert graceful client UI fallback.
    3. **CI Coverage Gates:**
       - Minimum 80% line coverage and 85% branch coverage on core domain logic.

---

## 📋 Comprehensive Test Fixture & Assertion Catalog

```typescript
// Vitest / Jest Standard Assertion Suite
import { describe, it, expect, vi, beforeEach } from 'vitest';

describe('PaymentService (10/10 Invariants)', () => {
  it('deduplicates parallel requests with matching idempotency keys', async () => {
    const key = 'uuid-v4-sample-key';
    const [res1, res2] = await Promise.all([
      paymentService.process({ key, amountInCents: 5000 }),
      paymentService.process({ key, amountInCents: 5000 })
    ]);
    expect(res1.transactionId).toBe(res2.transactionId);
    expect(res1.status).toBe('SUCCESS');
  });

  it('fails fast on negative amounts with typed DomainError', async () => {
    await expect(paymentService.process({ key: 'k2', amountInCents: -50 }))
      .rejects.toThrowError(InvalidAmountError);
  });
});
```
