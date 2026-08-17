---
name: ultimate-brainstorm-workflow
description: >
  Master workflow for structured brainstorming, architectural design spikes,
  alternative evaluation, and risk mitigation.
  Coordinates goal definition, constraint mapping, option matrices, recommendations,
  and acceptance criteria.
  Triggers on "ultimate brainstorm workflow", "/ultimate-brainstorm-workflow", or when
  initiating complex feature designs, architectural spikes, or design sprints.
argument-hint: "[design-spike | feature-brainstorm | risk-assessment]"
---

# Ultimate Brainstorming Workflow

This workflow drives systematic, divergent, and convergent technical brainstorming—assessing constraints, evaluating options through decision matrices, and mitigating risks prior to planning and implementation. It is the thinking engine that precedes all significant work.

---

## Iron Laws

1. **Never Jump to Code.** If a feature involves >2 files, >1 database table, or >1 external dependency, brainstorm first. Code without brainstorming is guessing.
2. **At Least 2 Options.** Every non-trivial decision must evaluate at least 2 distinct approaches. A "plan" with only one option is a bias, not a decision.
3. **Score, Don't Feel.** Rate options numerically (1–5 scale) on defined criteria. Gut feelings are hypotheses to be tested, not decisions.
4. **Risks Are First-Class.** Every recommendation must have an explicit risk log with mitigations. Ignoring risks is not the same as having none.
5. **Time-Box Divergence.** Brainstorming expands to fill available time. Set a hard limit: 15 minutes for divergent generation, then force convergence.
6. **No "Perfect" Solutions.** Engineering is the science of trade-offs. If an option has no drawbacks, you haven't researched it deeply enough.
7. **Document the "Why".** Write down the reasons for rejecting alternatives. Future maintainers need to know why a particular path wasn't chosen.

---

## Technical Decision Criteria & Weighting Scale

When scoring options, apply the following weights and definitions. Scoring must use a 1–5 scale where 1 is worst/most problematic and 5 is best/most optimal.

| Criterion | Weight | 1 Star (Worst) | 3 Star (Neutral) | 5 Star (Best) |
|---|---|---|---|---|
| **Complexity** | 30% | Require heavy refactoring, new paradigms, circular deps. | Fits into current architecture with minor extensions. | Self-contained, simple utility, no external state. |
| **Performance** | 20% | Blocks main thread, N+1 queries, high memory footprint. | Reasonable latency, standard db index hits. | Sub-millisecond, cache-heavy, O(1) execution. |
| **Dev Time** | 15% | Needs >1 week, complex environment configuration. | Can be completed in 2–3 days of active coding. | Resolvable within a single day/few hours. |
| **Technical Debt** | 15% | Introduces legacy dependencies, speculative abstraction. | Standard implementation, small maintenance costs. | Zero debt, standard library usage, zero dependencies. |
| **Security** | 20% | Large attack surface, auth bypass risk, client-side RLS. | Secure behind API gates with standard auth scopes. | Isolated context, zero input vector, strict server logic. |

---

## Risk Assessment Matrix (RAM)

Use this grid to classify and prioritize risks mapped during Phase 4:

```
        ┌───────────────┬───────────────┬───────────────┐
        │   Medium      │     High      │   Critical    │
 HIGH   │  (Mitigate)   │  (Mitigate)   │   (BLOCKER)   │
        ├───────────────┼───────────────┼───────────────┤
I       │    Low        │   Medium      │     High      │
M MED   │  (Monitor)    │  (Mitigate)   │  (Mitigate)   │
P       ├───────────────┼───────────────┼───────────────┤
A       │    Low        │    Low        │    Medium     │
 LOW    │  (Accept)     │  (Monitor)    │  (Mitigate)   │
        └───────────────┴───────────────┴───────────────┘
              LOW              MED            HIGH
                         L I K E L I H O O D
```

---

## The 5-Phase Brainstorming Pipeline

