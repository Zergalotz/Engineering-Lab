# Session 04: Python MQTT Infrastructure Bridge

## Overview
This sub-project implements the **Bridge Layer** for the Texas Smart Water Grid simulation. It serves as the translator between field hardware (simulated in Python) and the Enterprise Control Room (Java).

## System Architecture


- **Role:** Data Producer / Protocol Bridge
- **Protocol:** MQTT 5.0
- **Safety Level:** Fail-Safe Enabled (LWT)

## Technical Objectives
* **Persistent Handshaking:** Establish a resilient connection to the Mosquitto Broker.
* **Asynchronous Telemetry:** Non-blocking sensor polling using `paho-mqtt` loop structures.
* **Reliability (QoS 1):** Guaranteed delivery for critical pressure threshold alerts.
* **Infrastructure Awareness:** Implementing 'Last Will and Testament' to detect hardware brownouts.

## Setup & Virtual Environment
This project uses a local `.venv` to isolate industrial dependencies.

```bash
# Initialize and activate the "Workstation"
python3 -m venv .venv
source .venv/bin/activate

# Install the Handshake Tooling
pip install paho-mqtt