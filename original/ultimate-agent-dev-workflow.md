---
name: ultimate-agent-dev-workflow
description: >
  Master workflow for designing, configuring, implementing, and orchestrating
  autonomous AI agents and multi-agent systems using the Google Antigravity (AGY) SDK.
  Triggers on "ultimate agent dev workflow", "/ultimate-agent-dev-workflow", or when
  building custom AGY agents, hooking API runtimes, or delegating tasks to subagents.
argument-hint: "[agent-config | custom-tool | multi-agent]"
---

# Ultimate AI Agent Development Workflow

This workflow guides the design, configuration, tool integration, lifecycle hooks, and orchestration of autonomous agents using the Google Antigravity (AGY) SDK and serverless ecosystems.

---

## Iron Laws of Agent Development

1. **Determinism over Guesswork.** Lock all agent models, configuration parameters, and prompt templates. Never rely on random seeds, time-dependent logic, or unpinned model versions in production.
2. **Explicit Tool Boundaries.** Every tool exposed to the agent must have strict inputs, output limits, and input validations. Reject malformed tool requests before they execute.
3. **No Speculative Abstractions.** Do not implement speculative APIs, undocumented flags, or unproven libraries inside agent code. The agent's environment must match production constraints exactly.
4. **Fail-Safe Fallbacks.** Every agent pipeline must have recovery paths. If a model fails to return structured output or a tool call times out, fallback to an alternative model, rule-based logic, or request user feedback immediately.
5. **Secure Execution Sandboxes.** Never run unverified code, dynamic tests, or command line binaries on the host system. Always use isolated cloud containers like `upstash-box-js` to handle dynamic tasks.
6. **Auditable Observability.** Log all agent inputs, tool-execution states, token counts (including thinking tokens), and costs. Production behavior must be fully visible and inspectable.

---

## SDK Lifecycle Hooks Matrix

| Hook Name | Trigger Point | Purpose | Example Application |
| :--- | :--- | :--- | :--- |
| **`pre-turn`** | Before the model receives the prompt | Intercept inputs, check token budget, run query mapping | Injects system settings or sanitizes inputs |
| **`post-turn`** | After the model generates a response | Validate schema compliance, parse JSON, track token costs | Validates Pydantic structures |
| **`tool-execution`** | Before executing a tool call | Run safety predicates, check rates, enforce permissions | Rejects write commands on restricted files |
| **`error-recovery`** | When a tool or model call throws | Trap exceptions, attempt retries with backoff, run fallback | Handles database connection timeout |

---

## The 4-Phase Agent Development Pipeline

### Phase 1: Environment & Agent Configuration
*   **Sub-skills:** `google-antigravity-sdk`, `concise-planning`, `superpowers-brainstorm`
*   **Action:**
    1. **Verify SDK Installation:** Check that the `google-antigravity` package is present in dependencies. Ensure API credentials (`GEMINI_API_KEY`) are set and validated.
    2. **Define Agent Settings:** Create the agent configuration (`LocalAgentConfig`). Set model temperature (low values for transactional agents, high for brainstorming), max output tokens, and stop sequences.
    3. **Setup Persona & System Instructions:** Write clear, concise instructions defining the agent's role, task constraints, and output format.
    4. **Perform Startup Checks:** Validate that all required backend connection strings and environment keys are loaded. Fail fast if any configuration is missing.
    5. **Atomic Checklist Generation:** Use `concise-planning` to map out the agent configuration, tool bindings, and verification tests.
    6. **Brainstorm Architecture:** Use `superpowers-brainstorm` to evaluate multi-agent structures, coordinator-child configurations, and memory strategies.
    7. **Local Mock Environment Setup:** Configure mock implementations of external API keys, preventing actual network request costs during local debugging loops.
    8. **Lock Model Checkpoints:** Force system runs to execute against specific, locked model snapshots rather than rolling auto-update tags.

