---
name: ultimate-embedded-programming-workflow
description: Master workflow for bare-metal registers, RTOS scheduling, interrupt handling, and exception fault diagnostics.
---

# Ultimate Embedded Systems Programming Workflow
## The Architect's Bible: Hardcore Rules for Production-Grade C & C++ Firmware

This workflow defines the absolute standards, constraints, and pipelines for writing C and C++ firmware. It is written for critical, long-running systems (such as medical devices, automotive modules, aerospace guidance, or remote smart box controllers) where a single crash, memory leak, or register corruption is a catastrophic system failure.

It is designed in perfect harmony with the [ultimate-hardware-design-workflow](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/ultimate-hardware-design-workflow/SKILL.md). Every firmware choice is mapped directly to a corresponding hardware constraint.

---

## 1. The Ten Commandments of Embedded Firmware (C & C++)

1.  **Thou Shalt Commit to the Zero-Heap Invariant:** The heap is thy enemy. No dynamic memory allocation (`malloc`, `free`, `realloc`, `new`, `delete`) after initialization. All structures must have static or stack-based lifetimes.
2.  **Thou Shalt Block No Execution Threads:** Blocking is a design failure. Never use blocking delay functions in the main thread. All timing must be managed asynchronously using non-blocking state machines and monotonic hardware clocks (`millis()` / `micros()`).
3.  **Thou Shalt Design for Physical Fail-Safe Boundaries:** If the MCU freezes, the hardware must not catch fire. Configure watchdogs to force resets, and use hard-coded thermal limits to cut power to high-current actuators (e.g., solenoids, heaters) after a fixed duration.
4.  **Thou Shalt Treat Interrupts (ISRs) as Sacred:** Keep ISRs under 10 microseconds. Do not call slow library functions, print to serial, or allocate memory inside an ISR. Clear the interrupt flag immediately, queue the event, and defer processing to an RTOS task.
5.  **Thou Shalt Enforce Strong Type Safety:** Ban raw `int` and `long` types. Use explicit-width types (`uint8_t`, `int32_t`, `uintptr_t`) from `<stdint.h>`. Enforce strict enum validations to prevent implicit integer casting.
6.  **Thou Shalt Compile with Hardened Flags & Static Analyzers:** Compile out dynamic features. Disable Exceptions (`-fno-exceptions`) and RTTI (`-fno-rtti`) for C++. Enforce stack protector checks (`-fstack-protector-strong`) and static analysis gates (`cppcheck`, `clang-tidy`, MISRA C validation).
7.  **Thou Shalt Pack and Align Structures Deliberately:** Structures mapped to communication buses (CAN, SPI, UART) must be packed explicitly using `__attribute__((packed))` or `#pragma pack(push, 1)`. Manually pad fields to prevent alignment fault exceptions on 32-bit registers.
8.  **Thou Shalt Maintain Cache Coherency during DMA:** When transferring data via DMA on MCUs with L1 caches, always execute clean operations before transmitting and invalidations after receiving.
9.  **Thou Shalt Abstract the Hardware Layers:** Decouple application logic from physical pins. Put all drivers behind clean Hardware Abstraction Layers (HAL) so code can be unit-tested on host PCs using mocks.
10. **Thou Shalt Instrument for Post-Mortem Diagnostics:** Configure exception handlers to catch `HardFault`, `MemManage`, and `BusFault` crashes. Extract the Program Counter (PC) and Link Register (LR) context and write them to non-volatile backup registers before resetting.

---

## 2. Hardcore MISRA C:2012 & Defensive Programming Laws

When writing pure C firmware, follow these strict directives to guarantee memory safety and compile-time determinism:

*   **Rule-Based Variable Scoping:**
    *   Ban global variables. If shared variables are necessary, scope them as `static` file-scope variables.
    *   Pass context structures using pointers to modify task state:
        ```c
        typedef struct { uint32_t lastRead; bool isActive; } sensor_ctx_t;
        void sensor_update(sensor_ctx_t *const ctx);
        ```