### Phase 1: Problem Definition & Constraints
*   **Sub-skills:** `superpowers-brainstorm`, `concise-planning`, `sequential-thinking/sequentialthinking`
*   **Action:**
    1. **The Goal Statement:** Write a single sentence: "We need to [ACTION] so that [OUTCOME] because [MOTIVATION]."
       *   *Example:* "We need to implement real-time GPS tracking so that recipients can see delivery progress because the current polling model creates 30-second stale windows."
    2. **Hard Constraints (Non-Negotiable):**
       *   Tech stack boundaries (e.g., "Must use Supabase, no Firebase migration").
       *   Performance targets (e.g., "Page load < 2s on 3G").
       *   Security requirements (e.g., "RLS on all delivery data").
       *   Backward compatibility (e.g., "Existing API consumers must not break").
    3. **Soft Constraints (Preferred):**
       *   Budget/time preferences.
       *   Team skill familiarity.
       *   Library preferences.
    4. **Known Context:** Identify the active files, database schemas, API contracts, and current system behaviors that are relevant.
    5. Use `sequentialthinking` to trace causal chains and uncover hidden dependencies.

### Phase 2: Divergent Option Generation (2–4 Options)
*   **MCP Tools:** `sequential-thinking/sequentialthinking`, `perplexity-ask/perplexity_ask`, `tavily/tavily_search`, `tavily/tavily_research`
*   **Sub-skills:** `tavily-best-practices`, `upstash`, `postgres-best-practices`
*   **Action:**
    1. Generate 2–4 distinct, genuinely different implementation approaches. Examples:
       *   **Option A: Standard library / native platform** — Use built-in APIs, zero new dependencies.
       *   **Option B: Established package** — Use a well-maintained, typed, tree-shakable library.
       *   **Option C: Custom-built module** — Build from scratch for full control and minimal footprint.
       *   **Option D: Serverless/managed service** — Offload to a managed platform (Supabase Edge Functions, Firebase Cloud Functions, Upstash).
    2. For each option, document a 3-line summary: what it does, how it works, and what it costs (time + complexity).
    3. Use `sequentialthinking` to trace the execution flow of each option, mapping state transitions and identifying edge cases.
    4. Use `perplexity_ask` for cross-referencing complex architectural patterns.
    5. Use `tavily_search` and `tavily_research` for discovering existing solutions, community patterns, and known pitfalls.

### Phase 3: Convergent Decision Matrix
*   **Sub-skills:** `kaizen`, `ponytail`, `superpowers-review`
*   **Action:**
    1. Score each option on a **1–5 scale** across the decision criteria.
    2. Calculate weighted scores. Present results in a comparison table:

       | Option | Complexity (30%) | Performance (20%) | Dev Time (15%) | Tech Debt (15%) | Security (20%) | **Total** |
       |---|---|---|---|---|---|---|
       | **A: Native WebSockets** | 3 (0.9) | 5 (1.0) | 2 (0.3) | 4 (0.6) | 4 (0.8) | **3.6** |
       | **B: Supabase Realtime** | 5 (1.5) | 4 (0.8) | 5 (0.75) | 3 (0.45) | 5 (1.0) | **4.5** |
       | **C: Firebase RTDB** | 4 (1.2) | 5 (1.0) | 4 (0.6) | 2 (0.3) | 4 (0.8) | **3.9** |

    3. **Recommendation:** Choose the winner. Explain in 2–3 sentences why the alternatives were rejected.
    4. Apply `kaizen` principles: is there an incremental improvement path rather than a big-bang rewrite?
    5. Apply `ponytail` YAGNI: reject any option that builds speculative capabilities not needed today.

