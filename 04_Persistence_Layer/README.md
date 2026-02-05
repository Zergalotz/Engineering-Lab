# Session 04: Industrial Historian & Persistence Layer

## Architectural Overview
This session implements the **Level 3 (Operations)** persistence layer for the Conroe Water Grid. By integrating a SQLite-based **Historian**, we transition the system from volatile real-time telemetry to long-term data logging and auditability.

---

## Environment & Infrastructure Setup
<details>
<summary><b>1. Docker Broker Configuration (The "Pipe")</b></summary>

Before executing telemetry scripts, the MQTT Broker must be active.

* **Start Broker:** `docker run -d --name mosquitto -p 1883:1883 eclipse-mosquitto`
* **Check Health:** `docker ps`
* **Reset Broker:** `docker rm -f mosquitto`
</details>

---

## Component Inventory
This session utilizes a decoupled three-tier script architecture:

1. **`database_manager.py` (The Librarian):** * **Role:** Initializes the SQLite schema and manages the telemetry table.
   * **Target:** `conroe_water_grid.db`
2. **`subscriber.py` (The L3 Service):** * **Role:** Bridges the gap between **Level 2 (Communication)** and **Level 3 (Persistence)**. Listens for telemetry on `conroe/water/pressure` and performs SQL inserts.
3. **`audit_historian.py` (The Auditor):** * **Role:** Provides system transparency by querying the last 10 records sorted by timestamp.

---

## Execution Workflow
To verify the system integration, execute the following steps in separate terminal instances:

### **Step 1: Initialize the Listener (Terminal 1)**
Navigate to the session directory and start the subscriber service:
`cd ./04_Persistence_Layer/`
`python3 subscriber.py`

### **Step 2: Simulate Field Telementry (Terminal 2)
Publish a manual pressure reading to the MQTT broker:
`docker exec -it mosquitto mosquitto_pub -h localhost -t conroe/water/pressure -m "95.5"`

### **Steo 3: Audit the Historian (Terminal 3)
Verify that the data was successfully persisted to the database:
`python3 audit_historian.py`

## Engineering Troubleshooting
<details> <summary><b>View Common Error Resolutions</b></summary>

Dependency Missing: No module named 'paho' -> Run pip install paho-mqtt.

Path Errors: No such file or directory -> Use pwd to ensure you are in the /04_Persistence_Layer/ directory.

Connectivity: Connection Refused -> Ensure Docker is running and the Mosquitto container is active (docker ps).

Resource Contention: If the database file is locked, ensure only one process is writing to the Historian at a time.

</details>

## Design Decision Log
Refer to the Design_Design_Log file in the session directory.
> **Decession:** Decoupled Audit Logic.
> **Why:** By separating audit_historian.py from the main subscriber.py, we ensure that data verification does not interfere with the high-frequency ingestion of telemetry.

### **Final Alignment Check**
1. **Purdue Model:** References Level 2 and Level 3 correctly.
2. **Bash Blocks:** Now use the proper triple-backtick formatting for easier copying.
3. **Step Titles:** Now stand out with bold headers.

**Does this version capture exactly what you need for your folder 04?**