*   **Volatile & Const Pointer Qualifications:**
    *   Read-only buffers passed to functions must be qualified as const pointers to const data:
        ```c
        void send_data(const uint8_t *const buffer, const size_t length);
        ```
    *   Declare registers and pointers to DMA buffers as volatile to prevent compiler optimization sweeps.
*   **The Inline Function Mandate:**
    *   Banish complex macro functions (`#define MULTIPLY(a,b) a*b`) due to double-evaluation and precedence bugs.
    *   Use `static inline` functions to ensure full type checking by the compiler:
        ```c
        static inline uint32_t clamp_value(uint32_t val, uint32_t min, uint32_t max) {
            return (val < min) ? min : (val > max) ? max : val;
        }
        ```
*   **Strict Return Checks:**
    *   Every interface function must return an explicit status code (e.g., `typedef enum { STATUS_OK, STATUS_BUSY, STATUS_ERROR } status_t;`).
    *   The caller must check returns immediately. Never silently swallow code results.

---

## 3. Advanced Telematics & Automotive IoT Firmware Standards

For fleet management, GPS tracking, and telemetry solutions (such as iNAV platforms):

*   **Zero-Allocation NMEA & Binary GPS Parsing:**
    *   Never use string parsing functions that allocate memory on the heap. Use pointer offsets and `sscanf` for ASCII sentences.
    *   For binary GPS protocols (e.g., UBX, Concox/Jimi protocol frames), cast read buffers to packed structures after verifying header synchronization bytes and CRC checksums.
*   **Moving Average Fuel Level Calibration:**
    *   Capacitive fuel sensor data is highly noisy due to vehicle motion. Apply an **Exponentially Weighted Moving Average (EWMA)** filter to raw analog/RS485 reads:
        ```c
        typedef struct {
            float alpha; // Weighting factor (0.0 < alpha < 1.0)
            float filteredValue;
            bool isInitialized;
        } ewma_filter_t;

        static inline float ewma_filter(ewma_filter_t *const f, const float newValue) {
            if (!f->isInitialized) {
                f->filteredValue = newValue;
                f->isInitialized = true;
            } else {
                f->filteredValue = (f->alpha * newValue) + ((1.0f - f->alpha) * f->filteredValue);
            }
            return f->filteredValue;
        }
        ```
*   **Anti-Tamper & Battery Power Path Management:**
    *   Configure external power tracking interrupts (VBUS detect or analog voltage monitor).
    *   Upon detecting vehicle main battery disconnection:
        1. Immediately cut off power to non-critical external sensors and RFID modules.
        2. Force the cellular module to transmit a "Main Power Lost / Tampered" packet containing the last cached GPS coordinates.
        3. Drop the MCU core clock speed and enter a low-power cyclic sleep mode, waking up only to transmit periodic backup heartbeats.
*   **Telemetry Frame Packing:**
    *   Structure all telematics messages with explicit byte alignments to prevent gaps:
        ```c
        #pragma pack(push, 1)
        typedef struct {
            uint8_t startByte;
            uint8_t protocolId;
            uint32_t imeiHigh;
            uint32_t imeiLow;
            uint32_t epochTime;
            int32_t latitude;  // Scaled by 10^7
            int32_t longitude; // Scaled by 10^7
            uint8_t speedKmh;
            uint16_t statusFlags;
            uint16_t checksum;
        } telemetry_frame_t;
        #pragma pack(pop)
        ```

---

## 4. Dynamic Memory Elimination & Static C Patterns

Dynamic allocations trigger heap fragmentation. Over months of operation, this causes memory requests to fail, causing system lockups.

### Memory Pools & Stack Auditing
*   **Static Buffer Allocation:** Use static multi-dimensional arrays for block allocations:
    ```c
    #define BUFFER_POOL_SIZE 4
    #define BUFFER_MAX_LEN 128
    static uint8_t msgPool[BUFFER_POOL_SIZE][BUFFER_MAX_LEN];
    static bool msgOccupied[BUFFER_POOL_SIZE] = {false};
    ```