### Phase 4: Risk Mapping & Mitigation
*   **Sub-skills:** `superpowers-plan`, `ultimate-security-workflow`, `systematic-debugging`
*   **Action:**
    1. For the recommended option, build a **Risk Register:**

       | # | Risk | Likelihood | Impact | Mitigation |
       |---|---|---|---|---|
       | R1 | Library abandoned | Low | High | Check npm stats, GitHub activity, have fallback plan |
       | R2 | Performance regression | Medium | High | Benchmark before/after, set CI performance budget |
       | R3 | Data migration failure | Low | Critical | Dry-run migration on staging, backup first |

    2. For each High/Critical risk, define a **concrete mitigation action** — not "be careful" but "add a CI step that runs Lighthouse and fails below score 90."
    3. Identify **rollback triggers:** what measurable condition (error rate spike, latency increase, user complaints) would cause you to revert?
    4. Apply `ultimate-security-workflow` for security-specific risk assessment.

### Phase 5: Acceptance Criteria & Handoff
*   **Sub-skills:** `superpowers-plan`, `concise-planning`
*   **Action:**
    1. Define **verifiable acceptance criteria** (not vague goals):
       *   ✅ "GPS marker updates within 2 seconds of device movement"
       *   ✅ "OTP reveal triggers when rider is within 50m (Haversine distance)"
       *   ❌ "Tracking should be fast"
    2. Break the recommended option into **small, atomic implementation steps** (2–10 minutes each) using `superpowers-plan`.
    3. Generate the atomic checklist using `concise-planning`.
    4. Persist brainstorm decisions, risk register, and acceptance criteria to the `memory` graph for cross-conversation recall.

---

## Architectural Spike Protocol

When an option's complexity is high or feasibility is uncertain, execute a time-boxed **Architectural Spike** before finalizing the brainstorm:

1. **Establish a Sandbox:** Create an isolated git branch (`spike/feature-name`) or utilize the `scratch/` directory.
2. **Set a Hard Time-Box:** Limit coding to exactly **60 minutes**.
3. **Focus on Feasibility, Not Code Quality:** Write quick, messy code to verify the API works. Ignore lint rules, test coverage, and code styling during the spike.
4. **Identify Integration Gaps:** Discover undocumented behaviors, missing types, or setup issues.
5. **Document Discoveries:** Add a `spike_results.md` log inside the scratch directory.
6. **Revert/Trash Spike Code:** Once the spike completes, discard the branch or delete the scratch files. **NEVER merge spike code directly into main branches.** Rewrite the implementation cleanly during execution.

---

## Real-world Decision Case Study: Background Queueing

### The Scenario
We need to trigger SMS notifications asynchronously when deliveries are marked `ARRIVED`. The solution must handle potential API timeouts, concurrency limits, and guarantee execution even if the web server restarts.

### Evaluated Options
*   **Option A: BullMQ (Redis-backed)**
    *   *Summary:* A robust queueing library for Node.js using Redis for message persistence.
    *   *Pros:* Extremely fast; supports rate limits, delays, retries with backoff, parent-child jobs.
    *   *Cons:* Requires provisioning and maintaining a persistent Redis instance.
*   **Option B: Upstash QStash (Serverless Queue)**
    *   *Summary:* HTTP-based message queue built for serverless environments.
    *   *Pros:* Zero-config; serverless-friendly; native retries and backoff; completely managed.
    *   *Cons:* HTTP-only delivery target; latency overhead of HTTP transport layer.
*   **Option C: Pg-boss (Postgres-backed)**
    *   *Summary:* Job queue for Node.js utilizing Postgres tables for storage.
    *   *Pros:* Uses our existing Supabase Postgres DB; transactional safety (enroll queue job in same transaction as table update).
    *   *Cons:* Increases database connection pool footprint; tables grow rapidly if cleanup jobs fail.

### Case Study Decision Matrix

| Metric | BullMQ (Redis) | QStash (Serverless) | Pg-boss (Postgres) |
|---|---|---|---|
| **Complexity (30%)** | 3 (0.9) - Needs separate Redis setup | 5 (1.5) - Simple HTTP publish | 4 (1.2) - Runs inside existing DB |
| **Performance (20%)** | 5 (1.0) - In-memory Redis speed | 4 (0.8) - HTTP call overhead | 3 (0.6) - Database writes and locks |
| **Dev Time (15%)** | 3 (0.45) - Needs Docker + Config | 5 (0.75) - Instant client setup | 4 (0.6) - Database tables migration |
| **Tech Debt (15%)** | 3 (0.45) - New infrastructure dep | 4 (0.6) - Standard SDK | 5 (0.75) - Zero new infrastructure |
| **Security (20%)** | 4 (0.8) - VPC Redis configuration | 5 (1.0) - Token-based signature | 5 (1.0) - Database RLS and VPC |
| **Weighted Total** | **3.6** | **4.65** | **4.15** |

