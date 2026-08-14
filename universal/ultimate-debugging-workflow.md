---
name: ultimate-debugging-workflow
description: >
  Master workflow for troubleshooting, isolating, and resolving technical issues.
  Integrates root-cause tracing, sequential hypothesis testing, border instrumentation,
  and TDD regression protection.
  Triggers on "ultimate debugging workflow", "/ultimate-debugging-workflow", or when
  debugging runtime/compile errors.
argument-hint: "[error-message | bug-description]"
---

# Ultimate Debugging Workflow

This workflow drives systematic debugging to guarantee that bugs are root-caused, isolated, fixed cleanly, and permanently tested against regressions. It enforces discipline over gut-feel patching.

---

## Iron Laws

1. **THE IRON LAW:** Do not write ANY fix until the root cause is fully understood and verified. Symptom patching creates more bugs.
2. **One Variable at a Time.** When testing a hypothesis, change exactly ONE thing. If the fix doesn't work, revert immediately before testing the next hypothesis.
3. **3-Strike Reboot.** If 3 consecutive fix attempts fail, STOP coding. Return to investigation. The bug is not where you think it is.
4. **Reproduce First.** If you cannot reproduce it, you cannot fix it. Build an automated reproduction before attempting any fix.
5. **Test the Fix, Not the Symptom.** The regression test must verify the root cause is resolved, not just that the error message disappeared.
6. **No "Magic" Fixes.** If the error disappears without you understanding why, you haven't fixed the bug; you've just hidden it.
7. **Mitigate First, Root-Cause Second (Google SRE Standard).** During an active incident or breaking bug, **stop the bleeding immediately** (rollback release, toggle feature flag, shed load) BEFORE conducting deep root-cause investigation.
8. **High-Cardinality Traceability Invariant (OpenTelemetry Standard).** Every debug log or exception trace MUST be tagged with high-cardinality metadata: `trace_id`, `user_id`, `tenant_id`, `commit_sha`, and `feature_flag_state`.
9. **Idempotent Retry Guarantee (Stripe Fintech Standard).** Fixes for network timeouts or partial failures MUST incorporate idempotency keys or transaction state machines to allow safe retries without side-effect corruption.
10. **Observability-Driven Development (ODD Invariant).** Raw, high-cardinality event telemetry (not static aggregates) MUST be embedded directly into code path boundaries before deployment to allow instant production querying.
11. **Transactional Outbox Mandate.** Never perform dual-writes across service boundaries (e.g. DB write + API call) in an uncoordinated manner. Use the Transactional Outbox pattern: write the event to an outbox table within the same SQL transaction as the state change.
12. **Full Jitter Backoff Formula.** Retries MUST implement AWS Full Jitter exponential backoff: $\text{Sleep} = \text{random}(0, \min(\text{max\_delay}, \text{base\_delay} \times 2^{\text{attempt}}))$ to prevent retry storms and thundering herd failures.

---

## Google SRE, OpenTelemetry, Netflix & Stripe Debugging Standards

### 1. Google SRE 4-Loop Incident & Debugging Framework
- **Loop 1: Triage Loop (Blast Radius & SLO Burn):**
  - Assess user impact: Is the bug regional or global? Is it affecting QPS or error rate? Check SLO error budget burn rate.
- **Loop 2: Mitigate Loop ("Stop the Bleeding"):**
  - Prioritize immediate mitigation over understanding: (1) Roll back to previous clean release, (2) Toggle off offending feature flag, (3) Enable traffic shedding/fallback.
- **Loop 3: Investigate Loop (Breadth-First Telemetry):**
  - Perform breadth-first metrics inspection across the 4 Golden Signals:
    1. *Latency:* $p50, p95, p99$ response times.
    2. *Traffic:* QPS / incoming request rate.
    3. *Errors:* HTTP status codes (5xx vs 4xx).
    4. *Saturation:* CPU, memory, DB connection pool utilization.
- **Loop 4: Resolve & Blameless Post-Mortem Loop:**
  - After mitigation, conduct root-cause deep trace, apply TDD regression test, and publish blameless post-mortem.

