---
name: ultimate-security-audit-workflow
description: >
  Flawless 10/10 Master Workflow for automated security vulnerability audits, static code analysis (SAST),
  dependency CVE scans, OWASP Top 10 penetration testing vectors, SLSA Level 3 supply chain checks,
  and regulatory compliance (SOC2, GDPR, HIPAA).
  Triggers on "ultimate security audit workflow", "/ultimate-security-audit-workflow",
  or when auditing dependencies, setting up SAST, checking compliance, or verifying OWASP.
argument-hint: "[cve-scan | compliance-check | sast-audit | --owasp | --supply-chain]"
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

# Ultimate Security Auditing & Compliance Workflow (10/10 Master Engine)

This workflow drives systematic static code analysis (SAST), software composition analysis (SCA / CVEs), automated secrets detection, supply-chain verification (SLSA 3), and regulatory compliance mapping.

```
                                      [REPOSITORY AUDIT TARGET / PR DIFF]
                                                        │
                          ┌─────────────────────────────┴─────────────────────────────┐
                          ▼                                                           ▼
              [PHASE 1: DEPENDENCY SCA & CVE AUDIT]                         [PHASE 2: SAST & SECRETS SCAN]
              ├─ Automated CVSS Scans (Trivy / Snyk)                        ├─ Semgrep / AST Security Rules
              ├─ Lockfile Pinned Hashes & SLSA Level 3                      ├─ GitLeaks & TruffleHog Secrets Scan
              └─ Vulnerability Mitigation Matrix                            └─ Source-to-Sink Dataflow Tracking
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: OWASP TOP 10 PENETRATION AUDIT MATRIX              │
        │  • Injection • Broken Auth • SSRF • Cryptographic Failures • Security Misconfig│
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: REGULATORY COMPLIANCE MAPPING]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🇪🇺 GDPR/CCPA │           │ 🏢 SOC 2 TYPE│           │ 🏥 HIPAA PII │
            │ Data Deletion│           │ Audit Logs   │           │ Encryption   │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Security Auditing

1. **Zero High/Critical CVEs Allowed in Production**: Any dependency with a CVSS score $\ge 7.0$ (High/Critical) is an unconditional blocker.
2. **Deterministic Lockfile Integrity**: All dependencies must be strictly pinned with cryptographic integrity hashes (`package-lock.json`, `pnpm-lock.yaml`).
3. **AST Source-to-Sink Verification**: Track untrusted input sources (`req.body`, `searchParams`) to dangerous execution sinks (`eval`, `innerHTML`, `exec`, unparameterized queries).
4. **Automated Pre-Commit Secrets Scanning**: Commits containing API keys, private keys, or passwords must be blocked at pre-commit gates (`gitleaks`).
5. **Continuous Compliance Governance**: SOC2, GDPR, and HIPAA controls must be represented as automated unit/integration test assertions.

---

## 🔬 The 4-Phase Security Audit Pipeline

### Phase 1: Software Composition Analysis (SCA) & CVE Triage
*   **Action:**
    1. Run automated vulnerability scans: `npm audit`, `trivy fs .`, `pip-audit`.
    2. Grade vulnerabilities by CVSS score:
       - **Critical ($9.0 - 10.0$):** Immediate merge blocker. Upgrade or replace package.
       - **High ($7.0 - 8.9$):** Blocker unless an isolated workaround is formally verified.
       - **Medium ($4.0 - 6.9$):** Planned for immediate next sprint cycle.

### Phase 2: Static Application Security Testing (SAST) & Secrets Scanning
*   **Action:**
    1. **Semgrep / AST-Grep Custom Rules:**
       - Detect raw HTML injection, dynamic code evaluation, and unparameterized database queries.
    2. **Deep History Secrets Detection (GitLeaks / TruffleHog):**
       - Scan entire git history for leaked tokens, private keys, and OAuth client secrets.
       - If a secret is detected in git history, treat as compromised immediately: rotate credential + rewrite history.

### Phase 3: OWASP Top 10 Deep Audit Protocol
*   **Action:**
    1. **A01: Broken Access Control:** Audit every API route for user-ownership validation.
    2. **A02: Cryptographic Failures:** Ensure TLS 1.3 in transit, AES-256/ChaCha20 at rest, Argon2id for passwords.
    3. **A03: Injection:** Audit all SQL, NoSQL, OS command, and template interpolations.
    4. **A04: Insecure Design:** Validate rate limits, transaction timeouts, and circuit breakers.
    5. **A05: Security Misconfiguration:** Verify default credentials removed, debug routes disabled, verbose stack traces redacted.
    6. **A07: Identification & Auth Failures:** Verify brute-force lockout, session invalidation on logout.
    7. **A10: Server-Side Request Forgery (SSRF):** Restrict outbound URL fetchers to strict domain allowlists; block loopback addresses (`127.0.0.1`, `169.254.169.254`).

### Phase 4: Regulatory Compliance Mapping (SOC2, GDPR, HIPAA)
*   **Action:**
    1. **GDPR / CCPA:** Verify automated data export (`GET /api/user/export`) and hard deletion cascades (`DELETE /api/user/account`).
    2. **SOC 2 Type II:** Verify tamper-proof audit trails for administrative access, role elevation, and security configuration edits.
    3. **HIPAA / PCI-DSS:** Verify PII / cardholder data isolation, tokenization, and encryption key segregation.
