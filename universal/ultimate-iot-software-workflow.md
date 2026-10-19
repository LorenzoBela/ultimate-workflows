---
name: ultimate-iot-software-workflow
description: >
  Flawless 10/10 Master Workflow for IoT cloud backends, MQTT hierarchical namespaces, mutual TLS (mTLS) device auth,
  Kafka message decoupling, TimescaleDB/ClickHouse time-series ingestion, and JSON Device Twin synchronization.
  Triggers on "ultimate iot software workflow", "/ultimate-iot-software-workflow", or when
  designing IoT backends, configuring MQTT brokers, or building telemetry ingestion pipelines.
argument-hint: "[mqtt-topic | device-twin | telemetry-pipeline | --mtls | --timeseries]"
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

# Ultimate IoT Cloud & Software Backend Workflow (10/10 Master Engine)

This workflow guides the end-to-end design and deployment of IoT backend architectures—covering MQTT namespaces, mutual TLS (mTLS) device credentials, Kafka ingestion, time-series storage (TimescaleDB/ClickHouse), device twins, and staged firmware rollouts.

```
                                      [IOT TELEMETRY STREAM / MQTT INGRESS]
                                                        │
                          ┌─────────────────────────────┴─────────────────────────────┐
                          ▼                                                           ▼
              [PHASE 1: MTLS GATEWAY & MQTT BROKER]                         [PHASE 2: KAFKA DECOUPLING & INGEST]
              ├─ Mutual TLS (X.509 Device Certificates)                     ├─ Decouple MQTT Broker from DB
              ├─ Hierarchical Topic Trees (tenant/device/data)              ├─ Protobuf Binary Payload Parsing
              └─ Device Rate Limiting & Sliding Windows                     └─ Batch Buffer Ingestion Pipeline
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: TIME-SERIES STORAGE (TIMESCALE / CLICKHOUSE)       │
        │  • Hypertables • 10-Minute Compression Chunks • Deadband Geo Jitter Filter │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: DEVICE TWINS & STAGED OTA ROLLOUTS]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 👯 DEVICE TWN│           │ 🚀 STAGED OTA│           │ 📜 AUDIT LOG │
            │ Desired/Rep. │           │ 5% -> 25% -> │           │ Cryptographic│
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of IoT Cloud Backends

1. **Mutual TLS (mTLS) Authentication**: All edge IoT devices connecting to the MQTT/HTTP gateway MUST authenticate using hardware-stored X.509 client certificates.
2. **Decouple Broker from Database**: Never write directly to relational databases inside MQTT message handlers. Bridge MQTT messages into Kafka/RabbitMQ partitions.
3. **Protobuf Payloads Over Raw JSON**: Cellular IoT devices must transmit structured binary Protocol Buffers to minimize data costs and latency.
4. **Device Twin (Desired vs Reported State)**: Control commands must update the "desired" twin state in the cloud; the device confirms updates by publishing its "reported" state.
5. **Immutable Remote Override Audit Logs**: Critical commands (such as remote engine killswitches or solenoid locks) MUST be written to an immutable audit ledger before transmission.

---

## 🔬 The 4-Phase IoT Software Pipeline

### Phase 1: MQTT Topic Hierarchy & Security
- Namespace Format: `tenants/{tenantId}/devices/{deviceId}/telemetry`
- Command Format: `tenants/{tenantId}/devices/{deviceId}/commands/{commandId}`
- Client Certificate ACL: Devices may publish exclusively to their own device namespace.

### Phase 2: High-Speed Time-Series Ingestion (TimescaleDB)
```sql
CREATE TABLE device_telemetry (
  time TIMESTAMPTZ NOT NULL,
  device_id UUID NOT NULL,
  latitude DOUBLE PRECISION,
  longitude DOUBLE PRECISION,
  speed_kmh REAL,
  battery_voltage REAL,
  raw_payload JSONB
);

-- Convert to TimescaleDB Hypertable
SELECT create_hypertable('device_telemetry', 'time');

-- Enable automated compression on data older than 7 days
ALTER TABLE device_telemetry SET (
  timescaledb.compress,
  timescaledb.compress_segmentby = 'device_id'
);
SELECT add_compression_policy('device_telemetry', INTERVAL '7 days');
```

### Phase 3: JSON Device Twin Synchronization
```typescript
interface DeviceTwin {
  deviceId: string;
  desired: {
    lockState: 'LOCKED' | 'UNLOCKED';
    reportingIntervalSeconds: number;
  };
  reported: {
    lockState: 'LOCKED' | 'UNLOCKED';
    reportingIntervalSeconds: number;
    lastSeenAt: string;
  };
  version: number;
}
```
