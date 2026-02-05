# Engineering-Lab: Industrial Systems & Infrastructure Workshop

## Executive Summary
This repository is a **Centralized Engineering Laboratory** focused on the design, integration, and scaling of **Industrial IoT (IIoT)** and **Critical Infrastructure** systems. It documents my transition from traditional software development to **Full-Stack Systems Engineering**, specializing in the bridge between Level 0 (Physical Hardware) and Level 5 (Cloud/Enterprise).

While I an still keeping the skills I acquired in the traditional Web/App roles of software engineering I am just creating my specialization. Refer to previous paragraph.

This lab serves as a chronological record of architectural decisions, emphasizing **system reliability, data integrity, and the Purdue Model of Industrial Control.**

---

## Technical Stack & Architectural Standards
<details>
<summary><b>View Engineering Domain Expertise (Click to expand)</b></summary>

### **Languages & Frameworks**
* **Embedded:** C++, Arduino/C (Low-level register manipulation & non-blocking logic).
* **System Logic:** Python (Edge Gateways, Telemetry Processing, Async IO).
* **Enterprise:** Java (OOP Architecture, Middleware, Persistence Layers).

### **Infrastructure & Protocols**
* **Connectivity:** MQTT (Pub/Sub), REST APIs, Modbus.
* **Persistence:** SQL Historians (SQLite/PostgreSQL), Time-series Data Management.
* **DevOps:** Docker (Containerization), PlatformIO, Git (CI/CD Ready).

### **Methodologies**
* **Architecture:** Purdue Model (Levels 0-3), Singleton Patterns, Composition over Inheritance.
* **Standards:** Defensive programming, non-blocking I/O, and decoupled system design.
</details>

---

## Project Evolution (Field Sessions)
Each session is treated as a "System Module," containing isolated logic, documentation, and hardware schematics. 

| Session | Title                                           | Level (Purdue) | Key Engineering Objective                                              | Status          |
| :------ | :---------------------------------------------- | :------------- | :--------------------------------------------------------------------- | :-------------- |
| **01**  | [Internal Blink](./01_Internal_Blink)           | L0/L1          | Digital Logic & Precision Clock Signaling                              | ✅ Complete     |
| **02**  | [Analog Telemetry](./02_Analog_Telemetry)       | L1             | ADC Mapping, Signal Processing, & Warning Thresholds                   | ✅ Complete     |
| **03**  | [MQTT Handshake](./03_Python_MQTT_Handshake)    | L2             | **Edge Gateway:** Decoupled Pub/Sub & QoS Reliability                  | ✅ Complete     |
| **04**  | [Industrial Historian](./04_Persistence_Layer)  | L3             | **Data Integrity:** Implementing an Asynchronous SQL Persistence Layer | 🔄 In-Progress  |
| **05**  | [Planning & Design](./05_Planning)              | N/A            | Defining System Requirements & Architectural Roadmap                   | 📅 Upcoming     |

---

## Design Philosophy
* **The "Why" Before the "How":** Every session includes a **Design Decision Log (DDL)** to document the patterns (Singleton, Adapter, etc.) used to solve specific integration pains.
* **Fault Isolation:** Using **Composition over Inheritance** to ensure that sensor failures do not cascade into system-wide crashes.
* **Production Readiness:** Code is written to be **portable** (Docker-ready) and **documented** (Accordion-style) for rapid hand-off to cross-functional engineering teams.

---
## Learning Notes Log (Knowledge Gather and Application)
> **learning_notes.txt** There will be references that ties to the code files. This is to keep the code clean of indepth comments but provides a file where you can do into descriptive details.
> **REF#** Which session that is being worked on.
> **DATE** In order to track when it was learned.
> **Format of Reference** REF# 01 [01/03/26 - 6:46 PM CST] a brief comment

## Design Decision Log (Latest Entry)
> **ID:** `DEC-002: Accordion Documentation Strategy`
> **The Pain:** Recruiters need speed; Hiring Managers need depth.
> **The Why:** Implemented `<details>` tags to provide a "Scalable" reading experience—enabling quick scanning without losing technical rigor.

---
> **"Engineering is the art of managing complexity through resilient architecture."**
> — *Systems Integration & Infrastructure Engineer*