### 2. OpenTelemetry High-Cardinality Distributed Tracing
- **Trace Context Propagation:** Every request context must pass `trace_id` and `span_id` across microservice boundaries via W3C `traceparent` headers.
- **Span Correlation:** Correlate frontend client errors directly with backend database queries via shared `trace_id`.
- **High-Cardinality Attributes:** Tag span contexts with `user_id`, `tenant_id`, `environment`, `commit_sha`, and active `feature_flags`.

### 3. Netflix Resilience & Blast Radius Isolation
- **Circuit Breakers & Fallbacks:** Wrap third-party API calls (Stripe, OpenAI, Supabase) in circuit breakers with defined static fallbacks.
- **Thread Pool / Queue Load Shedding:** When downstream dependencies slow down, drop non-critical telemetry or background tasks to prevent main-thread threadpool exhaustion.
- **Chaos Experiment Guardrails:** Automated stop conditions linked to SLO alerts that terminate fault-injection tests (AWS FIS, Gremlin) if error spikes exceed limits.

### 4. Stripe Financial-Grade Idempotency, Outbox & Replay Debugging
- **Idempotency Key Verification:** Every state-mutating request MUST evaluate an `Idempotency-Key` header stored in Redis/DB to guarantee that retries on network timeout return the original cached response without re-executing business logic.
- **Transactional Outbox Pattern:** Atomically write business logic mutations and event messages to an `outbox` table in the exact same SQL transaction to guarantee at-least-once delivery.
- **Append-Only Event Ledger & Replay:** Log state transition deltas into an immutable event log, allowing exact replay of production bug scenarios in local isolated environments.
- **Automated Nightly Reconciliation:** Run daily ledger-vs-settlement reconciliation scripts; automatically flag discrepancies older than 24 hours as P1 bugs.

### 5. AWS & Cloudflare Full Jitter Exponential Backoff & Retry Storm Prevention
- **Full Jitter Sleep Formula:**
  $$\text{Sleep} = \text{random}(0, \min(\text{max\_delay}, \text{base\_delay} \times 2^{\text{attempt}}))$$
- **Request-to-Trace Header Injection:** Middleware MUST automatically inject `X-Request-ID`, `X-Trace-ID`, and `X-Span-ID` into all outbound HTTP requests and error responses.

---

## The 6-Step Debugging Pipeline

### Step 1: Error Capture & Environment Snapshot
*   **Action:**
    1. **Capture the exact error signature:**
       *   Full error message and stack trace.
       *   The exact input/payload that triggered it.
       *   Environment: OS, Node version, browser, device.
       *   Commit hash / branch name.
       *   Steps to reproduce (numbered, specific).
    2. **Classify the error type:**

       | Type | Examples | Typical Cause |
       |---|---|---|
       | **Compile/Build** | TypeScript errors, import resolution, missing modules | Wrong types, circular deps, misconfigured tsconfig |
       | **Runtime** | Unhandled rejection, null reference, segfault | Bad state, missing data, race condition |
       | **Logic** | Wrong output, incorrect calculation, stale data | Algorithm error, off-by-one, wrong operator |
       | **UI/Visual** | Layout broken, animation jank, wrong colors | CSS specificity, z-index, CLS, wrong token |
       | **Network** | CORS error, timeout, 4xx/5xx, failed fetch | API config, auth, rate limit, firewall |
       | **Database** | Constraint violation, migration drift, RLS denied | Schema mismatch, missing index, wrong policy |
       | **Performance** | Slow render, memory leak, high CPU | N+1 queries, missing memo, blocking main thread |

    3. Run Strict Linting & Type Validation first — many "bugs" are simply syntax, type, or lint errors.

### Step 2: Reproduction & Minimization
*   **Action:**
    1. **Reduce the problem** to the smallest possible reproduction:
       *   Can you reproduce it in a single file?
       *   Can you reproduce it with hardcoded data (removing API dependency)?
       *   Can you reproduce it in isolation (removing adjacent components)?
    2. **Write an automated reproduction:**
       *   For logic bugs: a failing unit test.
       *   For API bugs: a curl command or test script.
       *   For UI bugs: a `playwright` browser snapshot capturing the broken state.
       *   For database bugs: a SQL query via `supabase-mcp-server/execute_sql` that demonstrates the issue.
    3. **If you cannot reproduce it:**
       *   Add instrumentation logging at the suspected boundary.
       *   Check for race conditions (timing-dependent, async ordering).
       *   Check for environment-specific issues (different Node version, missing env var).