*   **C11 Alignment Standards:** Use `<stdalign.h>` to enforce strict alignment of static memory blocks:
    ```c
    alignas(uint32_t) static uint8_t rawBuffer[1024];
    ```

---

## 5. High-Performance Static String & Parsing Utilities

Standard library `std::string` and Arduino `String` are forbidden on hot paths. Use the following static structures and zero-allocation parsing routines instead.

### Zero-Allocation String Tokenizer
Use this to parse character buffers (like GPS NMEA sentences or AT responses) without allocating memory:
```c
// Split a character buffer by delimiter and extract a specific index field.
// Zero allocations, zero heap manipulation.
bool extract_field(const char* csv, char delimiter, size_t targetIndex, char* outBuffer, size_t outMaxLen) {
    if (!csv || !outBuffer || outMaxLen == 0) return false;
    outBuffer[0] = '\0';

    size_t currentIndex = 0;
    const char* start = csv;
    const char* end = NULL;

    while (1) {
        end = strchr(start, delimiter);
        if (currentIndex == targetIndex) {
            size_t len = end ? (size_t)(end - start) : strlen(start);
            if (len >= outMaxLen) {
                len = outMaxLen - 1;
            }
            memcpy(outBuffer, start, len);
            outBuffer[len] = '\0';
            return true;
        }
        if (!end) break;
        start = end + 1;
        currentIndex++;
    }
    return false;
}
```

---

## 6. Real-Time Concurrency & Lock-Free Design

Mutexes introduce latency and priority inversion risks. When passing data between Interrupt Service Routines (ISRs) and RTOS tasks, use lock-free data structures.

### Single-Producer Single-Consumer (SPSC) Queue in C
For serial UART buffers, CAN frame queues, or ADC samples:
```c
#define QUEUE_SIZE 64 // Must be a power of 2

typedef struct {
    uint8_t buffer[QUEUE_SIZE];
    volatile size_t writeIndex;
    volatile size_t readIndex;
} spsc_queue_t;

static inline void queue_init(spsc_queue_t *const q) {
    q->writeIndex = 0;
    q->readIndex = 0;
}

static inline bool queue_push(spsc_queue_t *const q, const uint8_t item) {
    size_t currentWrite = q->writeIndex;
    size_t currentRead = q->readIndex;
    if ((currentWrite - currentRead) == QUEUE_SIZE) return false; // Full
    
    q->buffer[currentWrite & (QUEUE_SIZE - 1)] = item;
    __sync_synchronize(); // Compiler/Hardware memory barrier
    q->writeIndex = currentWrite + 1;
    return true;
}

static inline bool queue_pop(spsc_queue_t *const q, uint8_t *const item) {
    size_t currentRead = q->readIndex;
    size_t currentWrite = q->writeIndex;
    if (currentRead == currentWrite) return false; // Empty
    
    *item = q->buffer[currentRead & (QUEUE_SIZE - 1)];
    __sync_synchronize(); // Compiler/Hardware memory barrier
    q->readIndex = currentRead + 1;
    return true;
}
```

---

## 7. Defensive Programming & State Machine Isolation

*   **Defensive Assertions in Production:**
    *   Standard `assert()` locks the CPU in an infinite loop. Always override `__assert_func` (or equivalent compiler assertion macros) to log the failing condition, file name, and line number to backup registers, shut down safety-critical actuators, and trigger a reboot:
        ```c
        void __assert_func(const char* file, int line, const char* func, const char* failedExpr) {
            save_crash_log(file, line, failedExpr);
            disable_all_actuators();
            NVIC_SystemReset(); // System Reset
        }
        ```
