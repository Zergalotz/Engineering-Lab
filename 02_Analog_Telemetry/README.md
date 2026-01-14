IoT Tank Level Simulator (Arduino Uno)
Date: January 2, 2026 Tech Stack: Arduino Uno R3, C++, PlatformIO, VS Code

Project Goal
To bridge the digital and physical worlds by simulating an industrial tank monitoring system. The project uses a potentiometer to mimic tank levels and triggers safety logic based on real-time telemetry.

<details> <summary><b>Hardware Configuration</b></summary>

Components
Microcontroller: Arduino Uno R3

Input: 10k Potentiometer (Dial)

Prototyping: 830 Tie-Point Breadboard

Power Source: MacBook via USB

Wiring Logic
VCC: 5V Pin on Uno to Breadboard Positive Rail

GND: Ground Pin on Uno to Breadboard Negative Rail

Signal: Potentiometer Center Pin to Analog Pin A0

Design Note: The potentiometer is positioned to "center straddle" the breadboard ravine to allow access to jumper pins on both sides.

Caution: > Short Circuit Prevention: Ensure GND and 5V jumpers never touch. Always verify wiring before connecting the USB power source.

</details>

<details> <summary><b>Software and Logic</b></summary>

Development Environment
IDE: VS Code with PlatformIO and C/C++ Extensions

Framework: Arduino / C++

Industrial Safety Logic
The void loop() monitors the analog signal and categorizes the tank state:

Critical High (>90%): Triggers "ALARM: CRITICAL HIGH LEVEL [!]"

Low Feed (<10%): Triggers "ALARM: LOW FEED DETECTED [!]"

Safe Zone: Prints "System Nominal"

</details>

<details> <summary><b>Deployment and Execution</b></summary>

Build: Click the Checkmark icon in PlatformIO to compile.

Upload: Click the Right Arrow (->) icon to flash the code to the Uno.

Monitor: Open the Serial Monitor (Plug icon) to view real-time telemetry.

Shutdown: Unplug the USB cable to power down. Always clear the breadboard and organize components after use.

</details>

<details> <summary><b>Learning Reflections and Troubleshooting</b></summary>

Key Takeaways
Breadboard Architecture: Refined the "ravine straddling" technique for large components to keep pins accessible.

Pin Mapping: Mastered Uno R3 pinout (GND, 5V, A0) and mapped them to physical breadboard rails.

IIoT Foundations: Understanding basic circuit safety and telemetry logic is the precursor to advanced concepts like MQTT and networked sensors.

Troubleshooting
Initial Setup: Reviewed breadboard continuity to ensure the potentiometer was receiving power across the bridge.

Direct Connection: Opted for a direct breadboard-to-Uno map for this session; future sessions will incorporate power distribution rails for multi-component support.

</details>