### Step 3: Root-Cause Investigation (The Deep Trace)
*   **Action:**
    1. **Trace backward** from the error point to its origin using `sequentialthinking`:
       *   Where did the bad data enter the system?
       *   What function transformed it incorrectly?
       *   What assumption was violated?
    2. **Boundary instrumentation:** Add temporary logging at each layer boundary:
       ```
       [INPUT]  → Function A → [OUTPUT/INPUT] → Function B → [OUTPUT/INPUT] → Function C → [ERROR]
       ```
       Check each boundary: where does the data first become wrong?
    3. **Common root causes checklist:**
       *   [ ] **Null/undefined propagation** — A value assumed to exist is actually null.
       *   [ ] **Off-by-one** — Loop bounds, array indexing, pagination offset.
       *   [ ] **Race condition** — Two async operations competing for shared state.
       *   [ ] **Stale closure** — React `useEffect` or callback capturing an old variable.
       *   [ ] **Type coercion** — `"5" + 3 = "53"` (string concat) vs `5 + 3 = 8` (number add).
       *   [ ] **Environment mismatch** — Different behavior in dev vs prod, different Node version.
       *   [ ] **Schema drift** — Database schema doesn't match the code's expectations.
       *   [ ] **Missing index** — Query works but is slow; `EXPLAIN` shows sequential scan.
       *   [ ] **RLS policy blocking** — Supabase query returns empty when data exists.
    4. For database issues: use `execute_sql` for direct query testing, `get_logs` for server-side errors, `Prisma-Studio` for visual data inspection, `migrate-status` for schema drift detection.
    5. Apply `PostgreSQL & Database Optimization Patterns` for database-specific root cause analysis.

### Step 4: Hypothesis Testing (Scientific Method)
*   **Action:**
    1. **Formulate 2–5 ranked hypotheses** explaining the root cause:
       ```
       H1 (Most Likely): [Description] — Test: [How to verify]
       H2 (Possible):    [Description] — Test: [How to verify]
       H3 (Unlikely):    [Description] — Test: [How to verify]
       ```
    2. **Test each hypothesis minimally:**
       *   Make the smallest possible edit that would confirm or deny the hypothesis.
       *   Run the reproduction test.
       *   **If it passes:** Hypothesis confirmed → proceed to Step 5.
       *   **If it fails:** Revert the edit COMPLETELY. Test the next hypothesis.
    3. **NEVER pile unverified fixes.** Each hypothesis test must start from a clean state.
    4. Use `perplexity_ask` for researching obscure error messages, framework-specific bugs, or undocumented behavior.
    5. **3-Strike Rule:** If 3 hypotheses fail:
       *   STOP writing code.
       *   Return to Step 3 and re-examine the trace.
       *   The bug is likely in a different location than assumed.
       *   Consider: is the reproduction itself correct?

### Step 5: Fix Implementation & Regression Protection (TDD)
*   **Action:**
    1. **Red phase (failing test):** Write a test that captures the exact bug scenario. This test MUST fail before the fix.
    2. **Green phase (minimal fix):** Apply the verified fix — the simplest, cleanest solution that makes the test pass. Follow `ponytail` principles: no over-engineering, no speculative abstractions.
    3. **Refactor phase:** Clean up the fix for readability, style, and naming. Apply `kaizen` continuous improvement.
    4. **Verify no collateral damage:**
       *   Run the full test suite — zero new failures.
       *   Run Strict Linting & Type Validation — zero new lint or type errors.
       *   Run the build — clean compilation.
    5. **Remove instrumentation:** Delete all temporary logging added during investigation.

### Step 6: Knowledge Update & Post-Mortem
*   **Action:**
    1. **Document the bug** in the memory graph:
       *   Entity: "Bug: [Brief description]"
       *   Observations: root cause, fix applied, files changed, test added.
       *   Relations: "affects" → [component], "caused-by" → [root cause pattern].
    2. **Post-mortem questions:**
       *   Why did this bug reach this stage? (Missing test? Missing validation? Missing type?)
       *   What systemic change would prevent this class of bug? (Stricter types? Better error boundaries? More integration tests?)
       *   Should this be added to the project's lint rules or CI checks?
    3. Use Concise 1-Line Actionable Review for terse, actionable review of the fix.
    4. Use `Conventional Semantic Git Commits` for a conventional, descriptive commit message: `fix(scope): brief description of root cause`.