**Recommendation:** Select **Upstash QStash**. It achieves the highest score due to its minimal complexity, fast setup in our serverless context, and zero maintenance overhead, outweighing the minor latency penalty.

---

## Case Study Option Implementations (Spike Snippets)

### 1. BullMQ Setup
```typescript
import { Queue, Worker } from 'bullmq';
import IORedis from 'ioredis';

const connection = new IORedis(process.env.REDIS_URL!);
const smsQueue = new Queue('SMSQueue', { connection });

// Add job
await smsQueue.add('sendSMS', { phone: '+123456', message: 'Arrived!' }, {
  attempts: 3,
  backoff: { type: 'exponential', delay: 1000 }
});

// Worker handler
const worker = new Worker('SMSQueue', async job => {
  await sendSMS(job.data.phone, job.data.message);
}, { connection });
```

### 2. Upstash QStash Setup
```typescript
import { Client } from '@upstash/qstash';

const client = new Client({ token: process.env.QSTASH_TOKEN! });

// Publish job via HTTP endpoint hook
await client.publishJSON({
  url: 'https://my-app.com/api/webhooks/sms',
  body: { phone: '+123456', message: 'Arrived!' },
  retries: 3
});
```

### 3. Pg-boss Setup
```typescript
import PgBoss from 'pg-boss';

const boss = new PgBoss(process.env.DATABASE_URL!);
await boss.start();

// Publish job
await boss.send('sms-queue', { phone: '+123456', message: 'Arrived!' }, {
  retryLimit: 3,
  retryDelay: 60
});

// Register worker
await boss.work('sms-queue', async job => {
  await sendSMS(job.data.phone, job.data.message);
});
```

---

## Trade-Off Documentation Log Format

Every architectural decision must document its trade-offs explicitly using this layout inside `docs/adr/`:

```markdown
### ADR Trade-off Log: [Decision Name]

*   **We chose:** [Selected Option]
*   **Because we value:** [Metric prioritized, e.g., low complexity, fast time-to-market]
*   **At the cost of:** [Metrics compromised, e.g., slightly higher network latency]
*   **Accepted Tech Debt:** [Specific deferred tasks or maintenance items]
```

---

## Pre-Mortem Audit Checklist

Before committing to the recommended decision, answer the following "Pre-Mortem" questions (assuming the implementation has failed 6 months in the future):

- [ ] *What caused it to break?* (API changes, scale, configuration, database locks)
- [ ] *Where did it fail first?* (Network timeout, memory leak, user input validation)
- [ ] *How did we notice?* (Logs, alert pager, user complaint, silent corruption)
- [ ] *How hard was it to fix?* (Minutes, hours, full database restore required)

---

## Brainstorm Output Template

```markdown
## Brainstorm: [Feature Name]

### Goal
[1-sentence goal statement]

### Constraints
- Hard: [list]
- Soft: [list]

### Options
| Option | Summary | Pros | Cons |
|---|---|---|---|
| A | ... | ... | ... |
| B | ... | ... | ... |

### Decision Matrix
[Scored comparison table]

### Recommendation
[Winner + 2-sentence rationale]

### Risk Register
[Risk table with mitigations]

### Acceptance Criteria
- [ ] [Testable criterion 1]
- [ ] [Testable criterion 2]

### Next Steps
- [ ] [Atomic implementation step 1]
- [ ] [Atomic implementation step 2]
```

---

## Anti-Patterns (Reject These)

