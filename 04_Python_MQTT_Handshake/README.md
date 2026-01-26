Session 04: Python-MQTT Handshake & Infrastructure
Project: Conroe Water Grid - IoT Integration

Objective: Establish a resilient connection between a Python-based sensor simulator and a Dockerized MQTT Broker.

Tech Stack
Language: Python 3.12+

Library: paho-mqtt (Version 2.x)

Infrastructure: Docker (Mosquitto 2.0+ Broker)

Protocol: MQTT v5.0

 Setup & Installation
1. The Broker (Docker)
Due to security updates in Mosquitto 2.0, the broker is configured to allow anonymous local connections and listen on IPv4.

Start the Broker:
docker run -d --name mosquitto -p 1883:1883 eclipse-mosquitto mosquitto -c /mosquitto/config/mosquitto.conf --allow-anonymous --listener 1883

2. The Python Environment
# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install paho-mqtt

The Handshake Logic
We utilized the Paho-MQTT Version 2.0 API. Note the mandatory reason_code parameter in the on_connect callback.

def on_connect(client, userdata, flags, reason_code, properties=None):
    if reason_code == 0:
        print("✅ SUCCESS: Connected to Conroe Grid Broker")
    else:
        print(f"❌ Connection Refused. Code: {reason_code}")

Troubleshooting (The "Senior" Log)
During development, we encountered and resolved the following "Infrastructure Friction":

------------------------------------------------------------------------------------------------------------------------------------
Error                         | Cause                         | Resolution
------------------------------------------------------------------------------------------------------------------------------------
[Errno 61] Connection refused | "Broker was in "Secure Mode"" | Added --allow-anonymous --listener 1883 to Docker start command.
------------------------------------------------------------------------------------------------------------------------------------
localhost resolution failure  | Mac IPv6/IPv4 conflict        | Switched BROKER address to 127.0.0.1.
------------------------------------------------------------------------------------------------------------------------------------
DeprecationWarning (V1)       | Outdated API signature        | Migrated to CallbackAPIVersion.VERSION2.
------------------------------------------------------------------------------------------------------------------------------------

Verification
To verify the data flow independently of the Python script, run the following command to subscribe to the stream:

docker exec -it mosquitto mosquitto_sub -t "conroe/#" -v