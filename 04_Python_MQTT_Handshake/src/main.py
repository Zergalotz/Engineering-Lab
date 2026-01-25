import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
import time
import json
from datetime import datetime



# --- CONFIGURATION (The "Blueprints") ---
BROKER = "localhost"  # You'll run Mosquitto in Docker later
PORT = 1883
CLIENT_ID = "Conroe_Water_Bridge_01"
STATUS_TOPIC = "conroe/water/bridge/status"
DATA_TOPIC = "conroe/water/bridge/telemetry"
is_connected = False 

# --- CALLBACKS (The "Intelligence") ---
def on_connect(client, userdata, flags, rc):
    """Called when the broker responds to our connection request."""
    global is_connected
    if rc == 0:
        is_connected = True
        print(f"✅ SUCCESS: Connected to {BROKER}")
        # When we connect, tell everyone we are ONLINE
        # QoS 1 ensures this status definitely arrives
        # retain=True ensures new subscribers see we are ONLINE immediately
        client.publish(STATUS_TOPIC, "ONLINE", qos=1, retain=True)
    else:
        is_connected = False
        print(f"❌ ERROR: Connection failed with code {rc}")

def on_disconnect(client, userdata, rc):
    global is_connected
    is_connected = False
    """Called when the script is manually or accidentally disconnected."""
    print("⚠️ Disconnected from Broker.")

# --- INITIALIZATION (The "Engine") ---
client = mqtt.Client(CallbackAPIVersion.VERSION1, CLIENT_ID)

# 1. SET THE LAST WILL AND TESTAMENT (LWT)
# This must be done BEFORE connecting. 
# If the script "dies" unexpectedly, the broker will publish this for us.
client.will_set(STATUS_TOPIC, payload="OFFLINE_CRITICAL", qos=1, retain=True)

# 2. ATTACH CALLBACKS
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# 3. START THE CONNECTION
print(f"Connecting to broker at {BROKER}...")
try:
    client.connect(BROKER, PORT, keepalive=60)
    
except Exception as e:
    print(f"could not connect: {e}")

# 4. THE NETWORK LOOP
# loop_start() runs in a background thread so we can do other things in the main thread
client.loop_start()

try:
    while True:
        if is_connected:
            # Simulate a simple data packet
            payload = {
                "timestamp": datetime.now().isoformat(),
                "sensor": "PS-CONROE-001",
                "pressure_psi": 55.4,
                "status": "HEALTHY"
            }
            
            # Publish telemetry at QoS 1 (At Least Once delivery)
            client.publish(DATA_TOPIC, json.dumps(payload), qos=1)
            print(f"📡 Telemetry Sent: {payload['pressure_psi']} PSI")
            
            time.sleep(10)  # Wait 10 seconds before next pulse

except KeyboardInterrupt:
    print("\n🛑 Shutting down gracefully...")
    # Clean disconnect (LWT will NOT be sent because we are leaving politely)
    client