*   **Hierarchical State Machines (HSM):**
    *   Always model multi-step security flows (e.g., OTP Verification → Face Check → Unlock Solenoid) using strict, deterministic state transitions.
    *   Protect against illegal jumps: enforce checking the previous active state before modifying state parameters. Never allow the solenoid to fire unless the state transition matches the exact defined path.

---

## 8. HardFault Diagnostics & Exception Decoding

When a CPU crash occurs, the firmware must capture diagnostic context before resetting the hardware.

### Overriding default Fault Handlers (ARM Cortex-M Example)
Map the `HardFault_Handler` to call an assembly routine that extracts stack frames and jumps to a C diagnostic decoder:
```assembly
.global HardFault_Handler
.type HardFault_Handler, %function
HardFault_Handler:
    tst lr, #4
    ite eq
    mrseq r0, msp
    mrsne r0, psp
    ldr r1, [r0, #24]  /* Extract Program Counter (PC) from stack frame */
    ldr r2, [r0, #20]  /* Extract Link Register (LR) from stack frame */
    b decode_hard_fault
```

---

## 9. IoT-SkillsBench Platform & Framework Rules

To guarantee cross-platform compilation and physical hardware execution stability, the firmware code must strictly adhere to the following framework constraints:

### A. Zephyr RTOS Rules (Nordic nRF52840)
1.  **Devicetree Aliasing:** Never declare raw GPIO pin integers. Pins must be resolved through Devicetree overlays using aliases:
    ```c
    #define LED_NODE DT_ALIAS(status_led)
    static const struct gpio_dt_spec led = GPIO_DT_SPEC_GET(LED_NODE, gpios);
    ```
2.  **Polarity-Agnostic Gating:** Always use `gpio_pin_set_dt(&led, 1)` (logical ON) rather than raw voltage states (`gpio_pin_set(dev, pin, 1)`). Let Zephyr's driver translate the logic state according to the devicetree active-high/active-low flags.
3.  **Sensor Subsystem API:** Fetch values from I2C/SPI sensors (e.g. BME280, MPU6050) using the Zephyr Sensor driver instead of raw register writes:
    ```c
    struct sensor_value temp, humidity;
    sensor_sample_fetch(sensor_dev);
    sensor_channel_get(sensor_dev, SENSOR_CHAN_AMBIENT_TEMP, &temp);
    ```

### B. ESP-IDF Rules (Espressif ESP32-S3)
1.  **One-Shot ADC v5.x API:** Do not use deprecated legacy ADC functions. Use the thread-safe oneshot driver API:
    ```c
    adc_oneshot_unit_handle_t adc_handle;
    adc_oneshot_unit_init_cfg_t init_config = { .unit_id = ADC_UNIT_1 };
    adc_oneshot_new_unit(&init_config, &adc_handle);
    ```
2.  **LEDC PWM Gating:** Always zero-initialize the configuration structs (e.g. `ledc_timer_config_t timer_conf = {0};`) to prevent random register corruption and panics.
3.  **FreeRTOS Watchdog Management:** High-performance loops (such as cellular GPRS loops) must yield control using `vTaskDelay()` or call `esp_task_wdt_reset()` to prevent triggering the task watchdog.

### C. Arduino Rules (ATmega2560)
1.  **Hardware Serial Gating:** Banish the `SoftwareSerial` library. For high-speed telemetry outputs, utilize the secondary hardware UARTS (`Serial1`, `Serial2`, or `Serial3` pins).
2.  **Non-Blocking Wire I2C Transactions:** Banish blocking while loops waiting on `Wire.endTransmission()`. Wrap all requests with short check-counter breaks to prevent I2C bus hangs.

---

## 10. Human-Expert Peripheral Driver Matrix (The 23 Peripherals)

Every peripheral driver must follow these expert C/C++ firmware integration standards:

