---
name: ultimate-hardware-design-workflow
description: Master workflow for schematic entry, high-speed PCB routing, signal integrity, and manufacturing assembly.
---

# Ultimate Electronics Hardware Design Workflow
## The Hardware Architect's Bible: Hardcore Rules for Automotive & Telematics PCBs

This workflow defines the absolute standards, constraints, and pipelines for designing, simulating, and routing high-reliability electronic hardware. It is written for automotive, industrial, and telematics hardware (such as vehicle tracking devices, fuel level monitors, OBD-II interfaces, and video telematics modules) that must withstand harsh electrical noise, thermal swings, and mechanical vibrations.

It is designed in perfect harmony with the [ultimate-embedded-programming-workflow](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/ultimate-embedded-programming-workflow/SKILL.md). Every hardware choice is mapped directly to a corresponding firmware control constraint.

---

## 1. The Ten Commandments of Automotive Hardware Design

1.  **Thou Shalt Defend Against Alternator Load Dumps (ISO 7637-2 Pulse 5a/5b):** A load dump occurs when the vehicle battery is disconnected while charging, sending an 80V–100V surge for up to 400ms. Place a high-power TVS diode (e.g., SM8S36A) or an active overvoltage surge stopper (e.g., LTC4365) at the main power input.
2.  **Thou Shalt Survive Cranking Drops (ISO 16750-2 Cold Cranking):** When the engine starts, the 12V rail drops to 3V–5V. Regulators must be wide-input buck-boost converters, or downstream supply circuits must have large bulk aluminum electrolytic capacitors (hold-up caps) to prevent the MCU from resetting.
3.  **Thou Shalt Protect Against Reverse Polarity:** Install a P-channel MOSFET in series with the input line (gate tied to ground via a zener/resistor protection clamp) to provide low RDS(on) reverse voltage protection.
4.  **Thou Shalt Enforce 50-Ohm Impedance on RF Traces:** Route GPS/GNSS and cellular RF lines as 50-ohm coplanar waveguides. Calculate trace widths based on the PCB stackup and dielectric constant ($E_r$).
5.  **Thou Shalt Cut Out Grounds Under RF Pads:** Remove the ground plane directly below the passive component pads (capacitors/inductors) in the RF matching network to prevent parasitic capacitance from shifting the resonance frequency.
6.  **Thou Shalt Isolate Cellular and GNSS Antennas:** Place the GNSS antenna and cellular antenna as far apart as possible (minimum 10cm or >20dB isolation) to prevent cellular transmit pulses from desensitizing the GNSS Low Noise Amplifier (LNA).
7.  **Thou Shalt Clamp External Sensor Lines (ESD Protection):** Wires running along the chassis (like fuel probes or ignition lines) act as antennas for ESD and EMF. Every external input pin on the connector must have a TVS diode (e.g., PESD12VS2UT) and an RC low-pass filter.
8.  **Thou Shalt Use Split CAN Termination:** When routing CAN bus interfaces (OBD-II / J1939), terminate with a split configuration (two 60-ohm resistors in series with a 4.7nF capacitor to ground from the center tap) to filter out high-frequency common-mode noise.
9.  **Thou Shalt Dedicate Solid Ground Planes:** Use a minimum of a 4-layer stackup: Signal/Power/Ground/Signal. The Ground layer under RF and high-speed MCU signals must be unbroken.
10. **Thou Shalt Validate Thermal Vias:** Place thermal vias directly under the exposed pads of power regulators, thermal-relief them, and connect them to solid copper planes on inner and bottom layers to dissipate heat without heatsinks.

---

## 2. ISO 7637-2 Automotive Transient Immunity Matrix

Automotive power lines contain transients caused by switching inductive loads (relays, starter motors, clutches). The hardware must incorporate protection circuits for each pulse category:

| Pulse | Source | Voltage Range | Duration | Mitigation Component |
|---|---|---|---|---|
| **Pulse 1** | Disconnection of inductive loads from power | -100V to -150V | 2 ms | Input Schottky or PMOS Reverse Protection clamp |
| **Pulse 2a** | Current interruption in wiring harness series | +37V to +55V | 0.05 ms | Input LC decoupling filter + Bypass capacitors |
| **Pulse 2b** | DC motor running as generator after ignition switch | +10V to +32V | 200 ms | Buck converter operating over wide $V_{IN}$ (up to 40V) |
| **Pulse 3a** | High-frequency negative switching spikes | -150V to -200V | 0.1 microseconds | Common-mode choke + Fast ESD TVS diodes |
| **Pulse 3b** | High-frequency positive switching spikes | +100V to +200V | 0.1 microseconds | Common-mode choke + Fast ESD TVS diodes |
| **Pulse 5a/5b** | Alternator Load Dump (severed battery line) | +65V to +120V | 400 ms | Clamping TVS Diode (SM8S36A) or LTC4365 Surge Switch |

