---
name: ultimate-testing-workflow
description: >
  Master workflow for testing, verification, and QA automation.
  Coordinates unit, integration, end-to-end (E2E) browser testing, API mocking, and
  coverage monitoring.
  Triggers on "ultimate testing workflow", "/ultimate-testing-workflow", or when
  authoring test suites, debugging test failures, or validating release quality.
argument-hint: "[test-suite | mock-payload | e2e-plan]"
---

# Ultimate Testing & QA Workflow

This workflow drives comprehensive testing strategy to verify functional correctness, prevent regression bugs, test network failure recovery, and ensure high test coverage.

---

## The 4-Phase Testing Pipeline

### Phase 1: Test Strategy & Vector Identification
*   **Sub-skills:** `superpowers-tdd`, `sequential-thinking/sequentialthinking`, `concise-planning`, `superpowers-brainstorm`
*   **Action:**
    1. Define the testing target (unit, integration, or E2E).
    2. Identify equivalence classes and boundary conditions. Map out expected behaviors under bad inputs, edge cases (e.g. empty lists, leap years), and concurrency.
    3. Determine the mocking boundary: what external components (third-party APIs, mail services, databases) must be stubbed or mocked?
    4. Use `sequentialthinking` to trace test-critical execution paths.
    5. Use `concise-planning` for atomic test case checklists and `superpowers-brainstorm` for identifying edge-case vectors.

### Phase 2: Unit & Integration Testing
*   **Sub-skills:** `superpowers-tdd`, `supabase-postgres-best-practices`, `systematic-debugging`
*   **MCP Tools:** `supabase-mcp-server/execute_sql`, `prisma-mcp-server/Prisma-Studio`
*   **Action:**
    1. Apply Test-Driven Development (TDD): write the failing test first, build code to pass, and refactor.
    2. Write unit tests with no external network/database dependencies. Mock repository layers or database connections cleanly.
    3. Write integration tests to verify database migrations, transactions, and API controllers. Use transactional rollbacks to keep test databases clean between runs.
    4. Use `supabase-mcp-server/execute_sql` for verifying SQL query correctness in integration tests.
    5. Use `prisma-mcp-server/Prisma-Studio` for visual data inspection during test debugging.
    6. Apply `supabase-postgres-best-practices` for testing RLS policies, constraint enforcement, and query performance.
    7. Use `systematic-debugging` for diagnosing test failures with the Iron Law (root-cause before fix).

### Phase 3: E2E Browser Testing (Playwright)
*   **MCP Tools:** `playwright` (browser_navigate, browser_click, browser_fill_form, browser_snapshot, browser_take_screenshot, browser_console_messages, browser_network_requests, browser_evaluate, browser_wait_for, browser_select_option, browser_press_key, browser_type, browser_handle_dialog, browser_file_upload, browser_tabs)
*   **Sub-skills:** `web-design-guidelines`, `ui-ux-pro-max`
*   **Action:**
    1. Write end-to-end browser tests to verify complete user flows (login → dashboard → checkout).
    2. Use Playwright MCP tools to capture selectors, input form data, trigger clicks, and verify DOM states:
       *   `browser_navigate` for page navigation.
       *   `browser_fill_form` and `browser_type` for input interactions.
       *   `browser_click` for button and link interactions.
       *   `browser_snapshot` and `browser_take_screenshot` for DOM state capture.
       *   `browser_console_messages` for JavaScript error detection.
       *   `browser_network_requests` for API call verification.
       *   `browser_wait_for` for async content loading assertions.
       *   `browser_handle_dialog` for alert/confirm dialog handling.
       *   `browser_file_upload` for file upload flow testing.
    3. Test edge-case UI behaviors: handle loading skeletons, check alert banners, and verify layout reflows.
    4. Assert accessibility compliance programmatically (e.g. axe-playwright contrast checks).
    5. Apply `web-design-guidelines` and `ui-ux-pro-max` for visual regression and accessibility validation.

### Phase 4: CI Validation & Coverage Target
*   **Sub-skills:** `lint-and-validate`, `ultimate-git-workflow`, `ultimate-deployment-workflow`
*   **Action:**
    1. Configure pre-commit or CI pipeline tests. Ensure no builds compile with failing tests.
    2. Target high code coverage on core domain services (80%+). Use coverage reports to find untested branch options.
    3. Test resilience: simulate network dropouts, API timeouts, and database failures to ensure the client recovers gracefully.
    4. Run `lint-and-validate` for final compilation and linting verification alongside test execution.
    5. Integrate with `ultimate-git-workflow` for pre-commit test hooks and `ultimate-deployment-workflow` for CI pipeline test gates.

---

## Cross-Cutting Concerns
*   **Research:** Use `tavily-search` and `context7/get-library-docs` for testing framework documentation (Jest, Vitest, Playwright, Cypress).
*   **Memory:** Use `memory` MCP to persist test architecture decisions, coverage targets, and recurring failure patterns.
*   **Review:** Use `superpowers-review` and `caveman-review` for reviewing test quality and coverage gaps.
*   **React Native Testing:** Apply `react-native-best-practices` and `react-native-best-practices-callstack` for mobile-specific testing patterns.
*   **Mocking:** Use `upstash-redis-start` for spinning up ephemeral Redis instances for integration test mocking.
