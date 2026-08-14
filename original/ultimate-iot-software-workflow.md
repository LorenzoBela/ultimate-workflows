---
name: ultimate-iot-software-workflow
description: Master workflow for MQTT design, mTLS auth, high-speed telemetry ingestion, device twins, and OTA rollouts.
---

# Ultimate IoT Cloud & Software Backend Workflow

This workflow guides the end-to-end design and deployment of IoT backend architectures—covering MQTT namespaces, mutual TLS (mTLS) device credentials, Kafka ingestion, time-series storage, device twins, and staged firmware rollouts.

---

## 1. Gateway Connectivity & Certificate Security
- **Sub-skills:** [iot-sw-mqtt-topic-design](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-mqtt-topic-design/SKILL.md), [iot-sw-mtls-device-auth](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-mtls-device-auth/SKILL.md), [iot-sw-mqtt-broker-config](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-mqtt-broker-config/SKILL.md)
- Design hierarchical MQTT topic architectures; restrict publishing permissions.
- Harden connections with mutual TLS (mTLS) X.509 client certificate checks.

## 2. Ingestion pipelines & Time-Series Storage
- **Sub-skills:** [iot-sw-telemetry-ingestion](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-telemetry-ingestion/SKILL.md), [iot-sw-time-series-storage](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-time-series-storage/SKILL.md), [iot-sw-data-payload-protobuf](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-data-payload-protobuf/SKILL.md)
- Decouple MQTT brokers from databases by bridging events into Kafka partitions.
- Optimize database write groups and apply compression algorithms to historical tables.

## 3. Device Management, Provisioning, & Twins
- **Sub-skills:** [iot-sw-device-twin-state](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-device-twin-state/SKILL.md), [iot-sw-device-provisioning](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-device-provisioning/SKILL.md), [iot-sw-ota-server-mgmt](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-ota-server-mgmt/SKILL.md)
- Structure JSON device twins to manage desired vs reported physical state.
- Coordinate bulk onboarding via ZTP and firmware registry dashboards.

## 4. Edge Analytics, Geolocation, & Real-Time UIs
- **Sub-skills:** [iot-sw-edge-analytics](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-edge-analytics/SKILL.md), [iot-sw-geolocation-tracking](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-geolocation-tracking/SKILL.md), [iot-sw-realtime-telemetry-ui](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-realtime-telemetry-ui/SKILL.md)
- Pre-process telemetry data using deadband filters and local averaging.
- Filter GPS jitter and stream events in real time to Next.js or mobile map screens.

## 5. System Health, Safety, & Audit Logs
- **Sub-skills:** [iot-sw-anomaly-detection](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-anomaly-detection/SKILL.md), [iot-sw-rate-limiting-devices](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-rate-limiting-devices/SKILL.md), [iot-sw-audit-log-actions](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-audit-log-actions/SKILL.md)
- Detect battery failures, lost heartbeat timers, and tamper triggers.
- Protect endpoints with connection limits and maintain signed audit logs of commands.
