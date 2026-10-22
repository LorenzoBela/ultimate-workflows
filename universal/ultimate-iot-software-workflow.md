---
name: ultimate-iot-software-workflow
description: >
  Engineering workflow for IoT cloud backends, MQTT hierarchical namespaces, mutual TLS (mTLS) device auth,
  Kafka message decoupling, TimescaleDB/ClickHouse time-series ingestion, and JSON Device Twin synchronization.
  Triggers on "ultimate iot software workflow", "/ultimate-iot-software-workflow", or when
  designing IoT backends, configuring MQTT brokers, or building telemetry ingestion pipelines.
argument-hint: "[mqtt-topic | device-twin | telemetry-pipeline | --mtls | --timeseries]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate IoT Cloud & Software Backend Workflow (Engineering Workflow)

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

1. **Mutual TLS (mTLS) Authentication**: Use per-device authenticated identity appropriate to the supported platform; prefer hardware-protected mTLS where available, and document supported provisioning/rotation/revocation and compensating controls where hardware storage is unavailable.
2. **Decouple Broker from Database**: Keep ingestion bounded and recoverable. Select direct bounded writes, a durable queue or Kafka/RabbitMQ from throughput, loss tolerance and operating requirements; do not add infrastructure without an observed need.
3. **Protobuf Payloads Over Raw JSON**: Choose Protobuf/CBOR/JSON from measured bandwidth, CPU, evolution and interoperability needs; pin schema/codec versions and maintain backward-compatible decoding.
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

## Identity, event and command lifecycle

Bind authenticated device identity to tenant/device topic authorization for BOTH publish and subscribe; a valid certificate alone is insufficient. Provision unique identities, rotate before expiry, support revocation/decommissioning and audit lifecycle changes without logging private keys. Verify broker ACL wildcard behavior, retained-message permissions and session takeover behavior.

Telemetry envelopes include tenant/device identity, stable event ID or sequence/boot epoch, event time, ingest time, schema version and payload bounds. Use tenant-aware storage keys/indexes, deduplication and an explicit late/out-of-order/clock-skew policy. Specify acknowledgement/commit ordering, bounded buffer/backpressure, DLQ retention and replay rules; transport QoS does not by itself provide exactly-once database effects. Schema changes and compression syntax depend on the deployed database/version; example SQL is not a universal migration.

Twin updates use scoped versions/ETags and optimistic concurrency. Commands include authorized tenant/device/action, command ID/idempotency key, issue/expiry time, expected state/version and correlation ID. Device reports acceptance/execution/rejection with observed state; cloud reconciles bounded retries and stale acknowledgements. Reject expired/replayed commands and conflicting stale writes, and define offline desired-state behavior deliberately. Critical physical actions also require independent local interlocks, safe-state policy and suitable human/device authorization; an immutable log is evidence, not a safety mechanism.

Exercise cross-tenant publish/subscribe, credential expiry/revocation, duplicate/out-of-order telemetry, conflicting twins, expired/replayed commands, DB/broker outages, queue overflow and restart replay in disposable environments. Record actual persisted side effects and recovery latency against a declared budget. Staged OTA promotion requires health/error criteria, abort/recovery thresholds and compatible signed device firmware; the historical 5%/25% illustration is not a deployment policy.