### Phase 2: Tooling & MCP Server Integrations
*   **Sub-skills:** `google-antigravity-sdk`, `upstash-box-js`, `upstash-redis-js`, `upstash-qstash-js`, `upstash-workflow-js`, `upstash-vector-js`, `upstash-search-js`, `upstash-ratelimit-js`, `upstash-cli`, `tavily-best-practices`
*   **MCP Tools:** `supabase-mcp-server/*`, `firebase-mcp-server/*`, `prisma-mcp-server/*`, `playwright/*`, `tavily/*`, `perplexity-ask/*`, `sequential-thinking/*`, `memory/*`, `context7/*`
*   **Action:**
    1. **Expose Custom Tools:** Bind Python or JavaScript functions to the agent, providing precise type annotations and detailed docstrings for function-calling.
    2. **Integrate MCP Servers:** Connect the agent to external toolsets using Model Context Protocol (MCP) clients.
    3. **Setup Safety Predicates:** Implement middleware functions that intercept tool requests and reject them if they violate security limits (e.g. modifying root files).
    4. **Sandbox Code Execution:** Use `upstash-box-js` to run unverified code, dynamic test suites, and binaries inside sandboxed containers.
    5. **Manage Agent Cache:** Use `upstash-redis-js` for caching intermediate states, rate limiting, and session values.
    6. **Dispatch Async Tasks:** Use `upstash-qstash-js` to enqueue agent jobs, schedule crons, and control concurrency.
    7. **Design Durable Workflows:** Use `upstash-workflow-js` to implement multi-step agent pipelines with automatic retries and checkpoint saves.
    8. **Integrate Semantic Search:** Use `upstash-vector-js` for semantic search queries over text chunks, matching cosine similarity thresholds.
    9. **Full-Text Search:** Use `upstash-search-js` for keyword-based document retrieval in agent knowledge bases.
    10. **Rate Limiting:** Use `upstash-ratelimit-js` to protect agent-facing API endpoints from abuse.
    11. **Web Research:** Apply `tavily-best-practices` for production-ready search integrations in agentic workflows.
    12. **Docker Container Cleanup:** Implement automatic teardown scripts that destroy containers and release memory caches on process exit.

### Phase 3: Lifecycle Hooking & Subagent Orchestration
*   **Sub-skills:** `google-antigravity-sdk`, `cavecrew`, `caveman`, `caveman-compress`, `ponytail-caveman`, `ultimate-agent-workflow`
*   **Action:**
    1. **Register Hooks:** Hook into the agent runtime using `on_pre_turn`, `on_post_turn`, and `on_tool_execute` methods.
    2. **Implement Retry Backoff:** Write error-recovery hooks that intercept model errors or API failures and run retries with exponential backoff and jitter.
    3. **Design Multi-Agent Networks:** Setup a supervisor agent that coordinates execution, delegating tasks to child subagents and consolidating their findings.
    4. **Expose Cavecrew Subagents:** Integrate specialized subagents (`cavecrew-investigator`, `cavecrew-builder`, `cavecrew-reviewer`) for targeted, file-bounded execution.
    5. **Compress Instructions:** Run `caveman-compress` on subagent templates to reduce input context footprint.
    6. **Apply Ponytail Simplicity:** Enforce `ponytail` YAGNI principles to ensure subagents write minimal, clean code without bloating the codebase.
    7. **Token Budget Quotas Hook:** Inject a token check in the `pre-turn` lifecycle hook. Stop the turn if the running thread has consumed over 120k tokens.
    8. **Execution Queue Locks:** Prevent race conditions in parallel subagent writes by registering a mutex lock in the Redis coordination key.

### Phase 4: Persistence, Structured Output & Auditing
*   **Sub-skills:** `google-antigravity-sdk`, `upstash-redis-start`, `memory`, `systematic-debugging`, `lint-and-validate`
*   **Action:**
    1. **Enforce Structured JSON:** Restrict the agent model output to valid JSON matching defined Pydantic classes or TypeScript interfaces.
    2. **Restore Conversation State:** Persist session data to disk or a database to allow agents to resume conversations with history intact.
    3. **Setup Scratch Databases:** Use `upstash-redis-start` to provision zero-config, ephemeral Redis instances for short-term task orchestration.
    4. **Update Knowledge Graph:** Record architectural patterns, database schemas, and tool structures in the `memory` MCP node to maintain continuity.
    5. **Audit Token Costs:** Track prompt and execution tokens, calculate costs, and monitor performance latency in structured logs.
    6. **Debug Failures Systematically:** Apply the `systematic-debugging` template when diagnosing agent crashes, testing hypotheses before applying fixes.
    7. **Run Validation Checks:** Validate agent code and configuration schemas using `lint-and-validate` before deployment.
    8. **Git Traceability Commit:** When an execution batch completes, write an automated summary message and trigger a git push.

---

## SDK & Upstash Integration Blueprints

