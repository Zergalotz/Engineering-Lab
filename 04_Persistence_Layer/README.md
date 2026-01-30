# 04_Persistence_Layer Session

CONROE WATER GRID: SESSION 5 MASTER BLUEPRINT
1. THE ENVIRONMENT SETUP
Before running any code, ensure the "Pipe" (Broker) is open.

Start Broker: docker run -d --name mosquitto -p 1883:1883 eclipse-mosquitto

Check Health: docker ps

Reset Broker (If it's acting up): docker rm -f mosquitto

2. THE COMPONENT SCRIPTS
Make sure these 3 files are in: /Users/ghastlymac/.../04_Persistence_Layer/

File A: database_manager.py (The Librarian)
Function: Creates the SQLite database file and the telemetry table.

Variable to Check: DB_NAME = "conroe_water_grid.db"

File B: subscriber.py (The Service)
Function: Listens to MQTT and writes data to the Database.

Critical Config:

BROKER = "localhost" (Try "127.0.0.1" if "localhost" fails)

TOPIC = "conroe/water/pressure"

Must have client.loop_forever() at the bottom.

File C: audit_historian.py (The Auditor)
Function: Reads the database file and prints the results to your screen.

Logic: SELECT * FROM telemetry ORDER BY timestamp DESC LIMIT 10

3. THE EXECUTION WORKFLOW
Open three terminal windows/tabs and follow this order:

STEP 1: NAVIGATE (Do this in all 3 terminals)
cd ./Engineering-Lab/04_Persistence_Layer/
# I removed my computers full path for privacy reasons...

STEP 2: THE LISTENER (Terminal 1)
python3 subscriber.py
# Leave this running. It should say "Subscriber active..."

STEP 3: THE PUBLISHER (Terminal 2)
docker exec -it mosquitto mosquitto_pub -h localhost -t conroe/water/pressure -m "95.5"
# Check Terminal 1 to see if "Logged to Historian" appears.

STEP 4: THE AUDITOR (Terminal 3)
python3 audit_historian.py
# This should print the rows showing your 95.5 PSI entry.

4. QUICK TROUBLESHOOTING CHECKLIST
"No module named 'paho'": Run pip install paho-mqtt.

"No such file or directory": Ensure your terminal is in the 04_Persistence_Layer folder.

"Connection Refused": Check if Docker is running (docker ps).

Typo Check: Ensure it is database_manager.py and not database_manger.py.