| # | Peripheral | Interface | Expert Code Rules & Anti-Fail Constraints |
|---|---|---|---|
| 1 | **LED** | GPIO (Digital Out) | Apply a state latch variable; never trigger writes if the target state matches the current. |
| 2 | **Push Button** | GPIO (Digital In) | Implement a non-blocking debouncer (20ms-50ms) using `millis()` state checks. |
| 3 | **Active Buzzer** | GPIO (Digital Out) | Limit activation time to a hard maximum duration to prevent coil burn. |
| 4 | **Passive Buzzer** | PWM | Configure output compare registers directly; stop the PWM timer completely when silenced. |
| 5 | **Relay Module** | GPIO (Digital Out) | Enforce a lock-out period (e.g., 500ms) between state transitions to prevent contact arcing. |
| 6 | **Laser Emitter** | GPIO (Digital Out) | Pulse the emitter at a maximum duty cycle to limit thermal breakdown. |
| 7 | **Rotary Encoder** | GPIO (Digital In) | Decode quadrature phases (A/B) inside GPIO edge interrupts; check state on transitions. |
| 8 | **16-Key Keypad** | GPIO (Digital Scan) | Scan row lines sequentially with digital outputs; read columns with internal pull-ups active. |
| 9 | **Tilt Switch** | GPIO (Digital In) | Apply a moving-average filter to tilt triggers to filter out mechanical vibration spikes. |
| 10| **Analog Joystick** | ADC (Analog) | Apply a $\pm5\%$ deadband around the center readings to prevent pointer drift. |
| 11| **Photoresistor** | ADC (Analog) | Average 10 consecutive ADC samples over 100ms; use a lookup table to estimate lux. |
| 12| **TMP36 Temp** | ADC (Analog) | Convert ADC voltage: $T = (V_{out} \text{ (mV)} - 500) / 10$. Average reads to filter noise. |
| 13| **Water Level** | ADC (Analog) | Power the sensor via a GPIO pin only during measurements to prevent probe electrolysis. |
| 14| **PIR Motion** | GPIO (Digital In) | Bind to an edge interrupt; ignore triggers for 3 seconds after an alarm to avoid bounce. |
| 15| **Ultrasonic** | Trigger / Echo GPIO | Trigger with a exact 10us HIGH pulse. Measure Echo pin high-duration using an Input Capture Timer. |
| 16| **Sound Sensor** | GPIO (Digital In) | Count pulses in a 50ms window rather than reading state to estimate sound pressure. |
| 17| **Shock Sensor** | GPIO (Digital In) | Bind to a falling-edge interrupt; set a lockout flag for 100ms after a trigger is recorded. |
| 18| **DHT11 Sensor** | 1-Wire | Implement precise microsecond timing gates for the 80us handshake and 50us bit periods. |
| 19| **DS18B20 Temp** | 1-Wire | Execute 1-Wire CRC-8 checks on the 64-bit ROM; enforce a 750ms wait for 12-bit conversions. |
| 20| **LCD1602 Display**| Parallel / I2C | Execute a 50ms wait after power-up before writing the 4-bit initialization sequence. |
| 21| **DS1307 RTC** | I2C (0x68) | Convert read bytes from Binary-Coded Decimal (BCD) to standard decimal formats on read. |
| 22| **MPU6050 Accel** | I2C (0x68) | Wake from sleep by writing 0x00 to Register 0x6B; read 14 raw registers in a single block. |
| 23| **BME280 Sensor** | I2C / SPI | Read calibration parameters from registers on boot; use double-precision math for pressure. |

---

## 11. Mandatory AI Code Generation Guidelines

When the AI agent generates C or C++ firmware code for the user, it **MUST** enforce the following constraints:

1.  **Heap Ban:** Never use `new`, `malloc`, `std::string`, `String`, or dynamic arrays in generated examples. Use `char[]` arrays, `snprintf`, and compile-time template/macro bounds.
2.  **No Blocking loops:** Ensure `loop()` or scheduling runs are cooperative and use `millis()` timing markers.
3.  **Type Safety:** Declare numeric values with explicit-width integer types (`uint16_t`, `int32_t`) from `<stdint.h>`.
4.  **Compiler Checks:** Enable all warnings (`-Wall -Wextra -Werror`).
5.  **Safe Pointers:** Never perform raw arithmetic offsets on pointers; use indexed buffers. Validate pointers against `NULL` before use.

