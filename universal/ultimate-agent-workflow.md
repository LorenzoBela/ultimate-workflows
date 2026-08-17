---
name: ultimate-agent-workflow
description: >
  Master workflow for prompt engineering, token caching, memory organization, and subagent
  delegation.
  Coordinates task decomposition, spawning cavecrew subagents, and compressing tool
  outputs to extend context limits.
  Triggers on "ultimate agent workflow", "/ultimate-agent-workflow", or when spawning
  subagents, managing agent context, or organizing memory graphs.
argument-hint: "[delegate-task | memory-sync | context-save]"
---

# Ultimate AI Agent Execution & Delegation Workflow

This workflow guides prompt configuration, memory graphs persistence, token compression, and subagent delegation to maximize reasoning quality, maintain state consistency, and preserve main-context window limits.

---

## Iron Laws of Agent Delegation

1. **Never Delegate Blindly.** A subagent is only as good as its instructions. Every delegation must have: (1) clear context, (2) strict boundary files, (3) exact task descriptions, and (4) run-ready verification commands.
2. **Context is Gold, but Bloat is Death.** Protect the token budget. Compress raw tool outputs, exclude vendor directories, and use `/caveman-compress` on long memory files.
3. **Idempotence by Default.** All modifications made by subagents must be safe to run repeatedly. If a subagent crashes midway, it must be able to resume without creating duplicate records, migrations, or broken syntax.
4. **Verification is the Final Gate.** No subagent task is complete until its specific validation tests run and report a 100% success rate. Never merge unverified subagent code.
5. **No Speculative Abstractions.** Keep code simple and direct. Do not let subagents create hypothetical classes, interfaces, or libraries that are not strictly requested by the task. Apply `ponytail` rules to keep implementations lean.
6. **State Synchronisation is Mandatory.** Observations made by subagents must be committed back to the persistent memory graph (`memory`) or shared cache (`upstash-redis-js`) before closing the subagent context.

---

## Agent Execution & Delegation Matrix

| Parameter / Skill | Investigator (`cavecrew-investigator`) | Builder (`cavecrew-builder`) | Reviewer (`cavecrew-reviewer`) |
| :--- | :--- | :--- | :--- |
| **Primary Scope** | Codebase search, finding definitions, tracing paths | surgical edits to $\le$ 2 files, bug fixes | inspecting diffs, validating logic, running tests |
| **Available Tools** | `grep_search`, `list_dir`, `view_file`, `context7` | `replace_file_content`, `write_to_file` | `playwright`, `run_command`, `lint-and-validate` |
| **Context Strategy** | Open files read-only, do not modify workspace | Focus on specific target lines, run unit tests | Verify E2E behavior, audit contrast & accessibility |
| **Token Budget** | Medium (20k–50k input tokens) | Small (10k–30k input tokens) | Medium (20k–40k input tokens) |
| **Failure Recovery** | Expand search queries, check synonyms | Rollback file edits, analyze logs | Run systematic debugging, log issue |

---

## The 4-Phase Agent Execution Pipeline

### Phase 1: Task Decomposition & Scope Assessment
*   **Sub-skills:** `sequential-thinking/sequentialthinking`, `concise-planning`, `superpowers-brainstorm`
*   **Action:**
    1. **Decompose the Request:** Break down the user's high-level task into atomic, logical steps. Use `sequential-thinking` to evaluate different execution paths.
    2. **Determine Delegation Model:** Use the delegation rules of thumb:
       *   *Main Thread:* Cross-cutting changes, architecture plans, multi-file structural edits, and final integration reviews.
       *   *Subagent:* Codebase investigations, isolated single-file changes, writing minor test cases, or running accessibility audits.
    3. **Define File Boundaries:** Identify the exact file paths that need reading or editing. Ensure subagents are restricted to these paths.
    4. **Agile Sprint Scoping:** Use `superpowers-brainstorm` to define constraints, identify risks (e.g. library version incompatibilities), and map out milestones.
    5. **Atomic Checklist Generation:** Run `concise-planning` to create a checklist containing target files, line ranges, and validation tests.
    6. **Check for Stale Files:** Verify that no active editor conflicts or unsaved files exist before spawning subagents.
    7. **Pre-flight Resource Verification:** Audit the current CPU, memory load, and network connectivity states. If workspace services are unstable, resolve connections before starting.
    8. **Identify Cache Reuse Paths:** Look for previous prompts in conversation logs that can be structurally re-aligned to maximize Gemini's context prompt caching.