### 1. Google Antigravity SDK Agent & Lifecycle Hooks Configuration
```typescript
import { LocalAgent, LocalAgentConfig, PreTurnContext, PostTurnContext } from 'google-antigravity-sdk';

const config: LocalAgentConfig = {
  model: 'gemini-2.5-pro',
  temperature: 0.1,
  systemInstruction: 'You are a transactional agent. Only return valid JSON matching the requested schema.'
};

const agent = new LocalAgent(config);

// Pre-Turn Hook: Intercept prompt and validate size
agent.onPreTurn(async (ctx: PreTurnContext) => {
  console.log(`[AGY SDK] Pre-turn trigger. Prompt length: ${ctx.prompt.length}`);
  if (ctx.prompt.length > 50000) {
    throw new Error('Prompt exceeds maximum token boundaries.');
  }
});

// Post-Turn Hook: Validate JSON output schema
agent.onPostTurn(async (ctx: PostTurnContext) => {
  console.log('[AGY SDK] Post-turn trigger. Validating structured output...');
  try {
    JSON.parse(ctx.response.text);
  } catch (e) {
    console.error('[AGY SDK] Output is not valid JSON. Requesting retry...');
    return ctx.retry();
  }
});

// Tool Execution Hook: Enforce file access boundaries
agent.onToolExecute(async (toolCall) => {
  const restrictedPaths = ['/etc', '/var/run', '/root'];
  const targetPath = toolCall.args.path;
  
  if (restrictedPaths.some(p => targetPath.startsWith(p))) {
    throw new Error(`Access denied: tool requested access to restricted path: ${targetPath}`);
  }
});
```

### 2. Spawning Subagents in Parallel (Python Orchestrator)
```python
import subprocess
import time
import sys
from pathlib import Path

def run_subagent(skill, task):
    script_path = Path("artifacts/superpowers/scripts/spawn_subagent.py")
    cmd = [
        sys.executable,
        str(script_path),
        "--skill", skill,
        "--task", task,
        "--output-format", "json"
    ]
    # Spawns subagent as background process
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Parallel execution run
proc1 = run_subagent("tdd", "Implement data validation methods in src/utils.ts")
proc2 = run_subagent("tdd", "Write unit tests for data validation in src/tests.ts")

# Wait for completions
processes = [("Builder", proc1), ("Tester", proc2)]
for name, p in processes:
    p.wait()
    stdout, stderr = p.communicate()
    print(f"[{name}] Finished with return code: {p.returncode}")
    if p.returncode != 0:
        print(f"[{name}] Error: {stderr}")
```

### 3. Durable Agent Workflows with `upstash-workflow-js`
```typescript
import { serve } from "@upstash/workflow/nextjs";

export const { POST } = serve<{ taskId: string }>(async (context) => {
  const { taskId } = context.requestPayload;

  // Step 1: Fetch task metadata from temporary Redis cache
  const taskMeta = await context.run("fetch-metadata", async () => {
    const raw = await fetch(`https://api.system.local/tasks/${taskId}`);
    return await raw.json();
  });

  // Step 2: Delegate code execution to isolated cloud sandbox
  const sandboxResult = await context.run("run-sandbox", async () => {
    const res = await fetch("https://api.upstash.local/box/execute", {
      method: "POST",
      body: JSON.stringify({ command: `npx jest ${taskMeta.testFile}` })
    });
    return await res.json();
  });

  // Step 3: Check test results and alert if errors occur
  if (sandboxResult.status === "failed") {
    await context.run("trigger-alert", async () => {
      await fetch("https://api.system.local/alerts", {
        method: "POST",
        body: JSON.stringify({ message: `Task ${taskId} failed tests.` })
      });
    });
  }

  return { success: true };
});
```

### 4. HTTP Connection Pooling for `upstash-redis-js`
```typescript
import { Redis } from '@upstash/redis';

// To prevent socket leaks in serverless environments, initialize the client once.
// This establishes HTTP connections over TCP, avoiding standard connection leaks.
const redis = new Redis({
  url: process.env.UPSTASH_REDIS_REST_URL!,
  token: process.env.UPSTASH_REDIS_REST_TOKEN!,
});

export async function checkRateLimit(userId: string) {
  const limit = 60; // 60 requests
  const windowSeconds = 60; // per minute
  
  const current = await redis.incr(`rate:${userId}`);
  if (current === 1) {
    await redis.expire(`rate:${userId}`, windowSeconds);
  }
  
  return current <= limit;
}
```

---

## Coordinator-Child Multi-Agent Network (Code Blueprint)

This implementation shows a Supervisor coordinating two parallel child agents, merging the task status logs:

```typescript
import { LocalAgent } from 'google-antigravity-sdk';

interface SubagentTask {
  agentName: string;
  taskDescription: string;
}

export class AgentSupervisor {
  private supervisor: LocalAgent;
  
  constructor() {
    this.supervisor = new LocalAgent({
      model: 'gemini-2.5-pro',
      systemInstruction: 'Coordinate tasks between Builder and Tester subagents.'
    });
  }
  