---

## Common Web & Node.js Error Catalog

When encountering standard runtime errors, reference this troubleshooting guide:

### 1. `Error [ERR_HTTP_HEADERS_SENT]: Cannot set headers after they are sent to the client`
*   *Cause:* Attempting to send a response (e.g. `res.send()`, `res.json()`, or returning a Next.js `Response`) after a response has already been dispatched. Typically caused by missing `return` keywords in conditional gates.
*   *Vulnerable Code:*
    ```typescript
    if (!user) {
      res.status(401).json({ error: 'Unauthorized' }); // Sends response, but execution carries on
    }
    res.json({ data: 'Sensitive Info' }); // Throws ERR_HTTP_HEADERS_SENT
    ```
*   *Correct Fix:*
    ```typescript
    if (!user) {
      return res.status(401).json({ error: 'Unauthorized' }); // Explicit return terminates execution
    }
    return res.json({ data: 'Sensitive Info' });
    ```

### 2. `Error: Connect ECONNREFUSED 127.0.0.1:5432`
*   *Cause:* The database server (or target API port) is not running locally, is bound to a different port/IP interface, or the environment variable connection string is incorrect.
*   *Troubleshooting:*
    1. Verify Postgres is running locally using `docker ps` or OS services manager.
    2. Run a port connectivity check: `Test-NetConnection -ComputerName localhost -Port 5432` in PowerShell.
    3. Verify connection variables inside `.env` match active port parameters.

---

## Memory Leak Diagnosing & Resolution

Memory leaks in Node.js (accumulating heap usage leading to Out-Of-Memory crashes) require systematic isolation of reference scopes:

### 1. Common Leaks Checklist
- [ ] **Unclosed Event Listeners:** Attaching listeners to global processes (`process.on('message')`) without ever removing them.
- [ ] **Stale Closures:** Inner functions retaining references to large outer-scope variables long after execution terminates.
- [ ] **Growing Cache Maps:** Storing session tokens or calculation records in local Javascript objects (`const cache = {}`) without size boundaries or TTL invalidations.
- [ ] **Orphaned Database Connections:** Instantiating new DB connection clients inside loop iterations or API handler functions instead of referencing a shared singleton client pool.

### 2. Memory Analysis Steps
1. **Trigger Garbage Collection:** Start the process with `--expose-gc` flag. Call `global.gc()` inside profiling logs.
2. **Take Heap Snapshots:** Use Chrome DevTools or `v8.writeHeapSnapshot()` to capture allocations.
3. **Compare Allocations:** Capture Snapshot 1 (Idle state) → Run load tests (1000 requests) → Capture Snapshot 2. Check for objects that failed to clear.

---

## Async & Race Condition Debugging Guidelines

Timing-dependent errors (e.g., duplicate rows added despite validation gates) require structured analysis of execution concurrency.

### 1. Identify the Pattern
A race condition typically occurs when:
*   Two asynchronous operations are started concurrently (e.g., two parallel fetches).
*   Both operations read a shared state (e.g., check if user exists).
*   Both observe the state as valid, then proceed to write changes concurrently, resulting in duplicate data or conflicting records.

### 2. The Isolation Fix Pattern (Distributed Locks)
In serverless environments, standard local variable locks are ineffective across instances. Utilize an distributed lock pattern using Redis (via `@upstash/redis`):

```typescript
import { Redis } from '@upstash/redis';

const redis = Redis.fromEnv();

export async function processPayment(userId: string, amount: number) {
  const lockKey = `lock:payment:${userId}`;
  
  // Attempt to acquire lock for 10 seconds
  const isAcquired = await redis.set(lockKey, 'locked', { nx: true, ex: 10 });
  if (!isAcquired) {
    throw new Error('Another payment transaction is currently processing.');
  }
  
  try {
    // Perform transactional logic here
    await executePaymentWrite(userId, amount);
  } finally {
    // Always release lock in finally block
    await redis.del(lockKey);
  }
}
```

