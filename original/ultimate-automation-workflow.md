---
name: ultimate-automation-workflow
description: >
  Master workflow for scripting, cron tasks, task runners, build automations,
  and developer CLI utilities.
  Triggers on "ultimate automation workflow", "/ultimate-automation-workflow", or when
  writing local automation scripts, build flows, or CLI utilities.
argument-hint: "[cli-script | build-automation | task-runner]"
---

# Ultimate Automation & Scripting Workflow

This workflow guides the design, implementation, and deployment of local automation, developer utilities, task scripts, and cron configurations to guarantee reliability, safe execution, and clean outputs.

---

## The 4-Phase Automation Pipeline

### Phase 1: Parameterization & Validation
*   **Sub-skills:** `lint-and-validate`, `systematic-debugging`
*   **Action:**
    1. Parse CLI arguments using standard parsing engines (e.g. `argparse` in Python, `commander` in Node, flag variables in Go).
    2. Provide descriptive, built-in help flags (`--help` or `-h`).
    3. Validate inputs, file existence, and directory permissions at startup. Fail fast with clear error messages.
    4. Support dry-run flags (`--dry-run` or `-d`) for destructive actions (e.g., mass renaming, file deletions).
    5. Run `lint-and-validate` on all script source files before executing automation jobs.

### Phase 2: Execution Safety & Idempotency
*   **Sub-skills:** `upstash-workflow-js`, `upstash-qstash-js`, `upstash-redis-js`
*   **Action:**
    1. Enforce **Idempotency**: running an automation script multiple times must yield the same clean system state (no duplicates).
    2. Create temporary file directories within the project scope (never `/tmp` or system roots). Clean up all temp assets upon script termination.
    3. Wrap core logic in `try/catch` or `defer` blocks to prevent scripts from leaving system resources open or lock files orphaned.
    4. For durable, multi-step automation flows, use `upstash-workflow-js` to define step-by-step workflows with automatic retries and failure recovery.
    5. For scheduled or delayed task execution, use `upstash-qstash-js` to publish messages to HTTP endpoints with delivery guarantees.
    6. Use `upstash-redis-js` for distributed lock management to prevent concurrent script execution collisions.

### Phase 3: Logging, Output & Formatting
*   **Sub-skills:** `caveman`, `caveman-compress`, `ponytail`
*   **Action:**
    1. Log progress information dynamically: differentiate stdout (for data outputs) and stderr (for debugging/diagnostic logs).
    2. Support silent flags (`--silent` or `-s`) to prevent log noise during cron integrations.
    3. Print structured, filterable logs (JSON or structured CSV) for analytics integrations.
    4. Apply `caveman` compression for terse log styling and `ponytail` minimalism for output brevity.

### Phase 4: Job Scheduling & CI Integration
*   **Sub-skills:** `ultimate-git-workflow`, `ultimate-deployment-workflow`, `upstash-qstash-js`
*   **Action:**
    1. Map crontab scheduling patterns or runner workflows (e.g. GitHub Actions, task runners like `npm run` or Makefile targets).
    2. Configure exit codes: return `0` on success, and custom non-zero codes on specific error failures.
    3. Set execution timeouts to prevent orphaned tasks from blocking CI runners or background schedulers.
    4. Use `upstash-qstash-js` for serverless cron scheduling with CRON expressions and automatic retries.
    5. Integrate with `ultimate-git-workflow` for pre-commit automation hooks and `ultimate-deployment-workflow` for CI/CD pipeline integration.

---

## Cross-Cutting Concerns
*   **Research:** Use `tavily-search` and `context7/get-library-docs` for discovering automation tool APIs and CLI framework documentation.
*   **Testing:** Use `superpowers-tdd` for testing automation scripts and `systematic-debugging` for diagnosing script failures.
*   **Memory:** Use `memory` MCP to persist automation run states and observations across sessions.