---

## 3. Power Supply Design & Transient Clamping (Firmware BOD Harmony)

Automotive electrical networks are notoriously noisy. You must design input protection stages to suppress surges, ESD, and reverse conditions before power reaches Buck/LDO converters.

```mermaid
graph LR
Vin[12V/24V Input] --> RevProt[PMOS Reverse Protection]
RevProt --> TVS[TVS Clamping: SM8S36A]
TVS --> PiFilter[LC Pi Filter]
PiFilter --> Buck[Wide Input Buck: e.g. LM25011]
Buck --> LDO[Clean 3.3V LDO for MCU/GNSS]
```

### Input Filter Design Rules
1.  **Reverse Protection:** Use a PMOS transistor (e.g., DMP4015SPS) for minimal voltage drop compared to a Schottky diode.
2.  **Surge Suppression:** Clamp transients using a TVS diode rated for peak load dump pulses. The clamping voltage must sit below the maximum input rating of the buck converter.
3.  **Differential & Common-Mode Filtering:** Place an LC Pi filter (Inductor + Decoupling Capacitors) after the TVS to filter high-frequency switching noise before it couples into the power rail.
4.  **Brownout Detection (BOD) Calibration:** Connect a precision resistor divider from the raw $V_{IN}$ to an analog comparator pin on the MCU. This hardware divider allows the firmware to detect a voltage drop before the buck output fails, enabling emergency logs.

---

## 4. TVS Diode Parameter Selection Calculations

When selecting TVS protection diodes for external connections, the hardware engineer must calculate and match four primary parameters to ensure protection without loading the signals:

*   **Reverse Working Maximum Voltage ($V_{RWM}$):**
    *   Must be higher than the maximum normal operating voltage of the protected line.
    *   *Example (12V Automotive Power Rail):* Normal $V_{IN} = 12\text{V}$, charging spikes up to $18\text{V}$. Choose $V_{RWM} \geq 24\text{V}$.
*   **Breakdown Voltage ($V_{BR}$):**
    *   The voltage at which the TVS begins to conduct and shunt current to ground. Typically measured at $I_T = 1\text{mA}$.
*   **Clamping Voltage ($V_C$):**
    *   The maximum voltage across the TVS during a peak current pulse ($I_{PP}$). This voltage **MUST** remain below the absolute maximum input voltage of the protected downstream chip (e.g., the CAN transceiver or Buck converter input).
*   **Parasitic Capacitance ($C_J$):**
    *   For high-speed lines (CAN bus, USB, RF), the capacitance of the TVS must be extremely low (typically $< 3\text{pF}$) to prevent signal edge degradation.
    *   For low-frequency lines (Power rails, Analog fuel probes), high capacitance (up to $1\text{nF}$) is acceptable and provides supplementary high-frequency noise filtering.

---

## 5. Hardware Power Gating & Low-Power Architectures

To implement the firmware's low-power modes, the hardware must be able to cut power to external peripherals (cellular modems, GNSS modules, active sensors) completely when not in use.

### High-Side Load Switch Implementation
*   Do not leave inactive sensors powered via logic pins (preventing back-powering MCU GPIOs).
*   Use a P-channel MOSFET (or a dedicated integrated load switch) to gate the VCC line of the cellular modem and fuel level transceivers:
    ```
             VCC_SYS (3.3V / 4.0V)
                   │
                   ▼ Source
              ┌─────────┐
         Gate │  PMOS   ├──────► Drain VCC_MODEM (To Cellular Module)
          ┌───┤  MOSFET │
          │   └─────────┘
         [R] Pull-Up
          │
          ├───► Collector / Drain
         [N] NPN Transistor / NMOS
          │    Gate controlled by MCU GPIO
          ▼ Emitter / Source (GND)
    ```
*   When the MCU pin goes LOW, the NMOS turns off, the PMOS gate is pulled to VCC_SYS, and the cellular module is completely powered off (drawing 0mA).

---

## 6. High-Speed RF & Signal Integrity Layout

