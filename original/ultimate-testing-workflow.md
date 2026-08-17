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
