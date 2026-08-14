---
name: ultimate-research-workflow
description: >
  Master workflow for technical research, document mining, API checks, and dependency validation.
  Combines dual-engine search (Tavily + Exa executed simultaneously),
  sequential query decomposition, and memory graph persistence.
  Triggers on "ultimate research workflow", "/ultimate-research-workflow", or when
  researching libraries, APIs, or system designs.
argument-hint: "[research-topic | search-query]"
---

# Ultimate Research Workflow

This workflow drives systematic information retrieval, document mining, API verification, and library health analysis. It guarantees that technical decisions, library choices, and API usage patterns are based on verified, up-to-date documentation — never hallucinated, assumed, or guessed.

By following this workflow, engineering teams avoid:
- Outdated API signatures causing compilation failures.
- Deprecated library features introducing technical debt.
- Severe security vulnerabilities in unverified third-party code.
- Hallucinated libraries or methods that do not exist.


---

## Iron Laws

1. **Never Assume API Syntax.** If you haven't verified an API signature against its current documentation, do not write code using it. Check first.
2. **Pin Versions.** Every library recommendation must include the exact version tested. "Use library X" without a version is incomplete research.
3. **Cite Everything.** Every finding must include a direct URL to the source. Uncited claims are hypotheses, not research.
4. **Acknowledge Staleness.** Explicitly state documentation age, last update date, and any known deprecations. Old docs are dangerous docs.
5. **Cross-Reference.** No single source is authoritative. Verify critical findings against at least 2 independent sources (official docs + community/GitHub issues).
6. **No Speculative Libraries.** Never suggest a library or package that is not published on npm or PyPI. Always check active status.
7. **Document Alternatives.** Never recommend a library without evaluating at least 2 competitors.
8. **Time-Box Research.** Limit active search and extraction to a maximum of **15 minutes**. If findings are still inconclusive, re-formulate the query decomposition.
9. **Dual-Engine Independent Submission & Comparison Mandate (Tavily + Exa).** When searching the web, ALWAYS execute queries using BOTH Tavily and Exa at the same time. **Tavily and Exa must EACH submit their own independent findings version/report.** Do NOT merge or blend their initial outputs. You MUST perform an explicit side-by-side comparison of the Tavily Version vs. Exa Version to analyze consensus, conflicting data, unique angles, and trade-offs before reaching a final decision.
10. **Zero-Vagueness Invariant & Goated Prompt Blueprint.** Never issue vague, low-signal queries (e.g., `react state`, `supabase auth`). Every MCP search invocation MUST follow the **Goated Prompt Engineering Blueprint**: combining (1) target artifact type (API signature / AST source / breaking change / benchmark), (2) exact library version pinning, (3) boolean domain scoping, and (4) explicit negative exclusions.
11. **Google Chain-of-Evidence (CoE) Zero-Phantom Reference Mandate.** Every factual claim, API signature, and metric MUST carry an explicit inline evidence tag binding it to a verified URL or registry API response. Citations generated from LLM memory are BANNED.
12. **AutoVerifier Triple Claim Extraction.** Factual assertions MUST be decomposed into structured `(Subject, Predicate, Object)` claim triples to detect cross-source contradictions and method-code misalignments before recommending solutions.

---

## Google Science One & Frontier Deep Research Standards (Google, OpenAI, AutoVerifier)

### 1. Google Chain-of-Evidence (CoE) Verifiability Architecture
- **Completeness & Correctness Invariants:**
  - *Completeness:* Every claim in a research report MUST link to a recorded evidence chain.
  - *Correctness:* Each evidence chain MUST genuinely support the attached claim (zero paraphrase drift).
- **CoE 4-Check Integrity Audit:**
  1. **Reference Verification:** 100% of citations resolved via live registry/scholarly APIs (`context7`, `tavily_extract`, `web_fetch_exa`). Zero phantom references allowed.
  2. **Metric & Score Verification:** Exact performance/bundle-size numbers verified against raw log lines or benchmark tables.
  3. **Method-Code Alignment:** Described library patterns MUST match actual source code AST declarations.
  4. **Specification Violation Check:** Enforce exact version bounds (e.g. Next.js 15, React 19).