Improper RF routing leads to dropped satellite fixes, cellular link drops, and poor network throughput.

*   **RF Coplanar Waveguide Routing:**
    *   Maintain a continuous reference ground plane directly beneath the RF trace on Layer 2.
    *   Do not route other signal lines parallel to or beneath the RF trace.
    *   Surround the RF trace on Layer 1 with ground copper pours stitched with vias to the ground plane (via-stitching shield).
*   **GNSS LNA Protection:**
    *   GNSS signals are weak (~-130dBm to -160dBm). If using an active antenna, provide a clean bias tee (inductor-capacitor network) to supply DC power to the LNA without injecting noise.
    *   Place a dedicated SAW filter between the LNA and the GNSS receiver input to reject out-of-band cellular transmission noise.

---

## 7. Connector Pin ESD & Filter Hardening (Fuel Sensors & Relays)

Every pin routed outside the enclosure (e.g., Power, Ground, RS485 for fuel sensors, RFID digital lines) is an entry point for electrostatic discharge (ESD).

```
   External Connector Pin 
            │
            ▼
   ┌─────────────────┐
   │  TVS Diode      │  ◄── Placed closest to the physical connector pin
   └────────┬────────┘
            │
            ▼
   ┌─────────────────┐
   │  Series Resistor│  ◄── 10 to 100 Ohm to limit ESD current spikes
   └────────┬────────┘
            │
            ▼
   ┌─────────────────┐
   │  Filter Cap     │  ◄── 100pF to 10nF to ground (Low-pass filter)
   └────────┬────────┘
            │
            ▼
   Internal MCU / Transceiver Pin
```

*   **RS485 Bus Protection (Fuel Probe Interface):**
    *   Use a dedicated RS485 transceiver (e.g., MAX3485) with built-in fault protection.
    *   Add gas discharge tubes (GDTs) or fast TVS arrays on the A and B communication lines to clamp high-energy induction surges from long cable harnesses.
*   **Inductive Kickback Diodes (Ignition Relay Control):**
    *   When driving external engine-cut relays, always place a flyback diode (e.g., 1N4007) in parallel with the relay coil to suppress the high-voltage inductive spike when the transistor switches off.

---

## 8. Li-Ion/LiFePO4 Backup Battery Charging Circuits

A telematics tracker must operate even if the main car battery is cut. Integrate a charging and protection block that can withstand extreme vehicle cabin temperatures:

*   **Thermally Safe Battery Charging:**
    *   Deploy a dedicated charger IC (e.g., MCP73833) with a thermal NTC thermistor input.
    *   Locate the thermistor directly against the battery pouch.
    *   Configure the IC to cut charging immediately if the battery temperature exceeds 45°C (to prevent swelling and thermal runaway inside closed vehicle dashboards).
*   **Over-discharge & Over-charge Protection:**
    *   Add a protection IC (e.g., AP9101C) in series with the cell to cut off current if the battery falls below 2.8V (over-discharge) or exceeds 4.25V (over-charge).

---

## 9. Backup Battery Lifespan & Power Consumption Calculations

When designing the backup power paths, the hardware engineers must perform current budget calculations to verify operating lifespans against firmware profiles:

*   **Current Consumption Variables:**
    *   $I_{active}$ (GPRS TX burst peak): 2000 mA (lasts for ~577 microseconds per GSM slot).
    *   $I_{transmitting}$ (Average transmitting): 250 mA.
    *   $I_{sleep}$ (Cellular standby, MCU sleeping, GNSS standby): 2.5 mA.
    *   $I_{deep\_sleep}$ (Cellular powered off, MCU deep sleep wake-on-RTC, GNSS powered off): 75 microamps.
*   **Battery Capacity Lifespan Equation:**
    $$T_{hours} = \frac{\text{Battery Capacity (mAh)}}{I_{avg} \text{ (mA)}}$$
    *   *Case A: Continuous GPS + Cellular Transmitting (450mAh Cell)*
        $$T = \frac{450}{250} = 1.8 \text{ hours}$$
    *   *Case B: Cyclic Telematics Wakeup (1 min active transmission of 250mA, 59 mins deep sleep of 75uA)*
        $$I_{avg} = \frac{(250 \text{ mA} \times 60 \text{ sec}) + (0.075 \text{ mA} \times 3540 \text{ sec})}{3600 \text{ sec}} \approx 4.23 \text{ mA}$$
        $$T = \frac{450}{4.23} \approx 106.3 \text{ hours} \approx 4.4 \text{ days of backup operation}$$

