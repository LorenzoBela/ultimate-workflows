---
name: ultimate-iot-hardware-workflow
description: Master workflow for schematic design, C++ firmware architectures, memory safety, and OTA updates.
---

# Ultimate IoT Hardware & Firmware Workflow

This workflow guides the end-to-end development of IoT physical components—covering schematic drafting, PCB trace layouts, cooperative C++ architectures, memory protections, watchdog integrations, and secure over-the-air (OTA) updates.

---

## 1. Schematic and PCB Layout Design
- **Sub-skills:** [iot-hw-schematic-design](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-hw-schematic-design/SKILL.md), [iot-hw-pcb-routing](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-hw-pcb-routing/SKILL.md), [iot-hw-bom-optimization](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-hw-bom-optimization/SKILL.md)
- Ensure all board entries are checked for decoupling capacitor allocations and boot strap pins.
- Route 50-ohm RF antenna traces and calculate trace widths for power domains.

## 2. Firmware Architecture & Cooperative Multi-Tasking
- **Sub-skills:** [iot-fw-no-block-loop](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-no-block-loop/SKILL.md), [iot-fw-peripheral-drivers](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-peripheral-drivers/SKILL.md), [iot-fw-led-signaling](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-led-signaling/SKILL.md)
- Write non-blocking loop architectures; reject any use of `delay()`.
- Place peripheral operations (SPI, I2C, UART) behind abstract drivers with built-in timeouts.

## 3. Reliability, Watchdogs, & Safety
- **Sub-skills:** [iot-fw-watchdog-timers](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-watchdog-timers/SKILL.md), [iot-fw-thermal-protection](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-thermal-protection/SKILL.md), [iot-fw-memory-safety](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-memory-safety/SKILL.md), [iot-fw-power-management](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-power-management/SKILL.md)
- Configure HW and Task watchdogs to reboot on freezes.
- Establish thermal protection cutoffs and prohibit run-time dynamic memory allocation.

## 4. Connectivity, Over-the-Air (OTA) Updates, & Hardening
- **Sub-skills:** [iot-fw-connection-resilience](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-connection-resilience/SKILL.md), [iot-fw-ota-updates](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-ota-updates/SKILL.md), [iot-fw-flash-encryption](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-flash-encryption/SKILL.md)
- Implement connection reconnect loops using exponential backoff.
- Use secure boot, flash encryption, and partitioning for firmware updates.

## 5. HIL Emulation & Physical Diagnostics
- **Sub-skills:** [iot-fw-hil-simulation](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-hil-simulation/SKILL.md), [iot-fw-debugging-jtag](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-debugging-jtag/SKILL.md)
- Verify code logic on developer desktops using synthetic sensor drivers.
- Debug physical hardware using logic analyzers, JTAG boundaries, and GDB.