  public async orchestrateTask(task: string) {
    console.log(`[Supervisor] Decomposing task: ${task}`);
    
    // 1. Plan division
    const subtasks: SubagentTask[] = [
      { agentName: 'Builder', taskDescription: 'Implement the feature in src/utils.ts' },
      { agentName: 'Tester', taskDescription: 'Create unit tests in src/tests.ts' }
    ];
    
    // 2. Parallel spawn simulated via Promise.all
    const results = await Promise.all(
      subtasks.map(async (sub) => {
        console.log(`[Supervisor] Spawning subagent: ${sub.agentName}`);
        const childAgent = new LocalAgent({
          model: 'gemini-2.5-flash',
          systemInstruction: `You are the ${sub.agentName} agent. Complete: ${sub.taskDescription}`
        });
        const response = await childAgent.execute(sub.taskDescription);
        return { agent: sub.agentName, output: response.text };
      })
    );
    
    // 3. Consolidation
    console.log('[Supervisor] Consolidating results...');
    const finalReport = await this.supervisor.execute(
      `Consolidate the following results into a markdown table:
${JSON.stringify(results)}`
    );
    return finalReport.text;
  }
}
```

---

## Upstash Vector Search Namespace Filtering Blueprint

This TypeScript blueprint handles document retrieval using targeted namespace namespaces and metadata filters:

```typescript
import { Index } from '@upstash/vector';

const index = new Index({
  url: process.env.UPSTASH_VECTOR_REST_URL!,
  token: process.env.UPSTASH_VECTOR_REST_TOKEN!,
});

export async function queryAgentKnowledgeBase(queryText: string, category: string) {
  // Query vectors within the 'documentation' namespace with metadata filter
  const queryResult = await index.query({
    data: queryText,
    topK: 5,
    includeMetadata: true,
    namespace: 'documentation',
    filter: `category = '${category}' AND status = 'active'`
  });
  
  return queryResult.map(match => ({
    id: match.id,
    score: match.score,
    text: match.metadata?.text || '',
    author: match.metadata?.author || 'Unknown'
  }));
}
```

---

## Safety Predicate Middleware Blueprint

Enforce tool-execution checks inside custom middleware:

```typescript
import { ToolCall } from 'google-antigravity-sdk';

export function runSafetyPredicate(toolCall: ToolCall): boolean {
  const command = toolCall.args.command || '';
  const forbiddenSubstrings = ['rm -rf', 'wget', 'curl', 'chmod', 'sudo'];
  
  if (forbiddenSubstrings.some(substring => command.includes(substring))) {
    console.warn(`[Safety Guard] Command execution blocked: contains forbidden substring. Command: ${command}`);
    return false;
  }
  
  return true;
}
```

---

## Sub-Skill Reference Manuals

### 1. Sandbox Environments & Repository Sync (`upstash-box-js`)
*   **Sandbox Initialization:** Provision dynamic cloud boxes for executing unverified code, running build scripts, or performing Git operations:
    ```typescript
    import { Box } from '@upstash/box';
    
    const box = new Box({
      apiKey: process.env.UPSTASH_BOX_API_KEY!
    });
    
    // Sync repository and run test suite
    const runResult = await box.run({
      repoUrl: "https://github.com/user/project.git",
      command: "npm install && npm run test"
    });
    console.log(runResult.stdout);
    ```

### 2. Rate Limiting & Traffic Protection (`upstash-ratelimit-js`)
*   **Sliding Window Algorithm:** Set up sliding window rate limiting to protect agent endpoints:
    ```typescript
    import { Ratelimit } from "@upstash/ratelimit";
    import { Redis } from "@upstash/redis";
    
    const ratelimit = new Ratelimit({
      redis: Redis.fromEnv(),
      limiter: Ratelimit.slidingWindow(10, "10 s"), // 10 requests per 10 seconds
      analytics: true
    });
    ```

### 3. CLI Diagnostics & Automation (`upstash-cli`)
*   **Status & Metric Auditing:** Run shell commands using the Upstash CLI to audit system status, trace queue delays, and check database sizes:
    ```bash
    upstash redis list --json
    upstash qstash stats
    ```

---

## Cross-Cutting Concerns
*   **Delegation:** Link with `ultimate-agent-workflow` to manage subagent prompts, context limits, and token budgets.
*   **Research:** Use `tavily-best-practices`, `perplexity-ask`, and `context7/get-library-docs` to gather API reference documentation.
*   **Validation:** Run `lint-and-validate` on all model configuration scripts, hooks, and tool classes.
*   **Review:** Use `superpowers-review` and `ponytail-review` to audit agent code for security flaws and code complexity.
*   **Git:** Coordinate branches, commits, and pushes using `ultimate-git-workflow` and `git-pushing`.
