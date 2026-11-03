---
name: ultimate-embedded-programming-workflow
description: "Develop or diagnose firmware with target-specific register, RTOS, DMA, interrupt, memory and fault-recovery constraints. Verify timing and physical behavior on the selected target."
---

# Embedded firmware

Identify MCU/board revision, SDK, compiler/ABI, clock and memory map, peripheral ownership, ISR priorities, timing budgets and safe states. Use supported vendor definitions and verify initialization order, pin polarity, boot defaults and power transitions against the target.

## Choose mechanisms from the target

- **Interrupts and concurrency.** Keep interrupt work bounded. Use an SDK-supported ISR queue or notification with the documented priority restrictions. A single-producer/single-consumer queue is appropriate only with exactly one producer and consumer, explicit ordering and verified lock-free operations on the actual ABI. If atomics may lock, choose a supported ISR primitive or measure a bounded critical section. Volatile serves documented register access; synchronization needs a separate mechanism.
- **DMA and memory.** Check coherency, cache line alignment, sharing, buffer lifetime and ownership. Apply maintenance at the ownership transitions specified by the target. Derive allocation, stack and queue limits from measured peaks and failure behavior. Use a bounded RTOS wait when it meets scheduling and watchdog requirements.
- **Wire inputs.** Check buffer and field bounds before decoding, decode explicit endianness, validate ranges and check protocol integrity/authentication. Avoid treating native struct layout as a wire format. For ASCII, establish termination or use a length-aware parser. Test malformed and truncated frames.
- **State and recovery.** Define state transitions, deadlines and fault outputs. Feed the watchdog only after meaningful progress. Select fault capture and assertion behavior for the target runtime and failure model. Validate stack/frame availability before reading fault context and avoid unsafe logging or flash writes in a fault handler. Define what resets, brownouts and interrupted updates do to actuator state and persistent data.
- **Drivers.** Verify SDK/device configuration, electrical assumptions, timeout and error paths. Use unsigned wrap-safe timer logic where suitable and validate timing across wraparound and sleep. Keep network retries bounded and independent of time-critical control.

## Verify on the target

Use host tests for parsers, state transitions and queue logic. Measure ISR/task latency, starvation, stack high-water, memory/queue pressure and peripheral timing on the board. Exercise full/empty queues, malformed input, stuck peripherals, watchdog starvation, brownout, power loss during persistence/update and safe actuator shutdown as applicable. Report target and fixture details and any hardware checks still required before release.

## Role and handoffs

**Firmware engineer.** Own iSR, DMA, timing, and safe device behavior. Use [ultimate-hardware-design-workflow](../ultimate-hardware-design-workflow/SKILL.md) and [ultimate-iot-hardware-workflow](../ultimate-iot-hardware-workflow/SKILL.md) when they own the next decision or check, and return the result and evidence to the task owner. Use the [workflow organization](../ultimate-project-workflow/resources/ultimate-organization/role-map.md) for cross-specialty work.

## Representative acceptance case

On a target without proven lock-free atomics, select a supported ISR primitive. Verify DMA ownership and force a stuck peripheral or watchdog reset. Measure timing and safe actuator state on target.
