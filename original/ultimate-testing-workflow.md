---
name: ultimate-testing-workflow
description: >
  Engineering workflow for testing, verification, and QA automation.
  Coordinates Test-Driven Development (TDD), Stryker mutation testing (project mutation threshold),
  property-based testing (fast-check), Playwright E2E browser automation, visual regression diffing,
  API contract testing, Chaos fault injection, and CI coverage gates.
  Triggers on "ultimate testing workflow", "/ultimate-testing-workflow", or when
  authoring test suites, debugging test failures, or validating release quality.
argument-hint: "[test-suite | mock-payload | e2e-plan | --mutation | --fuzz | --e2e]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate Testing & QA Automation Workflow (Engineering Workflow)

This workflow is the risk-based testing and quality assurance system. It unites the test-first discipline of **TDD (Red/Green/Refactor)**, risk-appropriate **mutation analysis**, the mathematical robustness of **Property-Based Testing (`fast-check`)**, the browser automation of **Playwright**, the fault tolerance of **Chaos Engineering**, and visible flake handling and project-specific **CI coverage gates**.

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
            │ project mutation threshold   │           │ Latency/Drop │           │ 0 Flaky & 80%│
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Testing & QA

1. **Tests Are First-Class Code**: Test code must adhere to the exact same clean code, typing, and readability standards as production code.
2. **Flake visibility**: Capture intermittent outcomes and investigate cause; quarantine only with an owner, issue, expiry and visible original failure. Do not assume every intermittent failure originates in the test.
3. **Test Behavior, Not Implementation Details**: Avoid asserting internal private state or mock interaction order unless sequencing is a business requirement.
4. **Red-Green-Refactor Discipline (TDD)**: For a defect, first reproduce its symptom on the baseline when feasible, repair it, then refactor. For reversible low-impact changes use proportionate verification; avoid tests that merely mirror implementation.
5. **Mutation analysis (project-configured threshold)**: Apply the project-configured mutation threshold and inspect meaningful boundary mutants (`>` to `>=`, `&&` to `||`, statement removals). Investigate surviving mutants; equivalent mutants do not automatically imply an incomplete test.
6. **Property-Based Fuzzing for Critical Logic**: Financial calculations, serialization algorithms, and state machines MUST be validated using generative property testing (`fast-check` / `Hypothesis`).
7. **Transactional Isolation**: Use an injected transaction-scoped client only when every operation shares it. For HTTP/worker tests that cannot join it, use disposable DB/schema resources isolated per worker. Separate raw BEGIN/ROLLBACK calls on a pooled root client do not provide isolation.
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
       - Prefer real domain behavior; use internal seams only when isolation is necessary and contract tests cover their integration.

### Phase 2: Unit & Integration Testing
*   **MCP Tools:** `supabase-mcp-server/execute_sql`, `prisma-mcp-server/Prisma-Studio`
*   **Action:**
    1. **Integration Test DB Rollback Pattern:**
       ```typescript
       // Prisma v6 illustrative pattern: inject tx into ALL participating code.
       // A successful callback commits; the sentinel below deliberately rolls back.
       const ROLLBACK = Symbol('test rollback');
       try {
         await prisma.$transaction(async (tx) => {
           const service = makeService({ db: tx });
           await exerciseAndAssert(service);
           throw ROLLBACK;
         });
       } catch (error) {
         if (error !== ROLLBACK) throw error; // assertion failures remain failures
       }
       // Verify fixture absence from an independent connection afterward.
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
       - Use the configured mutation threshold on relevant changed behavior; report equivalent/uncovered/time-out outcomes.
    2. **Simulated Fault Injection (Chaos Engineering):**
       - Intercept network calls via Playwright or MSW: inject 500ms latency, simulate 503 Service Unavailable, assert graceful client UI fallback.
    3. **CI Coverage Gates:**
       - Example configurable targets: 80% line and 85% branch coverage on core domain logic; use project risk and baseline policy, not universal gates.

---

## 📋 Comprehensive Test Fixture & Assertion Catalog

```typescript
// Vitest / Jest Standard Assertion Suite
import { describe, it, expect, vi, beforeEach } from 'vitest';

describe('PaymentService (Behavioral Invariants)', () => {
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

## Fixtures, recovery and evidence

Record actual tool versions and commands; snippets are adaptation templates until compiled against the selected project. Name disposable resources by run/worker; limit cleanup to owned resources. Verify rollback and cleanup with an independent connection. Never run destructive fixtures against production. Concurrency tests inspect persisted side-effect counts, not just equal response IDs.

Capture property-test seeds and shrinking counterexamples for replay. Generate valid business-domain values and malformed inputs; broad numeric bounds alone do not define correctness. Reset clocks, randomness, mocks and resources. Record baseline failures separately. Quarantines need an owner, issue and expiry; log first-attempt outcomes and retries without hiding a reproducible failure.

The 90% mutation and coverage figures above are example targets; project risk/configuration determines gates. Report equivalent, uncovered and timed-out mutants separately. Never install a new mutator merely to meet an illustrative threshold. Relevant tests can fail on baseline or already pass as regressions. Report passed, failed, unrun and unavailable checks separately; automated axe results do not prove manual accessibility criteria.