### 2. Google PAT (Paper Assistant Tool) Semantic Segmentation & Compute Allocation
- **Dynamic Segment Compute Allocation:**
  - Segment research topics into semantic components (e.g., *API Signatures*, *Migration Paths*, *Performance Benchmarks*, *Security Hazards*).
  - Dynamically allocate search tool calls based on information density (e.g., 60% of search calls targeted at API syntax & breaking changes, 40% at benchmarks & edge cases).

### 3. AutoVerifier 6-Layer Knowledge Graph & Claim Triples
Decompose complex technical assertions into structured `(Subject, Predicate, Object)` triples before synthesizing recommendations:
- *Example:* `(Next.js 15 App Router, requires, React 19)`
- *Example:* `(Prisma v6, supports, Supabase Transaction Pooling)`
- Cross-reference triples across Tavily and Exa outputs to spot contradictions and overclaims automatically.

### 4. DeepTRACE Bi-partite Citation Matrix & Minimal Source Cover
- Construct a **Statement-by-Source Matrix** evaluating whether listed URL sources factually support each sentence in the report.
- Prune redundant or low-signal source links to output a minimal, 100%-verified evidence graph.

### 5. HiEviDR Hierarchical Evidence Graph & Progressive Gating
- **Evidence Graph Construction ($\mathcal{G} = (\mathcal{N}_\text{e} \cup \mathcal{N}_\text{c} \cup \{n_\text{conclusion}\}, \mathcal{E})$):**
  - *Evidence Nodes ($\mathcal{N}_\text{e}$):* Atomic textual or visual evidence items retrieved directly from sources.
  - *Claim Nodes ($\mathcal{N}_\text{c}$):* Intermediate reasoning statements grounded in one or more evidence nodes.
  - *Conclusion Node ($n_\text{conclusion}$):* Final analytical answer supported by the entire directed acyclic graph.
- **Progressive Gating Mechanism:**
  1. *Citation Gate:* Activates only when cited evidence matches retrieved atomic nodes in $\mathcal{N}_\text{e}$.
  2. *Claim Gate:* Activates only when cited evidence adequately supports intermediate reasoning in $\mathcal{N}_\text{c}$.
  3. *Answer Gate:* Activates final conclusions only when all precursor claim nodes are 100% verified. Failure at any gate zeroes out credit.

### 6. Span-Grounded Verbatim Substring Validation
- Every extracted claim MUST carry a verbatim quote span from its source.
- Validate every quote span via exact substring matching against the raw scraped HTML/markdown text before emitting findings. Substring mismatches are dropped immediately.

---

## Goated Prompt Engineering & MCP Invocation Master Blueprint

To extract maximum signal and eliminate generic "AI slop" search responses, use this exact prompt construction formula for every MCP call:

### 1. The Pinpoint Query Engineering Formula
$$\text{Query} = \text{[Scope Filter]} + \text{[Exact Package @ Version / Symbol / Error String]} + \text{[Target Artifact Type]} + \text{[Stack Context / Constraints]}$$

#### ❌ BANNED (Vague / Low-Signal):
- `nextjs router`
- `prisma supabase connection issue`
- `react 19 state`

#### ✅ GOATED (Pinpoint / High-Signal):
- `site:github.com/vercel/next.js/issues "App Router" "useSearchParams" suspense boundary hydration mismatch v15.1.0 fix`
- `site:docs.supabase.com OR site:github.com/prisma/prisma "PrismaClientInitializationError" connection pooling PgBouncer transaction mode limit`
- `site:react.dev OR site:github.com/facebook/react/issues "useActionState" typescript signature return tuple pending state v19.0.0`

---

### 2. Dual-Engine Search Strategy (Tavily vs. Exa Mechanics)