---

## 12. The 6-Phase Embedded Programming Pipeline & Core Sub-Skills

This section documents the execution pipeline and indexes all specialized firmware and cloud-connection sub-skills.

### Phase 1: Register Initialization, Linker Scripts, & Boot Safety
*   **Active Sub-skills:**
    *   [embedded-fw-bare-metal](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/embedded-fw-bare-metal/SKILL.md) — Vector tables, BSS/DATA segment setups, and startup code.
    *   [embedded-fw-hal-abstraction](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/embedded-fw-hal-abstraction/SKILL.md) — Isolating physical pin configuration behind standard API interfaces.
    *   [embedded-fw-bootloaders](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/embedded-fw-bootloaders/SKILL.md) — Safe partition swapping, golden image fallbacks, and RSA signature verification.
    *   [iot-fw-flash-encryption](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-flash-encryption/SKILL.md) — Enabling hardware encryption keys and securing the JTAG boot security registers.
    *   [iot-sw-device-provisioning](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-device-provisioning/SKILL.md) — Injecting private client certificates and UUID parameters in factory stages.

### Phase 2: Compiler Optimization, RTOS Scheduling, & State Persistence
*   **Active Sub-skills:**
    *   [embedded-fw-compiler-tuning](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/embedded-fw-compiler-tuning/SKILL.md) — Flash size optimization (`-Os`, `-ffunction-sections`, `-fdata-sections`).
    *   [embedded-fw-rtos-scheduling](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/embedded-fw-rtos-scheduling/SKILL.md) — Queue parameters, scheduling ticks, and thread priority setups.
    *   [embedded-fw-state-persist](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/embedded-fw-state-persist/SKILL.md) — Wear-leveled parameters storage using LittleFS/SPIFFS libraries.
    *   [iot-fw-no-block-loop](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-no-block-loop/SKILL.md) — Cooperative multitasking logic without CPU stalling loops.
    *   [iot-fw-power-management](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-power-management/SKILL.md) — Sleep modes execution, RTC alarms configuration, and clock gating controls.

### Phase 3: Peripheral Drivers, Interrupt Service Routines, & Filtering
*   **Active Sub-skills:**
    *   [embedded-fw-comm-protocols](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/embedded-fw-comm-protocols/SKILL.md) — Configuring UART, SPI (DMA), and CAN baud rates.
    *   [embedded-fw-interrupt-handling](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/embedded-fw-interrupt-handling/SKILL.md) — Routing ISR execution blocks in RAM (`IRAM_ATTR`) and prioritizing interrupts.
    *   [embedded-fw-sensor-filters](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/embedded-fw-sensor-filters/SKILL.md) — Fixed-point EWMA and digital filtering for analog telemetry.
    *   [iot-fw-peripheral-drivers](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-peripheral-drivers/SKILL.md) — Low-level RS485, RFID, Modbus sensor, and MDVR serial protocols.
    *   [iot-sw-edge-analytics](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-edge-analytics/SKILL.md) — Processing GPS coordinates and sensor logs locally before server upload.
    *   [iot-sw-geolocation-tracking](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-geolocation-tracking/SKILL.md) — Cleaning GPS coordinates, tracking azimuth changes, and local geofence audits.

