---
name: ultimate-iot-software-workflow
description: >
  Flawless 10/10 Master Workflow for IoT cloud backends, MQTT hierarchical namespaces, mutual TLS (mTLS) device auth,
  Kafka message decoupling, TimescaleDB/ClickHouse time-series ingestion, and JSON Device Twin synchronization.
  Triggers on "ultimate iot software workflow", "/ultimate-iot-software-workflow", or when
  designing IoT backends, configuring MQTT brokers, or building telemetry ingestion pipelines.
argument-hint: "[mqtt-topic | device-twin | telemetry-pipeline | --mtls | --timeseries]"
---

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