### Phase 2: Subagent Spawning & Task Delegation
*   **Sub-skills:** `cavecrew`, `upstash-box-js`, `ultimate-agent-dev-workflow`
*   **Action:**
    1. **Select the Specialized Agent:** Choose the correct `cavecrew` subagent based on the task type (Investigator for research, Builder for edits, Reviewer for verification).
    2. **Compose the Prompt:** Write a highly structured, one-shot prompt containing context, tasks, verification rules, and constraints.
    3. **Configure Sandbox Environment:** For tasks that involve running unsafe code or compiling binaries, use `upstash-box-js` to spin up isolated containers for parallel work.
    4. **Token Control:** Enforce `caveman` formatting rules on the generated prompt to minimize context size.
    5. **Register Lifecycle Observers:** If spawning via the Antigravity SDK, set up `pre-turn` and `post-turn` hooks to track subagent execution state.
    6. **Monitor Process Output:** Route subagent stdout/stderr logs directly to `artifacts/superpowers/subagents/` for auditing.
    7. **Implement Status Pings:** For subagents executing operations asynchronously, set up automated status pings or callbacks to keep the supervisor informed of locks and delays.
    8. **Graceful Timeouts:** Wrap subagent execution hooks in rigid timeouts (e.g., 90 seconds). If a subagent times out, capture the current filesystem state, terminate the process, and log the diagnostic stack.

### Phase 3: Token Compression & Context Management
*   **Sub-skills:** `caveman`, `caveman-compress`, `caveman-stats`, `ponytail-caveman`
*   **Action:**
    1. **Apply Caveman Rules:** Keep all responses and prompts terse. Remove conversational filler, redundant logs, and long explanations.
    2. **Compress Memory Files:** Run `/caveman-compress` on local developer journals, README files, or scratch logs to keep input token counts low.
    3. **Monitor Token Consumption:** Use `caveman-stats` regularly to calculate token savings, checking input, output, and cache hit metrics.
    4. **Enforce YAGNI Code Quality:** Apply `ponytail-caveman` combined rules to prevent subagents from adding boilerplate code or useless helper functions.
    5. **Garbage Collection:** Delete temporary logs and scratch files from the `artifacts/` folder once subagent tasks are verified and completed.
    6. **Optimistic Caching:** Structure prompts so that headers and instructions match previous turns, leveraging Google's prompt caching system.
    7. **Clean Stacking:** Consolidate subagent outputs by extracting the delta diff instead of copying complete files back into the main discussion thread.
    8. **Prune History Redundancies:** In long execution sessions, summarize the intermediate status steps and truncate stack traces to preserve top-level reasoning tokens.

### Phase 4: Memory Mapping & State Synchronization
*   **MCP Tools:** `memory`, `upstash-redis-js`, `upstash-redis-start`
*   **Action:**
    1. **Read Active Graph:** Retrieve the current knowledge graph using `memory/read_graph` to align the subagent with established patterns.
    2. **Extract Discoveries:** On subagent completion, parse the output logs to extract key findings (e.g. database schemas, API overrides, port mapping configs).
    3. **Write Observations:** Save these findings to the knowledge graph using `memory/create_entities` and `memory/create_relations` to keep the context persistent.
    4. **Provision Ephemeral Storage:** Use `upstash-redis-start` to spin up zero-config scratch databases for managing high-frequency subagent data (e.g., job queues).
    5. **Distributed Caching:** Use `upstash-redis-js` to cache persistent data across sessions if the knowledge graph is not suited for it.
    6. **Merge and Verify Workspace:** Synchronize workspace changes back to the main git branch and run final verification checks.
    7. **Audit Log Validation:** Verify that subagents did not log sensitive API keys, session tokens, or user credentials in the public log output.
    8. **Resolve Memory Desyncs:** If multiple subagents modify the shared workspace, run a reconciliation pass between the database schemas and the active memory graph.