| Dimension | Tavily Search (`tavily_search` / `tavily_research`) | Exa Semantic Search (`web_search_exa`) |
|---|---|---|
| **Query Style** | Structured boolean operators (`site:`, `"exact"`, `AND/OR`) | Natural language semantic intent ("Here is the production implementation of X in TS:") |
| **Search Depth** | MANDATORY: `search_depth="advanced"`, `max_results=15-20` | Semantic vector neural search |
| **Domain Control** | Strict `include_domains` and `exclude_domains` arrays | `category="github"`, `category="research paper"`, `category="company"` |
| **Best For** | Official API docs, exact GitHub issue error strings, release notes | Niche community implementations, conceptual alternatives, similarity discovery |

---

### 3. Master MCP Invocation Examples (Copy-Paste Ready)

#### A. Tavily Search (`tavily_search`) — Exact API Signature Lookup
```json
{
  "query": "site:github.com/upstash/qstash-js OR site:upstash.com/docs \"Client\" publishJSON parameters typescript return type v2",
  "search_depth": "advanced",
  "max_results": 15,
  "include_domains": ["github.com", "upstash.com"],
  "exclude_domains": ["medium.com", "dev.to"],
  "include_raw_content": true
}
```

#### B. Exa Neural Search (`web_search_exa`) — Production Implementation Patterns
```json
{
  "query": "Here is an production-ready TypeScript example of Upstash Redis ratelimit with sliding window in Next.js Server Actions handling edge cases:",
  "category": "github",
  "numResults": 15
}
```

#### C. Context7 Documentation Flow (`context7`)
```json
// Step 1: Resolve ID
{ "libraryName": "date-fns" }

// Step 2: Fetch Docs
{
  "libraryId": "date_fns_v3",
  "query": "format addDays exact function signature TypeScript parameters return type"
}
```

---

### 4. 5-Tier Search Query Matrix

When conducting a comprehensive research audit, execute queries across all 5 tiers simultaneously using both engines:

| Tier | Objective | Tavily Query Pattern | Exa Neural Pattern |
|---|---|---|---|
| **Tier 1: Canonical Docs** | API signatures & types | `site:[docs_domain] "[symbol]" signature typescript` | `"Official API reference and TypeScript stubs for [symbol]"` |
| **Tier 2: Real Production Code** | AST & usage examples | `site:github.com "[symbol]" "import {" typescript` | `"Production code example using [symbol] in Next.js/React"` |
| **Tier 3: Error & Bug Tracker** | GitHub issues & CVEs | `site:github.com/[repo]/issues "[exact_error_string]" fix` | `"How to resolve [exact_error_string] when using [package]"` |
| **Tier 4: Benchmarks & Trade-offs** | Performance & size | `"[package_A]" vs "[package_B]" bundle size gzipped latency` | `"Detailed performance comparison and trade-offs between [A] and [B]"` |
| **Tier 5: Deprecations** | Migration paths | `"deprecated" "[old_symbol]" replace "[new_symbol]" migration` | `"Upgrading [package] from v[X] to v[Y] breaking changes codemod"` |


---

## The 5-Phase Research Pipeline