---

## Debugging Decision Tree

```
ERROR OCCURS
    │
    ├── Can you reproduce it? ──── NO ──→ Add logging at boundaries → Retry
    │                                       ↓
    │                                  Still can't reproduce?
    │                                       → Check race conditions
    │                                       → Check environment differences
    │
    YES
    │
    ├── Is it a compile/type error? ── YES ──→ Run Strict Linting & Type Validation → Fix types
    │
    NO
    │
    ├── Minimize reproduction (single file, hardcoded data)
    │
    ├── Trace backward from error to origin
    │
    ├── Formulate 2-5 hypotheses
    │
    ├── Test hypothesis 1 (smallest edit) ── PASS ──→ Write regression test → Fix
    │                                            │
    │                                           FAIL → Revert → Test H2
    │                                                        │
    │                                                       FAIL → Revert → Test H3
    │                                                                    │
    │                                                                   FAIL → STOP
    │                                                                          │
    │                                                                   Return to trace
    │                                                                   Re-examine assumptions
```

---

## Systemic Log Collection & Telemetry Standards

When debugging complex serverless and edge systems, standard `console.log` statements are insufficient. Implement structured semantic logging with distinct levels:

```typescript
type LogLevel = 'DEBUG' | 'INFO' | 'WARN' | 'ERROR' | 'FATAL';

interface LogContext {
  userId?: string;
  requestId?: string;
  durationMs?: number;
  metadata?: Record<string, unknown>;
}

export function logEvent(
  level: LogLevel,
  message: string,
  error?: Error,
  context?: LogContext
) {
  const payload = {
    timestamp: new Date().toISOString(),
    level,
    message,
    requestId: context?.requestId || process.env.REQUEST_ID,
    userId: context?.userId,
    durationMs: context?.durationMs,
    error: error ? {
      name: error.name,
      message: error.message,
      stack: error.stack,
    } : undefined,
    ...context?.metadata,
  };
  
  // Output structured JSON for logging aggregators
  console.log(JSON.stringify(payload));
}
```

### Logging Level Rules:
*   `DEBUG`: Highly verbose, execution-path tracing (disabled in production).
*   `INFO`: High-level business milestones (e.g., "Payment completed", "User logged in").
*   `WARN`: Non-fatal operational anomalies (e.g., "Database retrying connection", "Cache miss on critical item").
*   `ERROR`: Recoverable operational failures that require engineering attention but don't halt the process.
*   `FATAL`: Non-recoverable crashes (e.g., "Missing required environment variables", "Port blocked").

---

## Production Incident Post-Mortem Template

Every critical bug resolved must have a post-mortem documented in the project logbook to avoid regression and build institutional knowledge:

```markdown
# Incident Post-Mortem: [Incident ID / Date] - [Brief Bug Title]

## Executive Summary
- **Severity Level:** [Critical / High / Medium / Low]
- **Time to Detect:** [Minutes / Hours]
- **Time to Resolve:** [Minutes / Hours]
- **Impact Scope:** [Percent of users affected / key services degraded]

## Symptom & Impact Description
- What was observed by the client?
- What was the initial alert or error log that triggered the investigation?

## Root Cause Analysis (5 Whys)
1. Why did the failure occur? -> [Answer]
2. Why was that condition present? -> [Answer]
3. Why was that not detected by tests? -> [Answer]
4. Why was the system designed this way? -> [Answer]
5. Why did we not have safety guards in place? -> [Answer]

## Corrective Actions
- **Short-Term Mitigations:** [Hotfixes, rollback, scaling adjustment]
- **Long-Term Corrective Actions:** [Refactoring, stricter database constraints, missing tests]

## Prevention Checklist
- [ ] Automated regression test written and merged.
- [ ] Monitoring dashboard alert configured for this threshold.
- [ ] Schema constraints added (if applicable).
```

---

## Anti-Patterns (Reject These)

