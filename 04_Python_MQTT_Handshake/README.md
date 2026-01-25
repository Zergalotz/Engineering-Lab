# Session 04: Python MQTT Infrastructure Bridge

1. Objective
This sub-project implements the **Bridge Layer** for the Texas Smart Water Grid simulation. It serves as the translator between field hardware (simulated in Python) and the Enterprise Control Room (Java).

2. Technical Specifications & "Knowledge Lock"
This session moved beyond basic scripting into Industrial Protocol Reliability. Key engineering concepts implemented include:

Last Will and Testament (LWT): Configured the broker to automatically publish an OFFLINE_CRITICAL message if the Python bridge loses power or network connectivity. This ensures "Silent Failures" are detected immediately.

Message Retention: Set the retain flag on status messages. This ensures that any new service (like our future Java Backend) immediately knows the current state of the sensor upon startup without waiting for the next heart-beat.

Quality of Service (QoS 1): Implemented a two-way handshake (PUB -> PUBACK) to guarantee that critical pressure data is acknowledged by the broker at least once, even on unstable municipal networks.

JSON Serialization: Standardized telemetry data into a structured JSON envelope containing sensor_id, psi, and ISO-8601 timestamps.

3. Verification (Proof of Work)
Handshake Test: Terminal logs confirm successful CONNACK from the local Mosquitto broker.

Failure Simulation: Manually terminating the script triggers the LWT message on the subscriber client, verifying the "Dead-Man's Switch" logic.

Data Integrity: Verified that the outgoing JSON payload is valid and readable by standard industrial parsers.