---

## 10. Automotive Wiring Harness & Chassis Grounding Guidelines

Reliable telemetry hardware requires a robust external wiring layout:

*   **Standard Telematics Wire Gauge Selection:**
    *   **Main 12V/24V Power & Ground:** Use AWG 18 wire to withstand currents and mechanical stress.
    *   **Ignition Sense & Digital Inputs:** Use AWG 22 wire.
    *   **Serial Communication Lines (RS485):** Use shielded twisted pair (STP) AWG 24 to prevent EMI from the vehicle's ignition coils.
*   **Color-Coding Standards for Professional Installations:**
    *   **Red:** Constant Battery +12V/+24V.
    *   **Black:** Chassis Ground.
    *   **Orange:** Ignition Accessory (+12V/+24V active only when key is ON).
    *   **Yellow:** Negative output to Starter Relay (immobilizer coil trigger).
    *   **Green/White:** RS485-A / RS485-B for external fuel sensor integration.
*   **Ground Loop Prevention:**
    *   Ensure the tracker is grounded directly to a solid factory chassis bolt.
    *   Do not share the ground point with high-power audio amplifiers or lighting controllers to prevent voltage shifts on the RS485 bus.

---

## 11. IoT-SkillsBench Peripheral Electrical Interface Matrix (The 23 Peripherals)

Every peripheral schematic connection must adhere to these hardware integration rules:

| # | Peripheral | Interface | Required Passive Components & Layout Constraints |
|---|---|---|---|
| 1 | **LED** | Digital GPIO | Series current-limiting resistor (e.g. 330 Ohm for 3.3V rails) to clamp maximum forward current. |
| 2 | **Push Button** | Digital GPIO | 10k Ohm pull-up/pull-down resistor; 100nF parallel ceramic capacitor close to MCU for hardware debouncing. |
| 3 | **Active Buzzer** | Digital GPIO | Low-side NPN/NMOS drive transistor with a 1k Ohm base resistor; flyback diode across coil. |
| 4 | **Passive Buzzer** | PWM GPIO | Series 10uF DC-blocking capacitor to prevent continuous DC bias heating the coil. |
| 5 | **Relay Module** | Digital GPIO | Optoisolated driver circuit separating the 5V/12V relay coil supply from the 3.3V MCU digital plane. |
| 6 | **Laser Emitter** | Digital GPIO | NPN transistor switch with low-value series resistor to govern diode bias current limit. |
| 7 | **Rotary Encoder** | Digital GPIO | 10k Ohm pull-ups on both A and B outputs; 10nF filter capacitors to GND to filter mechanical bounce. |
| 8 | **16-Key Keypad** | Digital GPIO | 1k Ohm series resistors on column lines to protect MCU pins during simultaneous multi-key presses. |
| 9 | **Tilt Switch** | Digital GPIO | 10k Ohm pull-up resistor; 100nF filter capacitor to GND to suppress transient state switches. |
| 10| **Analog Joystick** | ADC Input | 100nF decoupling capacitors on X and Y wiper contacts to filter high-frequency wiper noise. |
| 11| **Photoresistor** | ADC Input | Voltage divider with a static 10k Ohm resistor ($\pm1\%$ tolerance) to establish a stable reference sweep. |
| 12| **TMP36 Temp** | ADC Input | 100nF bypass capacitor directly across $V_{IN}$ and GND pins; series 1k Ohm resistor to ADC input. |
| 13| **Water Level** | ADC Input | High-side PMOS switch gating the sensor's power line to prevent continuous current flow and probe erosion. |
| 14| **PIR Motion** | Digital GPIO | 10k Ohm pull-up/pull-down on signal line; 10uF bulk electrolytic capacitor close to sensor for power stability. |
| 15| **Ultrasonic** | Digital GPIO | Level-shifter (e.g., BSS138) on Echo pin: shifts 5V sensor output to 3.3V safe levels for MCU. |
| 16| **Sound Sensor** | Digital GPIO | 100nF bypass caps on comparator IC; 10k Ohm pull-up on the open-drain digital output line. |
| 17| **Shock Sensor** | Digital GPIO | 10k Ohm pull-up; 100nF filter capacitor to GND to suppress mechanical ring frequencies. |
| 18| **DHT11 Sensor** | 1-Wire GPIO | 4.7k Ohm pull-up resistor on the single-wire data line; 100nF decoupling capacitor across VCC/GND. |
| 19| **DS18B20 Temp** | 1-Wire GPIO | 4.7k Ohm pull-up resistor; 100nF local bypass capacitor directly across sensor VCC and GND. |
| 20| **LCD1602 Display**| Parallel / I2C | 10k Ohm single-turn potentiometer connected to $V_0$ pin to adjust liquid crystal contrast. |
| 21| **DS1307 RTC** | I2C Bus | 32.768kHz crystal oscillator routed with Guard Rings; 5V-to-3.3V bidirectional I2C level translator. |
| 22| **MPU6050 Accel** | I2C Bus | 4.7k Ohm pull-up resistors on SDA/SCL lines; 100nF and 10uF bypass capacitors placed adjacent to VDD. |
| 23| **BME280 Sensor** | I2C / SPI | 100nF decoupling capacitor on VDD and VDDIO; 4.7k Ohm pull-ups on SDA/CSB pins to prevent floating states. |

