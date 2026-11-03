---
name: ultimate-hardware-design-workflow
description: "Design and review PCBs, automotive or industrial power protection, signal integrity and manufacturing readiness using target requirements, exact component ratings and measured qualification evidence."
---

# Hardware design

## Establish the design basis

Identify supply and transient environment, applicable standard edition and severity, ambient conditions, load states, cell chemistry and part, I/O exposure, harness and bus topology, enclosure, fabrication stackup and product qualification needs. Capture nominal, worst-case and fault conditions. If vehicle class, transient source impedance or cell chemistry is unknown, record the gap and prepare the verification plan before selecting protection or charging parts.

## Schematic and component decisions

- **Power input.** Derive reverse-polarity, cranking, surge and brownout requirements from the source and applicable test profile. Compare clamping, series protection and hold-up by worst-case energy, tolerance, recovery and safe operating area. Check protected-node peaks at actual pulse current and temperature against downstream ratings. Check repeated pulses and failure behavior. Select actual part numbers after these checks.
- **Charging and backup.** Map exact cell and chemistry to the charger, protection thresholds, hot and cold inhibit, load sharing, storage and thermal derating. Evaluate peak and sleep current, aging and restart thresholds. Verify safe behavior if the sensor, battery or main source is absent or faulted.
- **External interfaces.** Select protection from the interface exposure, bandwidth and signal integrity. Place return paths and clamps to control surge current. Determine CAN termination from actual endpoints and existing terminations. Check relay suppression against switching device limits and required release behavior.
- **RF, switching and layout.** Use the module reference design and actual stackup. Preserve return paths and partition noisy current loops from sensitive RF/analog paths. Check antenna isolation and matching on the assembled device. Validate via, copper and enclosure assumptions against thermal and mechanical constraints.
- **Manufacturing.** Verify footprints against selected parts, alternate ratings and availability. Establish test access, programming/fixture points, assembly tolerances, stencil/reflow guidance and inspection criteria with the fabricator or assembler.

## Evidence and release

Trace each electrical and environmental requirement to schematic decisions, rating calculations and the applicable test. Review ERC/DRC, BOM and footprints. Use simulation for stated assumptions, then validate on the actual prototype with representative loads, instrumentation and fixture conditions. Include pulse, crank, thermal, signal integrity and EMC tests as applicable. Record board revision, test levels, observed margins, exceptions and recovery. Keep prototype readiness, physical qualification and formal certification as separate states.

## Role and handoffs

**Electrical and PCB engineer.** Own ratings, topology, and qualification. Use [ultimate-embedded-programming-workflow](../ultimate-embedded-programming-workflow/SKILL.md) and [ultimate-iot-hardware-workflow](../ultimate-iot-hardware-workflow/SKILL.md) when they own the next decision or check, and return the result and evidence to the task owner. Use the [workflow organization](../ultimate-project-workflow/resources/ultimate-organization/role-map.md) for cross-specialty work.

## Representative acceptance case

Trace a power requirement to the actual part, derated limits, worst-case calculation and bench method. Catch a charger chemistry mismatch or inadequate margin. Keep qualification pending without measurements.
