---
name: ultimate-iot-hardware-workflow
description: >
  Engineering workflow for IoT hardware schematic design, PCB layout routing,
  non-blocking C++ firmware, hardware watchdog integration, flash encryption, and dual-bank OTA updates.
  Triggers on "ultimate iot hardware workflow", "/ultimate-iot-hardware-workflow", or when
  designing IoT devices, routing high-frequency traces, or authoring embedded firmware.
argument-hint: "[schematic | pcb-layout | firmware-arch | --ota | --watchdog]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate IoT Hardware & Firmware Workflow (Engineering Workflow)

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

1. **Bounded memory policy**: Select static allocation or bounded pools for hard real-time paths where required. SDK/network libraries may need dynamic allocation; document lifetime, failure handling, fragmentation and measured RAM/stack bounds.
2. **Scheduler-aware timing**: Keep cooperative event loops responsive with monotonic deadlines. Dedicated RTOS tasks may use bounded blocking waits that yield correctly; choose the target SDK primitives and verify cancellation/timeouts.
3. **Hardware Watchdog Protection**: Configure task/idle watchdog subscriptions for the selected SDK and feed only after bounded health progress; scheduler yielding and watchdog feeding are distinct requirements.
4. **Recoverable authenticated OTA**: On targets supporting A/B, update an inactive partition and validate signatures before selection; configure rollback and acknowledge health explicitly. On constrained targets, use a documented equivalent recovery design. A golden image is usable only if boot/anti-rollback policy permits it.
5. **Measured power management**: Select integrated load switches, PMOS gating or supported device sleep states for sensors/modems where appropriate to meet a measured sleep-current budget; account for switch leakage and GPIO back-powering.

---

## 🔬 The 4-Phase IoT Pipeline

### Phase 1: Schematic Design & RF Routing
- Route 50-ohm RF traces on Layer 1 over an unbroken Ground Plane on Layer 2.
- Follow selected component reference-layout decoupling/return-loop constraints; 2mm is an illustrative placement goal requiring layout review.

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
- Discover the actual SDK/target partition table and flash constraints; for ESP-IDF select `esp_ota_get_next_update_partition(NULL)`, never hardcode ota_1 or overwrite the active image. A/B storage is platform-dependent.
- Verify a cryptographic image signature using the configured trusted key and platform secure-boot/OTA mechanism. SHA-256 is a digest, not itself a signature. Also verify target identity, image bounds and security version.
- Enable and verify `CONFIG_BOOTLOADER_APP_ROLLBACK_ENABLE` on supported ESP-IDF targets. Set the candidate boot partition only after the complete image validates. On first boot run bounded health checks, then call `esp_ota_mark_app_valid_cancel_rollback()`; if unhealthy, use the documented invalid/rollback path. A restart before confirmation can trigger rollback when the configuration and a valid prior image support it.
- Coordinate anti-rollback eFuse/security-version policy with recoverability; an old image below the security floor cannot be assumed usable. Provision/rotate/revoke signing keys through an authorized manufacturing/release process and never expose private keys in logs or examples.

## Target verification and recovery

The scheduling example assumes transmitTelemetryData/serviceNetworkState are bounded nonblocking operations; verify their driver/network timeouts and task scheduling on the target. Adopt static allocation only when compatible with SDK/library lifecycles and measured RAM/stack constraints. Verify unsigned monotonic-timer wraparound behavior.

Before declaring OTA safe, run target/HIL cases for corrupted/unsigned/wrong-target images, active-partition protection, interrupted download, power loss while selecting an image, reset before health acknowledgement and successful confirmation. Confirm the exact rollback partition selected and availability after anti-rollback updates. Test brownout, stuck peripheral and watchdog starvation. Host mocks do not prove bootloader recovery, secure provisioning, thermal safety or sleep current; mark unavailable target evidence explicitly and retain that gate before production rollout.