---

## Specialized Sub-Agent Blueprints

### 1. `cavecrew-investigator` Prompt Blueprint
```markdown
[ROLE]
You are cavecrew-investigator, a specialized codebase research agent. Your task is to locate files, definitions, and API usage patterns.

[BOUNDARIES]
- Search path: C:/Users/Lorenzo Bela/Downloads/SpayV2
- Read-only access. Do not write or edit any files.

[TASK]
Find all references to 'is_manual_override' in database schemas, services, and Next.js route files. Trace the call paths from the frontend to the controller.

[OUTPUT FORMAT]
Return a JSON array containing objects with:
- file: Absolute path of the file
- line: Line number of the match
- snippet: Matching line content
- context: 2 lines before/after the match
```

### 2. `cavecrew-builder` Prompt Blueprint
```markdown
[ROLE]
You are cavecrew-builder, a specialized code modification agent. Your task is to apply surgical edits to the target file.

[BOUNDARIES]
- Target file: C:/Users/Lorenzo Bela/Downloads/SpayV2/web/src/lib/installments-calculator.ts
- Modify only lines 120-145. Do not add speculative classes or helpers.

[TASK]
Update the installment calculator method to handle manual fee overrides. Extract rates from the remarks JSON metadata as specified in the plan.

[VERIFICATION]
Run 'npx tsx web/src/scripts/test-calculator.ts' to verify correctness.

[OUTPUT FORMAT]
Return a git-diff representing the changes made, followed by the test suite output.
```

### 3. `cavecrew-reviewer` Prompt Blueprint
```markdown
[ROLE]
You are cavecrew-reviewer, a specialized code review and validation agent. Your task is to audit changes for correctness, styling, and security.

[BOUNDARIES]
- Target files: C:/Users/Lorenzo Bela/Downloads/SpayV2/web/src/lib/installments-calculator.ts
- Read-only access.

[TASK]
Audit the recent changes for:
1. SQL injection vulnerability (check parameterization).
2. Proper error boundaries (check for try-catch blocks and typed errors).
3. Type-safety (check for 'any' types).
4. Accessibility (check for contrast ratios on modified components).

[OUTPUT FORMAT]
Return a Markdown list of issues categorized by severity:
- Blocker: Must fix immediately
- Major: Functional or performance issues
- Minor: Code styling or minor optimizations
```

---

## Token Compression Rules & Examples

To maintain a low context footprint, all agent prompts must be compressed by stripping out natural language noise.

### Prompt Compression Example
*   **Before Compression (245 tokens):**
    > "Hi, I hope you are doing well. I need you to search through the codebase for me. I am looking for the file where the D3 bar chart is defined because the colors of the bars are currently hardcoded and I need to modify them so that they use our design system colors instead. Once you find it, please let me know the path and the line numbers where the colors are declared so I can go in and edit it."
*   **After Compression (46 tokens):**
    > "Search codebase. Locate D3 bar chart file definition. Target: hardcoded bar colors. Return file path and line numbers containing the color declarations. No narrative."

### Compression Guidelines
- **Drop Greetings & Sign-offs:** Never write "Hello", "Thanks", "Hope you're doing well", or "Let me know".
- **Use Imperative Verbs:** Start sentences with active instructions: "Locate", "Modify", "Run", "Verify", "Return".
- **Condense Code Blocks:** Only include lines that are directly relevant to the edit. Use comments (`// ...`) to represent unmodified regions.
- **Reference Paths Directly:** Never describe where a file is; write the literal path: `web/src/components/charts/D3BarChart.tsx`.

---

## Few-Shot Dynamic Tool Mapping Blueprint

Use the following few-shot prompt structure to guide subagents in selecting the most context-appropriate tool during execution:

