import paho.mqtt.client as mqtt
import sqlite3
from database_manager import DB_NAME

# Configuration
BROKER = "::1" #ip address 127.0.0.1 or localhost
TOPIC = "conroe/water/pressure"

def save_to_db(topic, payload):
    """Writing the data to our permanent record."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO telemetry (topic, payload) VALUES (?, ?)", (topic, payload))
        conn.commit()
        conn.close()
        print(f"Logged to Historian: {payload} PSI")
    except Exception as e:
        print(f"Database Error: {e}")

def on_message(client, userdata, msg):
    # Convert the raw bytes from the wire into a human readable number
    val = float(msg.payload.decode())
    save_to_db(msg.topic, val)

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

print("🛰️ Subscriber active... Waiting for Grid data...")
client.connect(BROKER, 1883)
client.subscribe(TOPIC)
client.loop_forever()