### Phase 4: Stability, Watchdog Resiliency, & Memory Audits
*   **Active Sub-skills:**
    *   [embedded-fw-watchdog-resilience](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/embedded-fw-watchdog-resilience/SKILL.md) — Configuring independent hardware watchdogs (IWDG) and window limits.
    *   [embedded-fw-memory-allocation](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/embedded-fw-memory-allocation/SKILL.md) — Declaring static memory buffers and avoiding dynamic heap fragmentation.
    *   [embedded-fw-low-power-states](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/embedded-fw-low-power-states/SKILL.md) — Transitioning core power domains during main voltage loss.
    *   [iot-fw-watchdog-timers](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-watchdog-timers/SKILL.md) — Feeding watchdogs across RTOS tasks.
    *   [iot-fw-connection-resilience](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-connection-resilience/SKILL.md) — Exponential backoff strategies for cellular GPRS network drops.
    *   [iot-fw-thermal-protection](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-thermal-protection/SKILL.md) — Monitoring battery temperature and disabling charging states under vehicle heat.
    *   [iot-fw-memory-safety](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-memory-safety/SKILL.md) — Safe buffer bounds and preventing pointer leaks.

### Phase 5: Simulation, Profiling, & HardFault Diagnostics
*   **Active Sub-skills:**
    *   [embedded-fw-unit-testing](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/embedded-fw-unit-testing/SKILL.md) — Using mocks (like Unity) to run tests on host developer desktops.
    *   [embedded-fw-profiling-metrics](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/embedded-fw-profiling-metrics/SKILL.md) — Measuring thread execution times with SEGGER SystemView.
    *   [embedded-fw-diagnostics-faults](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/embedded-fw-diagnostics-faults/SKILL.md) — Setting custom HardFault handlers and decoding PC/LR registers.
    *   [iot-fw-hil-simulation](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-hil-simulation/SKILL.md) — Simulating GPS NMEA feeds and cellular tower responses on test benches.
    *   [iot-fw-debugging-jtag](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-debugging-jtag/SKILL.md) — GDB debugging, hardware breakpoints, and stack tracing.
    *   [iot-fw-led-signaling](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-fw-led-signaling/SKILL.md) — Communicating states (cellular, GPS, error codes) using LED blink patterns.

### Phase 6: Cloud Connection, MQTT, & Telemetry Ingestion
*   **Active Sub-skills:**
    *   [iot-sw-mqtt-topic-design](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-mqtt-topic-design/SKILL.md) — Structured MQTT topic schemas (`boxes/{mac}/telemetry`).
    *   [iot-sw-mqtt-broker-config](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-mqtt-broker-config/SKILL.md) — SSL/TLS setup and authentication layers on the broker.
    *   [iot-sw-mtls-device-auth](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-mtls-device-auth/SKILL.md) — Mutual TLS device authentication using X.509 client certificates.
    *   [iot-sw-data-payload-protobuf](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-data-payload-protobuf/SKILL.md) — Packing payloads using Protobuf to minimize GPRS cellular data.
    *   [iot-sw-telemetry-ingestion](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-telemetry-ingestion/SKILL.md) — Structuring message queues (RabbitMQ/Kafka) to decouple GPRS decoders from databases.
    *   [iot-sw-time-series-storage](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-time-series-storage/SKILL.md) — Ingesting tracking coordinates into databases like TimescaleDB/ClickHouse.
    *   [iot-sw-realtime-telemetry-ui](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-realtime-telemetry-ui/SKILL.md) — Streaming coordinates to tracking maps via WebSockets.
    *   [iot-sw-device-twin-state](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-device-twin-state/SKILL.md) — Managing states (locking/unlocking) between cloud database and device.
    *   [iot-sw-ota-server-mgmt](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-ota-server-mgmt/SKILL.md) — Scheduling staged rollouts and managing firmware binaries.
    *   [iot-sw-rate-limiting-devices](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-rate-limiting-devices/SKILL.md) — Protecting servers from high-frequency cellular spamming.
    *   [iot-sw-anomaly-detection](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-anomaly-detection/SKILL.md) — Alerting on drops in GPS tracking updates or voltage fluctuations.
    *   [iot-sw-audit-log-actions](file:///C:/Users/Lorenzo%20Bela/.gemini/config/skills/iot-sw-audit-log-actions/SKILL.md) — Logging remote device overrides (like ignition cut-off commands) into database ledgers.