| Anti-Patterns | Why It's Wrong | Do This Instead |
|---|---|---|
| `try { ... } catch(e) {}` | Silently swallowing errors hides root causes | Log, report, or re-throw with context |
| Fixing where the error shows | Symptom patching, real bug remains | Trace to where bad data ORIGINATED |
| Piling 3+ unverified patches | Impossible to isolate which change worked | One change at a time, revert on failure |
| "It works on my machine" | Environment mismatch is the bug | Document exact repro environment |
| Debugging without reproduction | Can't verify the fix works | Reproduce first, always |
| Adding `console.log` permanently | Noise in production logs | Remove all debug logging after fix |
| Fixing without a test | Same bug will return | Write regression test BEFORE the fix |

---

## Universal Checklists & Reference Architecture

### 1. Root Cause Analysis Checklist (`systematic-debugging`)
*   **Read Error Messages:** Note stack traces, line numbers, file paths, and error codes.
*   **Reproduce Consistently:** Gather repro steps. If timing-dependent or environment-specific, gather system status before guessing.
*   **Multi-Component Diagnostic Instrumentation:**
    *   Identify boundaries (Workflow -> Build -> API -> Database).
    *   Log inputs/outputs at each boundary.
    *   Trace backward until you isolate the failing component.
*   **3-Strike Architectural Review Gate:** If 3 consecutive fix attempts fail, stop coding. Re-examine baseline constraints, code coupling, and dependencies with your partner.

### 2. Database Diagnostics (`PostgreSQL Indexing & Optimization Patterns`)
*   Identify slow read queries using `EXPLAIN (ANALYZE, BUFFERS)`.
*   Pinpoint unindexed columns under RLS policies or filters.
*   Analyze blocking locks to isolate transactions that have exceeded 1 second runtime.

### 3. Repro Script Design & Profiling (`Systematic Root-Cause Debugging`)
*   **Boundary Repro Scripts:** Create small test scripts (saved to `/scratch/repro_[bug].ts`) that run the suspect method with boundary values (empty string, maximum integers, null).
*   **Local Execution Logs:** Capture CPU/heap snap profiles using Node inspector or custom timers.

### 4. Metro Dev Server Profiling on Mobile (`React Native Performance Best Practices`)
*   **Metro Dev Console:** Trigger React Native DevTools using:
    ```bash
    # Open Metro terminal and press 'j' to open debugger, or shake device/simulator for menu
    ```
*   **Profiling Jank:** Collect a performance trace to detect JS thread blocks during UI interactions. Ensure no blocking calculations exceed 16ms (60 FPS limit).

### 5. Heap Profiling & Memory Leak Isolation (`systematic-debugging`)
*   **Write Heap Snapshot:** Write a heap snapshot programmatically in Node.js when memory consumption leaks:
    ```javascript
    import v8 from 'v8';
    import fs from 'fs';
    
    export function dumpHeapSnapshot(label: string) {
      const snapshotStream = v8.getHeapSnapshot();
      const fileName = `./scratch/heap-${label}-${Date.now()}.heapsnapshot`;
      const fileStream = fs.createWriteStream(fileName);
      snapshotStream.pipe(fileStream);
      console.log(`Heap snapshot successfully saved to ${fileName}`);
    }
    ```
*   **Playwright Flaky test debugger:** Run targeted test cases repeatedly in Playwright to isolate race conditions and transient UI bugs:
    ```bash
    # Run test repeatedly to catch race condition failures
    npx playwright test test/e2e/otp-reveal.spec.ts --repeat-each=10 --workers=1
    ```

---

## Cross-Cutting Concerns
*   **Research:** Use Web Search, Web Extraction Tool, `perplexity-ask`, and official library documentation for researching error messages, known issues, and framework-specific debugging guides.
*   **Browser Debugging:** Use Playwright / Headless Browser Automation for reproducing and diagnosing browser-based issues (DOM state, network requests, console errors, screenshots).
*   **Database Debugging:** Use `supabase-mcp-server/execute_sql`, `supabase-mcp-server/get_advisors`, `supabase-mcp-server/get_logs`, and `prisma-mcp-server/Prisma-Studio` for inspecting data states.
*   **Memory:** Use Persistent Project Memory / Scratchpad to persist bug patterns and root causes — build a project-specific bug knowledge base.
*   **Security Debugging:** Apply `ultimate-security-workflow` when the bug involves auth, permissions, or data access.
*   **Planning:** If debugging reveals a systemic issue requiring refactoring, escalate to `ultimate-planning-workflow`.
