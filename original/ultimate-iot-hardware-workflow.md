---
name: ultimate-iot-hardware-workflow
description: >
  Flawless 10/10 Master Workflow for IoT hardware schematic design, PCB layout routing,
  non-blocking C++ firmware, hardware watchdog integration, flash encryption, and dual-bank OTA updates.
  Triggers on "ultimate iot hardware workflow", "/ultimate-iot-hardware-workflow", or when
  designing IoT devices, routing high-frequency traces, or authoring embedded firmware.
argument-hint: "[schematic | pcb-layout | firmware-arch | --ota | --watchdog]"
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

# Ultimate IoT Hardware & Firmware Workflow (10/10 Master Engine)

This workflow guides the end-to-end development of IoT physical devices and low-level firmware—covering schematic drafting, PCB trace layouts, cooperative non-blocking C++ architectures, memory protections, hardware watchdog integrations, and secure dual-bank over-the-air (OTA) updates.

```
                                      [IOT DEVICE HARDWARE / FIRMWARE SPEC]
                                                        │
                          ┌─────────────────────────────┴─────────────────────────────┐
                          ▼                                                           ▼
              [PHASE 1: SCHEMATIC ENTRY & RF LAYOUT]                        [PHASE 2: NON-BLOCKING FIRMWARE]
              ├─ Decoupling Capacitors on Every VDD                         ├─ Cooperative millis() Scheduling (No delay)
              ├─ 50-Ohm Controlled RF Antenna Trace                         ├─ Peripheral Drivers with Timeout Guards
              └─ High-Side PMOS Power Gating                                └─ Zero Dynamic Heap Allocations
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: HARDWARE WATCHDOGS & THERMAL SAFETY                │
        │  • Task Watchdog Timer Feeds • NTC Temperature Cutoffs • Safe Low-Power Sleep │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: DUAL-BANK OTA & SECURE BOOT]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🔄 DUAL-BANK │           │ 🔐 FLASH ENC │           │ 🧪 HIL TEST  │
            │ A/B Rollback │           │ Secure Boot  │           │ JTAG & GDB   │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of IoT Hardware & Firmware

1. **Zero Heap Allocation After Boot**: No `malloc`, `free`, `new`, or `delete` in runtime loops. All buffers are statically allocated.
2. **Never Block the Event Loop**: Calling `delay()` in the main thread is forbidden. All operations must use non-blocking monotonic clock comparisons (`millis()`).
3. **Hardware Watchdog Protection**: Every critical RTOS task must participate in watchdog pet routines (`esp_task_wdt_reset()`).
4. **Dual-Bank A/B Partitioning for OTA**: Firmware updates must download to an inactive partition, verify cryptographic hash/signatures, and fall back to the golden image if boot validation fails.
5. **High-Side Power Gating for Battery Life**: Power to sensors and radio modems must be gated via hardware PMOS switches to enable true zero-current sleep states.

---

## 🔬 The 4-Phase IoT Pipeline

### Phase 1: Schematic Design & RF Routing
- Route 50-ohm RF traces on Layer 1 over an unbroken Ground Plane on Layer 2.
- Place decoupling capacitors within 2mm of MCU power pins.

### Phase 2: Non-Blocking Firmware State Machine
```cpp
void loop() {
  uint32_t currentMillis = millis();
  
  if (currentMillis - lastTelemetryMillis >= TELEMETRY_INTERVAL_MS) {
    lastTelemetryMillis = currentMillis;
    transmitTelemetryData();
  }
  
  // Service network loop and watchdog
  serviceNetworkState();
  esp_task_wdt_reset();
}
```

### Phase 3: Secure Dual-Bank OTA Update
- Download update to `ota_1` partition.
- Verify SHA-256 signature against hardware public key.
- Set boot partition and trigger software restart. If crash loop occurs, bootloader reverts to `ota_0`.