### Phase 1: Query Decomposition & Strategy
*   **MCP Tools:** `sequential-thinking/sequentialthinking`
*   **Sub-skills:** `concise-planning`, `superpowers-brainstorm`
*   **Action:**
    1. **Decompose** the research topic into atomic questions:
       *   Primary question: "How does X work?"
       *   Implementation question: "What is the API signature for Y?"
       *   Compatibility question: "Does X work with our stack (Next.js 15, React 19, TypeScript 5.5)?"
       *   Alternatives question: "What are the top 3 alternatives to X?"
       *   Risk question: "What are the known issues, gotchas, or breaking changes?"
    2. **Define evaluation criteria** before searching:
       *   Licensing (MIT/Apache preferred, avoid GPL for commercial).
       *   Bundle size (tree-shakable? What's the minified+gzipped size?).
       *   TypeScript support (native types? DefinitelyTyped? Untyped?).
       *   Maintenance health (last commit, open issues count, release cadence).
       *   Community adoption (npm weekly downloads, GitHub stars, Stack Overflow activity).
    3. Use `sequentialthinking` to map branching lines of inquiry.
    4. Use `concise-planning` to structure the research plan into an atomic investigation checklist.

### Phase 2: Dual-Engine Simultaneous Broad Search & Discovery (Tavily + Exa)
*   **MCP Tools:** `tavily/tavily_search`, `tavily/tavily_research`, `tavily/tavily_map`, `tavily/tavily_crawl`, `exa/web_search_exa`, `exa/web_fetch_exa`
*   **Sub-skills:** `tavily-best-practices`
*   **Action:**
    1. **Dual-Engine Simultaneous Execution:** Always execute search queries using BOTH `tavily` (`tavily_search` / `tavily_research`) AND `exa` (`web_search_exa`) at the same time to collect multi-perspective search results and eliminate single-engine bias.
    2. **Volume & Semantic Coverage:** For Tavily, ensure `max_results` is set to `10`–`20` per query. For Exa, run semantic vector queries simultaneously to capture neural matches, similar links, and alternative technical viewpoints.
    3. **Diverse Multi-Querying:** Run at least 3–5 distinct queries across BOTH tools in parallel targeting different aspects (official docs, community perspectives, GitHub issues, alternative solutions).
    4. **Initial search:** Target specific domains using advanced parameters in Tavily while leveraging Exa's natural language semantic search in parallel:
       *   Official documentation: `docs.*.com`, `*.dev`
       *   GitHub repositories: `github.com`
       *   Community discussions: `stackoverflow.com`, `reddit.com/r/webdev`, `reddit.com/r/reactjs`
       *   Release notes: `github.com/*/releases`
    5. **Site mapping & Discovery:** Use `tavily_map` to discover URL structures while running Exa `web_search_exa` to find related conceptual links and competitor tools.
    6. **Deep crawling:** Use `tavily_crawl` for comprehensive site crawling and Exa `web_fetch_exa` for semantic parsing.
    7. **Multi-step research:** Combine `tavily_research` and Exa search simultaneously for multi-angle autonomous deep dives.
    8. Apply `tavily-best-practices` and Exa semantic search techniques in tandem for query construction, domain filtering, and parallel search orchestration.

### Phase 3: Targeted Extraction & Documentation (Tavily + Exa + Context7)
*   **MCP Tools:** `tavily/tavily_extract`, `exa/web_fetch_exa`, `context7/resolve-library-id`, `context7/get-library-docs`
*   **Sub-skills:** `tavily-best-practices`
*   **Action:**
    1. **Content extraction:** Use `tavily_extract` and `exa/web_fetch_exa` side-by-side to fetch and parse clean content/markdown from target URLs containing guides, tutorials, or API references.
    2. **Library documentation:** Use the two-step Context7 flow:
       *   Step 1: `context7/resolve-library-id` — Resolve the library name to its Context7 ID.
       *   Step 2: `context7/get-library-docs` — Fetch version-specific API documentation with code examples.
    3. **API signature verification:** For every API function you plan to recommend:
       *   Extract the exact function signature (parameters, types, return values).
       *   Note the minimum version that supports this signature.
       *   Check for deprecated alternatives or breaking changes in recent versions.
    4. **Dependency tree check:** For library recommendations:
       *   How many transitive dependencies does it install?
       *   Are there known CVEs in the dependency tree?
       *   What's the total bundle size impact?

### Phase 4: Dual-Engine Independent Submissions & Side-by-Side Comparison
*   **MCP Tools:** `tavily/tavily_search`, `exa/web_search_exa`
*   **Sub-skills:** `upstash-redis-js`, `upstash-vector-js`, `upstash-search-js`
*   **Action:**
    1. **Submit Tavily Version:** Collect and structure Tavily's independent research output (`Tavily Report Version`), focusing on domain/keyword index results, official docs, and deep site crawls.
    2. **Submit Exa Version:** Collect and structure Exa's independent research output (`Exa Report Version`), focusing on neural/semantic vector matches, concept-linked articles, and alternative perspectives.
    3. **Side-by-Side Comparison & Decision Matrix:** Compare the Tavily Version against the Exa Version across key dimensions:
       *   **Consensus Points:** Where both Tavily and Exa agree on API signatures, best practices, or library choices.
       *   **Divergent Findings / Conflicts:** Where Tavily and Exa suggest different APIs, workarounds, or architectures.
       *   **Unique Perspectives:** Niche libraries or novel code patterns uncovered by Exa that Tavily missed, or specific official release notes captured by Tavily that Exa missed.
    4. **Final Decision Synthesis:** Formulate the final recommendation based strictly on the side-by-side evaluation of both submitted versions.
    2. **Local verification:** Cross-reference retrieved documentation with:
       *   Current `package.json` / `requirements.txt` for version compatibility.
       *   Current `tsconfig.json` for TypeScript target compatibility.
       *   Current framework version (Next.js, React, Expo) for feature availability.
    3. **API testing:** If possible, verify API calls work by writing a minimal test script (save to `scratch/` directory).
    4. **Cache research findings:** Use `upstash-redis-js` to cache verified API signatures and documentation snippets for quick retrieval in subsequent queries.
    5. For large research corpora, index findings using `upstash-vector-js` for semantic similarity retrieval.

### Phase 5: Knowledge Persistence & Reporting
*   **MCP Tools:** `memory` (create_entities, create_relations, add_observations, read_graph)
*   **Sub-skills:** `docx`, `ckm:slides`, `ultimate-documentation-workflow`
*   **Action:**
    1. **Pre-check:** Read `memory/read_graph` at the start of every research task to build on previous findings.
    2. **Persist findings:** Create entities and relationships in the memory graph:
       *   Entity: Library name, version, category.
       *   Observations: API signatures, bundle sizes, known issues, recommendations.
       *   Relations: "replaces", "compatible-with", "conflicts-with", "depends-on".
    3. **Research report format:** Reference the layout from Section 4.
    4. For formal deliverables, use `docx` for Word document research reports.
    5. For stakeholder presentations, use `ckm:slides` for HTML slide decks.

---

## Tavily API Parameters & Configuration Guide

When calling the `tavily` API tools programmatically or via subagents, configure parameters according to the following optimization guide:

| Parameter | Recommended Value | Why |
|---|---|---|
| `search_depth` | `"advanced"` | Fetches richer context, summaries, and raw crawl matches instead of quick answers. |
| `max_results` | `10` to `20` | MANDATORY: To ensure a comprehensive pool of search responses, always request 10-20 results per query. |
| `include_domains` | `["docs.supabase.com", "github.com"]` | Restricts lookup to authority domains for the topic. |
| `exclude_domains` | `["medium.com", "dev.to"]` | Filters out low-quality, out-of-date personal blogs. |
| `include_raw_content`| `true` | Required when extracting code snippets or specific configuration examples. |

---

## Real-world Research Case Study: Date/Time Libraries

### The Topic
We need to select a modern, lightweight utility library for date parsing, formatting, and time zone manipulation in our Next.js web application.

### Evaluation Scorecard

| Metric | Day.js | date-fns | Native `Intl` |
|---|---|---|---|
| **Bundle Size** | 2.8 KB (min) | Tree-shakable (varies) | **0 KB** (Built-in) |
| **API Style** | Moment-like wrapper | Modular pure functions | Native JS object |
| **Time Zone Support** | Via plugin (`dayjs/plugin/timezone`) | Via `date-fns-tz` | Native IANA |
| **Tree-shaking** | No (imports full object) | **Yes** | N/A |
| **TS Support** | Native | Native | Native |
| **Community Health** | High, but Moment legacy | High, active | Core Web Standard |
| **Weighted Total** | **3.8** | **4.2** | **4.5** |

### Verified Code Usage Snippets

#### 1. date-fns (v3.0.0+)
*Source: `date-fns.org/v3.0.0/docs`*
```typescript
import { format, addDays } from 'date-fns';

const today = new Date();
const nextWeek = addDays(today, 7);
const formatted = format(nextWeek, 'yyyy-MM-dd HH:mm:ss');
console.log(formatted);
```

#### 2. Native `Intl` Date Formatting
*Source: `developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat`*
```typescript
const formatter = new Intl.DateTimeFormat('en-US', {
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
  hour: '2-digit',
  minute: '2-digit',
  second: '2-digit',
  hour12: false,
  timeZone: 'UTC'
});
console.log(formatter.format(new Date()));
```

---

## Context7 API Integration Flow

When using the `context7` MCP server to retrieve official package documentation, execute the following two-step flow sequentially:

### Step 1: Resolve Library ID
Call `context7/resolve-library-id` with the library name to retrieve the correct registry ID.
```json
// Example Arguments
{
  "libraryName": "date-fns"
}
// Example Output
{
  "libraryId": "date_fns_v3"
}
```

### Step 2: Retrieve Library Documentation
Call `context7/get-library-docs` with the resolved ID to retrieve API markdown documentation, type stubs, and code examples.
```json
// Example Arguments
{
  "libraryId": "date_fns_v3",
  "query": "addDays function signature and parameters"
}
// Example Output
{
  "docs": "### addDays
`addDays(date: Date | number | string, amount: number): Date`
Add the specified number of days to the given date.
..."
}
```

---

## Advanced Search Operators Reference

When formulating search queries for `tavily_search` or `web_search_exa`, use the following advanced search operators to filter results:

*   **`site:domain.com`**: Restrict results to a single domain.
    *   *Example:* `site:github.com/facebook/react issues "hydration mismatch"`
*   **`"exact phrase"`**: Force match on exact strings (crucial for stack traces).
    *   *Example:* `"TypeError: Cannot read properties of undefined (reading 'map')"`
*   **`AND` / `OR`**: Combine terms.
    *   *Example:* `Prisma OR Supabase "connection pool" serverless`
*   **`-exclude`**: Exclude specific terms.
    *   *Example:* `next.js router -pages` (ignores the old Pages router)

---

## Research Query Templates

Use the following query templates depending on the objective:

### 1. Library API Reference Lookup
`"site:[docs_url] OR site:[github_repo] [class_or_method_name] signature example typescript [version]"`
*Example:* `site:github.com/upstash/qstash-js "Client" signature example typescript v2`

### 2. Bug & Error Diagnosis
`"site:github.com/[org]/[repo]/issues OR site:stackoverflow.com \"[exact_error_message]\" fix OR workaround"`
*Example:* `site:github.com/prisma/prisma/issues "PrismaClientInitializationError" Supabase connection limit workaround`

### 3. Deprecation Migration Guide
`"\"[old_method_name]\" deprecated replace \"[library_name]\" migration guide v[new_version]"`
*Example:* `"router.events.on" deprecated replace "next/navigation" migration guide v13`

---

---

## Document Triage & Confidence Assessment

When evaluating search results, grade sources using the following confidence checklist to filter out noise:

*   **Grade A (90-100% Confidence): Official Documentation & Specs**
    *   *Examples:* MDN Web Docs, PostgreSQL Official Documentation, React Dev Docs, RFC specifications.
    *   *Trust:* Absolute. Match signatures exactly.
*   **Grade B (75-89% Confidence): Verified Library Code & GitHub Source**
    *   *Examples:* GitHub source files (`/src`), verified release notes, official examples inside registry repositories.
    *   *Trust:* High. Use to trace internal function behaviors.
*   **Grade C (50-74% Confidence): Active Community Threads & Issue Trackers**
    *   *Examples:* GitHub issues (with >3 reactions/confirmations), Stack Overflow (with accepted checkmark and recent edits).
    *   *Trust:* Medium. Crucial for workarounds, build errors, and undocumented limits.
*   **Grade D (0-49% Confidence): Medium Articles, Personal Blogs, and AI Summaries**
    *   *Examples:* Medium posts, Dev.to tutorials, outdated YouTube description logs.
    *   *Trust:* Low. Use only as high-level conceptual inspiration. Always verify code independently.

---

## Programmatic Web Scraping & Content Cleaning

When extracting text from URLs using `tavily_extract` or programmatic GET requests, clean the document corpus using these rules before running synthesis:

1. **Remove Layout Noise:** Strip navigation footers, sidebar links, header menus, and newsletter subscribe banners.
2. **Isolate Code Wells:** Look for `<pre>` or `<code>` blocks to extract native type declarations and configurations.
3. **Format as Markdown:** Convert HTML structures to semantic markdown headers (`#`, `##`, `###`) to preserve documentation hierarchies.
4. **Prune Script Blobs:** Remove `<script>` tags, inline CSS styles, and marketing trackers to keep context clean.

---

## Research report format

```markdown
## Research: [Topic]

### Executive Summary
[2-3 sentence summary]

### Dual-Engine Independent Submissions

#### 1. Tavily Research Version
- **Focus:** Keyword/Domain search & official docs crawling
- **Key Findings:** [Summary of Tavily's independent findings]
- **Proposed Solution:** [Tavily's primary recommendation]

#### 2. Exa Research Version
- **Focus:** Neural/Semantic vector search & concept matching
- **Key Findings:** [Summary of Exa's independent findings]
- **Proposed Solution:** [Exa's primary recommendation]

### Side-by-Side Comparison Matrix
| Evaluation Criteria | Tavily Submission | Exa Submission | Consensus / Final Verdict |
|---|---|---|---|
| Recommended Approach | [Tavily proposal] | [Exa proposal] | [Agreed / Chosen Path] |
| API Signature / Spec | [Tavily signature] | [Exa signature] | [Verified standard] |
| Edge Cases & Risks | [Tavily caveats] | [Exa caveats] | [Mitigated risks] |

### Final Decision & Rationale
[Chosen approach + version + explicit rationale based on the comparison]

### Code Snippet Example
```typescript
// Verified working code block here
```

### Caveats & Deprecations
- [Known limitation 1]
- [Known limitation 2]

### Sources
1. [URL 1] - [Description]
2. [URL 2] - [Description]
```

---

## Research Query Log Template

Track executed queries and search scopes using this structure inside the scratch directory (`scratch/research_log.md`):

```markdown
### Research Query Log: [Topic]

| ID | Query | Target Domains | Results Count | Top Source URL | Date Run |
|---|---|---|---|---|---|
| Q01 | `site:docs.supabase.com RLS policy auth.uid()` | `docs.supabase.com` | 8 | `https://docs.supabase.com/...` | 2026-06-23 |
| Q02 | `"PrismaClientInitializationError"` | `github.com/prisma/prisma` | 15 | `https://github.com/prisma/...` | 2026-06-23 |
```


---

## Research Quality Checklist

- [ ] Every finding cites a direct URL source
- [ ] Version numbers are pinned for all recommendations
- [ ] API signatures verified against current documentation (not memory)
- [ ] At least 2 independent sources for critical findings
- [ ] Documentation age noted — alert if >6 months old
- [ ] Bundle size / dependency count checked for library recommendations
- [ ] Compatibility verified against current project stack versions
- [ ] Known issues, gotchas, and deprecations documented
- [ ] Findings persisted to memory graph for future reference

---

## Troubleshooting Obscure Errors Checklist
When research yields zero results or search queries fail to uncover the error, apply this checklist:
- [ ] **Strip Dynamic Variables:** Remove system paths, GUIDs, database IDs, and timestamps from the search query. Search only for the static string components.
- [ ] **Search for Parent Exception:** If the child stack trace is too specific, search for the parent wrapper class or error module definition (e.g. `PrismaClientKnownRequestError` instead of `P2002`).
- [ ] **Trace Native Code:** Go to the library's GitHub repository. Use code search to locate the file throwing the exception string. Identify what code paths trigger that error code.
- [ ] **Verify open PRs:** Check the repository's open and closed PR history for issues addressing the bug. Often a fix is implemented but not yet merged or published in a release.
- [ ] **Translate Stack Trace:** If the stack trace originates in a compiled layer (e.g. WASM or C++ bindings), look up the underlying binding code parameters.

### Research Tools Selection Grid
Select the appropriate tool depending on the nature of the research query (always run Tavily + Exa together for search):
- **Tavily Search (`tavily_search` / `tavily_research`):** Best for structured domain filters, keyword indexing, deep site crawling, and comprehensive multi-query results.
- **Exa Search (`web_search_exa` / `web_fetch_exa`):** Best for neural/semantic search, discovering similar links, concept matching, and finding alternative perspectives/frameworks.
- **Dual Tavily + Exa Concurrent Search:** MANDATORY for web searches — run BOTH engines simultaneously to cross-validate facts, eliminate single-engine bias, and gather complete perspectives to aid decision making.
- **Tavily Extract & Exa Fetch:** Best for parsing raw markdown contents of target documentation URLs.
- **Context7:** Best for fetching official API documentation, guides, and typing declarations for npm packages.
- **Playwright Browser:** Best for reading pages requiring authentication, complex JS execution, or visual verification.



---

## Anti-Patterns (Reject These)

| Anti-Pattern | Why It's Wrong | Do This Instead |
|---|---|---|
| "I know this API works" | Memory may be stale or hallucinated | Verify against current docs before using |
| Recommending without version | Version changes break APIs | Always pin `library@version` |
| Single-source trust | Docs can be outdated or wrong | Cross-reference 2+ sources |
| "Just use X" without trade-offs | Hides complexity and risks | Present options with scored comparison |
| Blog post as sole source | Blogs age poorly, may be inaccurate | Prefer official docs + GitHub issues |
| Skipping npm audit | Hidden CVEs in transitive deps | Always check dependency security |

---

## Sub-Skill Checklists & Reference Templates

### 1. Tavily Search Best Practices (`tavily-best-practices`)
*   **Method Selection Matrix:**
    *   **search():** Web search results for real-time data, community issues, or package releases.
    *   **extract():** Content from specific URLs parsed cleanly into markdown.
    *   **crawl():** Site-wide extraction focusing on target semantic paths (e.g., API documentation).
    *   **map():** Discovering all active URLs on a domain.
    *   **research():** End-to-end multi-topic research with AI synthesis.
*   **Search Query Optimization:** Keep queries under 400 characters, descriptive, and focus-targeted. Use domain filters (`include_domains`, `exclude_domains`) and `time_range` constraints.
*   **Extraction Guidelines:** Limit URL arrays to maximum 20 targets. Use `extract_depth: "advanced"` to parse complex layouts and dynamic content pools.

### 2. Semantic Vector Indexing (`upstash-vector-js`)
*   **Distance Metrics:** Use Cosine distance for text embeddings, Dot Product for normalized vectors, and L2 (Euclidean) for image feature maps.
*   **Namespace Scopes:** Query within isolated namespaces to restrict searches to specific document subsets.
*   **Metadata Filtering:** Apply boolean filtering logic on vector metadata fields (e.g. `category == "security"`) during index queries to reduce execution limits and improve match accuracy.

### 3. Keyword Search Configuration (`upstash-search-js`)
*   **Index Management:** Create search index mappings defining properties, types (text vs keyword), and tokenizers.
*   **Querying & Aggregations:** Combine term searches with numeric filters (e.g., `price < 50`) and group/bucket result counts dynamically.

### 4. Parallel Web Search Orchestrator (`tavily-best-practices`)
*   **Concurreny-Controlled Web Search:** Execute queries in parallel using asynchronous client loops with error tolerance and parameter scopes:
    ```typescript
    import { tavily } from '@tavily/core';
    
    const tv = tavily({ apiKey: process.env.TAVILY_API_KEY });
    
    export async function runParallelResearch(queries: string[]) {
      const searchPromises = queries.map(query => 
        tv.search({
          query,
          searchDepth: 'advanced',
          maxResults: 5,
        }).catch(err => {
          console.error(`Search failed for "${query}":`, err);
          return null; // Return null instead of breaking whole batch
        })
      );
      
      const results = await Promise.all(searchPromises);
      return results.filter(r => r !== null);
    }
    ```

---

## Cross-Cutting Concerns
*   **Planning:** Feed research outputs into `ultimate-planning-workflow` for implementation step generation.
*   **Brainstorming:** Feed research into `ultimate-brainstorm-workflow` for option evaluation matrices.
*   **Architecture:** Feed architectural research into `ultimate-architecture-workflow` for ADR documentation.
*   **Documentation:** Use `ultimate-documentation-workflow` for maintaining research logs and API reference docs.
*   **Memory:** Use `memory` MCP to persist research findings across conversations — never re-research the same topic.