| Anti-Pattern | Why It's Wrong | Do This Instead |
|---|---|---|
| "Let's just try it and see" | No evaluation, no rollback plan | Brainstorm → Plan → Implement |
| Single-option "brainstorm" | Confirmation bias, not analysis | Generate 2–4 genuine alternatives |
| "We might need this later" | YAGNI violation, speculative scope | Build for today, design for tomorrow |
| Risk-free claims | Every option has risks | Acknowledge and mitigate explicitly |
| Gut-feel decisions | Unauditable, personality-dependent | Score numerically on defined criteria |
| 2-hour brainstorm sessions | Diminishing returns after 30 min | Time-box: 15 min divergent, 15 min convergent |

---

## Brainstorming Session Facilitation Techniques

When running collaborative brainstorming sessions, utilize the following structured techniques to prevent groupthink and stimulate divergent ideas:

### 1. Crazy Eights (Sketching Phase)
*   **Goal:** Sketch 8 distinct ideas in 8 minutes.
*   **Method:** Fold a sheet of paper into 8 panels. Set a timer for 8 minutes. In each minute, sketch or write one rough idea, UI wireframe, or system architecture flow.
*   **Rule:** Speed over detail. Do not self-censor.

### 2. Silent Brainstorming & Sticky Sorting
*   **Goal:** Generate initial options without verbal influence.
*   **Method:**
    1. Set a 10-minute silent timer.
    2. Everyone writes ideas on post-its/virtual boards individually.
    3. Group sticky notes into cluster themes (affinity mapping).
    4. Silently vote on clusters using dot voting (each member gets 3 dots).

### 3. Round Robin
*   **Goal:** Ensure equal participation and voice.
*   **Method:** Go around the circle/meeting room. Each person presents exactly one idea or option. No evaluations or criticisms are allowed until everyone has contributed.

### 4. Reverse Brainstorming
*   **Goal:** Uncover failure paths and hidden flaws.
*   **Method:** Instead of asking "How do we solve this?", ask "How do we make it fail completely?" / "How do we maximize user friction?".
*   **Why it works:** It is often easier for developers to find flaws and security vulnerabilities when prompted with negative patterns.

### 5. SCAMPER Model
*   **Goal:** Iterate on existing architectures systematically.
*   **Method:** Evaluate the current design against 7 modification vectors:
    *   **Substitute:** What library/API can we substitute?
    *   **Combine:** Can we combine these two endpoints/tables?
    *   **Adapt:** Can we adapt a pattern from another domain?
    *   **Modify/Magnify:** Can we modify the database index structure to magnify performance?
    *   **Put to another use:** Can we use the cache memory for session state?
    *   **Eliminate:** Can we eliminate this intermediate class/wrapper?
    *   **Reverse/Rearrange:** Can we rearrange the steps of the delivery sequence?

### 6. Facilitator Prompt Cheat Sheet
When discussions stall or options seem identical, use the following prompts:
- *"If we had to build this in exactly 2 hours, what would we cut?"* (Locates core value)
- *"If budget was unlimited but execution latency had to be under 1ms, how would we rewrite this?"* (Locates performance boundaries)
- *"What is the most boring, standard way to solve this?"* (Locates baseline)
- *"What happens if our user base grows by 100x overnight?"* (Locates scalability bottlenecks)

### 7. Brainstorm Session Outputs Checklist
At the conclusion of the brainstorming meeting or spike, confirm the following artifacts are produced:
- [ ] Goal statement written in the ADR or workspace readme.
- [ ] Weighted Decision Matrix table completed with at least 2 options.
- [ ] At least 3 major risks identified with corresponding mitigations in the risk register.
- [ ] A dedicated markdown code spike log file (if a technical spike was performed).
- [ ] An atomic implementation plan checked into the workspace.

---

## Sub-Skill Checklists & Reference Templates

### 1. Scoping Guidelines (`superpowers-brainstorm`)
*   **Goal:** Define high-level target in 1–2 sentences.
*   **Constraints:** Identify technology stack limitations, time allocations, compatibility requirements, performance targets, and "must not change" guidelines.
*   **Known Context:** Establish what exists today: relevant files, components, and current system behaviors.
*   **Risks:** List security concerns, data loss vectors, regression opportunities, or surprising side effects.
*   **Options (2–4):**
    *   *Summary:* Approach description.
    *   *Pros / Cons:* Strategic tradeoffs.
    *   *Complexity / Risk:* Score from 1 to 5.