---

## 12. Enclosure Environmental Sealing (IP67/IP68 Standards)

Automotive tracking and telemetry modules are frequently exposed to moisture, road salt, dust, and temperature-driven pressure fluctuations:

*   **Silicone Gasket Compression:** Use a molded silicone gasket around the enclosure parting line. Ensure a minimum compression of 30% to prevent ingress.
*   **Potting Compounds:** For external sensors (e.g., fuel probe caps), pot the entire terminal cavity with a polyurethane or epoxy potting compound to prevent moisture intrusion.
*   **Pressure Equalization Venting:**
    *   Thermal cycles inside closed boxes cause internal pressure changes. This pulls moisture in through wire interfaces.
    *   Integrate a hydrophobic venting membrane (e.g., Gore Automotive Vent) to allow air pressure equalization while blocking liquid water and dust.

---

## 13. Debug Ports, Indicators, & Factory Testbeds

Production hardware must support debugging and automated testing.

*   **SWD / JTAG Test Header:**
    *   Always place SWDIO, SWCLK, RESET, VCC, and GND test points on the PCB.
    *   Incorporate ESD protection diodes on SWD lines if they are exposed on the external casing.
*   **Diagnostic LED Architecture:**
    *   Implement Status LEDs driven by MCU GPIOs to indicate states:
        *   **Solid Green:** System Power/OK.
        *   **Blinking Blue:** Cellular Link active.
        *   **Blinking Amber:** GNSS searching/no fix.
        *   **Blinking Red:** Crash Fault logged.
*   **Bed-of-Nails Testpoints:**
    *   Ensure all primary power rails, UART TX/RX lines, sensor comparator lines, and boot pins have exposed, gold-plated circular test pads (minimum 1.0mm diameter) on the bottom layer of the board.
    *   Keep test pads away from high-speed RF lines to avoid signal degradation.

---

## 14. Manufacturing PCB Stencil & Reflow Soldering Parameters

To guarantee high manufacturing yield and prevent component misalignment:

*   **Ground Pad Stencil Design:** Stencil apertures for large ground thermal pads must be cross-hatched (matrix layout) rather than a single solid square. This avoids excess solder paste that can cause chips to float or bridge adjacent signal pins.
*   **Lead-Free Solder Profile (SAC305):** Configure the reflow profile to maintain a liquidus temperature above 217°C for 60 to 90 seconds, peaking at 240°C–245°C.

---

## 15. Mandatory AI Hardware Design Guidelines

When the AI agent generates schematics, layout recommendations, or circuit topologies, it **MUST** enforce the following constraints:

1.  **Transient Protection Mandate:** Every DC power input schematic must include transient clamping (TVS diode) and reverse polarity protection (PMOS or Schottky).
2.  **Passive Gating:** Always provide NMOS/PMOS load switches for cellular modems and active sensor arrays to enable firmware-controlled low-power cycling.
3.  **Split CAN Termination:** Standard CAN transceiver layouts must use split termination (60-ohm x2 + capacitor to GND) rather than a single 120-ohm resistor.
4.  **No Single Ground Vias for Power:** High-current paths (such as Buck converters and cellular modems) must use multiple stitched vias to Ground to minimize trace impedance.
5.  **ESD Clamps at Boundaries:** All external communication lines (RS485, digital input pins) must have TVS protection placed directly adjacent to the connector footprint.

---

## 16. The 5-Phase Electronics Design Pipeline & Core Sub-Skills

This section documents the execution pipeline and indexes all specialized hardware sub-skills required to complete an automotive-grade board.

