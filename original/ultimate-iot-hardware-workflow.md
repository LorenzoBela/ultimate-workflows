---
name: ultimate-iot-hardware-workflow
description: >
  Flawless 10/10 Master Workflow for IoT hardware schematic design, PCB layout routing,
  non-blocking C++ firmware, hardware watchdog integration, flash encryption, and dual-bank OTA updates.
  Triggers on "ultimate iot hardware workflow", "/ultimate-iot-hardware-workflow", or when
  designing IoT devices, routing high-frequency traces, or authoring embedded firmware.
argument-hint: "[schematic | pcb-layout | firmware-arch | --ota | --watchdog]"
---

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