*   **Recommendation:** Select one option and provide full technical justification.
*   **Acceptance Criteria:** Verifiable bullet list of outcomes.

### 2. Checklist Guidelines (`concise-planning`)
*   **Atomic:** Each task should represent a single logical unit of work.
*   **Verb-First:** Actions must start with active verbs (e.g. "Add...", "Refactor...", "Verify...").
*   **Concrete:** Specify file basenames or modules.

### 3. Full-Stack Layering & Scoping Patterns (`fullstack-dev`)
*   **Feature-First Project Organization:** Structure codebases by feature domains (e.g., `/features/deliveries/`, `/features/payments/`) containing respective controllers, hooks, and tests together. This isolates features and prevents circular dependencies.
*   **Layer Boundaries:** Ensure architectural spikes split logic into:
    *   **Controller Layer:** Validates incoming payloads (DTOs) and maps HTTP statuses.
    *   **Service Layer:** Executes transactions, aggregates data, and enforces rules.
    *   **Repository Layer:** Reads/writes to DB client directly.
*   **API Choice Guide:** Choose tRPC/REST for standard internal Web app flows, GraphQL for client-customisable data aggregations, and gRPC for service-to-service communication.

### 4. Technical Document Specifications (`docx`)
*   **Engineering ADR Documents:** When generating technical specifications, use a consistent layout:
    *   Page size set to Letter standard (12240 x 15840 DXA).
    *   Table layouts using explicit double-border dividers and cell width percentages.
    *   All images linked in reports must define descriptive alternate text (`altText`).

### 5. Architectural Decision Record Template (`docx`)
Engineering decisions must be formalized using this structure:
```markdown
# ADR: [Title of Decision]
*   **Status:** [Proposed / Accepted / Rejected]
*   **Date:** [Date]
*   **Deciders:** [Name, Name]

## Context
[Describe the technical problem, user needs, and limitations we are facing today]

## Decision
[Clearly state the chosen option and why it was picked over alternatives]

## Consequences
- **Pros:** [Positive impacts, performance gains, safety improvements]
- **Cons:** [New complexities, dependencies introduced, refactoring cost]
```

### 6. Decision Matrix Score Calculator (`concise-planning`)
Use this utility script to automate decision matrix weighting calculations:
```javascript
const criteriaWeights = { complexity: 0.3, performance: 0.2, devTime: 0.15, techDebt: 0.15, security: 0.2 };

const options = [
  { name: "A: Native WebSockets", complexity: 3, performance: 5, devTime: 2, techDebt: 4, security: 4 },
  { name: "B: Supabase Realtime", complexity: 5, performance: 4, devTime: 5, techDebt: 3, security: 5 }
];

options.forEach(opt => {
  let score = 0;
  for (let key in criteriaWeights) {
    score += opt[key] * criteriaWeights[key];
  }
  console.log(`${opt.name}: Score = ${score.toFixed(2)}`);
});
```

---

## Cross-Cutting Concerns
*   **Planning:** Feed brainstorm outputs directly into `ultimate-planning-workflow` for implementation planning.
*   **Research:** Use `tavily-search`, `tavily-research`, `tavily-extract`, `perplexity-ask`, and `context7/get-library-docs` for validating technical assumptions.
*   **Documentation:** Use `ultimate-documentation-workflow` and `docx` to formalize brainstorm outputs into ADR documents.
*   **Presentation:** Use `ckm:slides` to create strategic HTML presentations of brainstorm outcomes with Chart.js decision matrices.
*   **Architecture:** Feed architectural brainstorms into `ultimate-architecture-workflow` for ER diagrams and system design.
*   **Memory:** Use `memory` MCP to persist brainstorm decisions and rationale across conversations.