### Phase 1: Schematic Entry, BOM Optimization, & Connector Rigidity
*   **Active Sub-skills:**
    *   [hw-design-schematic-capture](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/hw-design-schematic-capture/SKILL.md) — Multi-sheet hierarchical schematic configurations and footprint mappings.
    *   [hw-design-component-sourcing](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/hw-design-component-sourcing/SKILL.md) — Lifecycles of parts, alternative vendor mapping, and cost optimizations.
    *   [hw-design-connector-selection](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/hw-design-connector-selection/SKILL.md) — Pitch constraints, current tolerances, locking tabs, and IP-grade waterproofing specs.
    *   [iot-hw-bom-optimization](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-hw-bom-optimization/SKILL.md) — Standardizing passive component packages (0603/0402) to maximize manufacturing efficiencies.
    *   [iot-hw-schematic-design](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-hw-schematic-design/SKILL.md) — Strapping pin configurations, ESD array alignments, and MCU power pin decoupling.
*   **Core Standards:** Check footprints against physical data sheets. Generate Netlists and resolve all open floating nodes before proceeding.

### Phase 2: Power Rails, Battery Charging, & SPICE Analogs
*   **Active Sub-skills:**
    *   [hw-design-simulation-spice](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/hw-design-simulation-spice/SKILL.md) — Running SPICE simulations for transient clamping circuits and input LC filters.
    *   [hw-design-power-integrity](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/hw-design-power-integrity/SKILL.md) — Voltage regulator routing, plane allocations, and decoupling loop paths.
    *   [hw-design-battery-charging](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/hw-design-battery-charging/SKILL.md) — Battery charger configuration, zener clamping, and thermal NTC cut-off lines.
*   **Core Standards:** Run simulations for inputs up to 100V. Assert buck converter stability under load transitions from 100mA to 2A.

### Phase 3: PCB Layout, Impedance Matching, & Signal Integrity
*   **Active Sub-skills:**
    *   [hw-design-pcb-routing](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/hw-design-pcb-routing/SKILL.md) — Layer stackups, trace parameters, differential width guides, and ground returns.
    *   [hw-design-signal-integrity](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/hw-design-signal-integrity/SKILL.md) — Length matching CAN high/low lines, preventing crosstalk, and routing loop area restrictions.
    *   [hw-design-rf-antenna-matching](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/hw-design-rf-antenna-matching/SKILL.md) — Coplanar waveguide matching, SAW filter designs, and Pi-network component placements.
    *   [iot-hw-pcb-routing](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-hw-pcb-routing/SKILL.md) — Isolation of RF antennas, routing high-current GSM bursts, and shielding MCU clock oscillators.
*   **Core Standards:** Route 50-ohm RF traces on Layer 1 with ground reference plane on Layer 2. Ensure CAN trace skew is under 0.15mm.

### Phase 4: Mechanical Outlines & Thermal Simulations
*   **Sub-skills:**
    *   [hw-design-mechanical-cad](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/hw-design-mechanical-cad/SKILL.md) — Exporting 3D STEP models to CAD to check clearances inside the vehicle OBD-II housings.
    *   [hw-design-thermal-sim](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/hw-design-thermal-sim/SKILL.md) — Thermal via layout arrays and passive PCB heatsink calculations.
*   **Core Standards:** Position thermal vias directly under the exposed pads of power regulators, thermal-relief them, and connect them to solid copper planes on inner and bottom layers.

### Phase 5: DFM Checking, Factory QA Testbeds, & EMC Verification
*   **Sub-skills:**
    *   [hw-design-manufacturing-dfm](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/hw-design-manufacturing-dfm/SKILL.md) — Fiducials, panelization structures, component orientations, and pick-and-place clearances.
    *   [hw-design-emc-compliance](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/hw-design-emc-compliance/SKILL.md) — Shielding, common-mode chokes, ground loop avoidance, and automotive CISPR-25 emissions limits.
    *   [hw-design-physical-prototyping](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/hw-design-physical-prototyping/SKILL.md) — Manual solder stencils, reflow profiles, and rework guidelines.
    *   [hw-design-testpoint-bed](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/hw-design-testpoint-bed/SKILL.md) — Factory bed-of-nails test fixtures, test point locations, and automated software diagnostics checks.
*   **Core Standards:** Perform board clearance checks. Verify all test pads are on the bottom side of the board and exceed 1.0mm in diameter to ensure high probing yield.