```markdown
[CONTEXT]
Given a specific task, map the command to the most narrow and specific tool possible.

[EXAMPLES]
Input: Read the contents of the database schema file to verify the columns.
Output: view_file { AbsolutePath: "web/prisma/schema.prisma" }

Input: Look up the implementation details of our custom focus trap hook.
Output: grep_search { Query: "useFocusTrap", SearchPath: "web/src/hooks" }

Input: Check the console output of our test execution for compilation errors.
Output: run_command { CommandLine: "npm run test:compile", Cwd: "web" }
```

---

## Memory & State Reconciliation Code Template

This script template reconciles observations between the local agent memory context and the persistent Postgres database cache:

```typescript
import { Redis } from '@upstash/redis';
import { supabase } from './supabaseClient';

const redis = new Redis({
  url: process.env.UPSTASH_REDIS_REST_URL!,
  token: process.env.UPSTASH_REDIS_REST_TOKEN!,
});

interface MemorySyncPayload {
  agentId: string;
  observationKey: string;
  value: string;
}

export async function reconcileAgentMemory(payload: MemorySyncPayload) {
  const cacheKey = `agent:memory:${payload.agentId}:${payload.observationKey}`;
  
  // 1. Write observation to fast Redis cache for other subagents
  await redis.set(cacheKey, payload.value, { ex: 86400 }); // 24 hour TTL
  
  // 2. Persist database observation in relational Supabase schema for auditing
  const { error } = await supabase
    .from('agent_observations')
    .insert([
      {
        agent_id: payload.agentId,
        observation_key: payload.observationKey,
        observation_value: payload.value,
        synchronized_at: new Date().toISOString()
      }
    ]);
    
  if (error) {
    console.error(`[Memory Sync] Supabase desync for key ${payload.observationKey}: ${error.message}`);
    throw error;
  }
}
```

---

## Sub-Skill Checklists & Reference Manuals

### 1. Memory Graph Management (`memory`)
*   **Observation Persistence:** When creating entities in the knowledge graph, write clean, declarative descriptions:
    ```json
    {
      "entity": "InstallmentsCalculator",
      "type": "Class",
      "observations": [
        "Located in web/src/lib/installments-calculator.ts",
        "Calculates monthly installment values based on term lengths (3m, 6m, 12m)",
        "Handles manual fee overrides stored in order.remarks JSON metadata"
      ]
    }
    ```
*   **Relation Definition:** Link entities to represent system architecture:
    ```json
    {
      "source": "InstallmentsCalculator",
      "target": "UserSetting",
      "type": "queries",
      "description": "Reads global interest rate settings from the database"
    }
    ```

### 2. Ephemeral Storage Operations (`upstash-redis-start`)
*   **Provisioning Command:** Provision an isolated Redis instance for temporary agent task state:
    ```bash
    curl -X POST https://upstash.com/start-redis \
      -H "Content-Type: application/json" \
      -d '{"name": "agent-scratch-db", "ttl": 259200}'
    ```
*   **Lock Pattern:** Ensure subagents do not overwrite each other's work by acquiring distributed locks using HTTP calls (`upstash-redis-js`):
    ```typescript
    // Attempt to acquire lock for 30 seconds
    const lockAcquired = await redis.set("lock:installments-calculator", "agent-builder-1", {
      nx: true,
      ex: 30
    });
    ```

### 3. Task Planning Trade-offs (`superpowers-brainstorm` & `concise-planning`)
*   **Risk Scoping Matrix:** Before allocating tasks to subagents, run a risk check:
    *   *High Risk (Do not delegate):* Modifying core database schemas, changing authentication flows, or editing shared global configurations.
    *   *Low Risk (Safe to delegate):* Implementing standalone utility functions, writing test files, or updating style definitions.

---

## Cross-Cutting Concerns
*   **Development:** Link with `ultimate-agent-dev-workflow` to implement custom agents, hooks, and tool bindings.
*   **Research:** Utilize `tavily-best-practices`, `context7/get-library-docs`, and `perplexity-ask` for retrieving documentation and technical guides.
*   **Validation:** Always run `lint-and-validate` after any subagent modifies files.
*   **Review:** Apply `superpowers-review` and `caveman-review` to inspect subagent outputs.
*   **Git:** Coordinate commits and repository pushing using `ultimate-git-workflow` and `git-pushing`.
