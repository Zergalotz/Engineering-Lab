import paho.mqtt.client as mqtt
import time
import random

# Configuration
BROKER = "127.0.0.1"
PORT = 1883
TOPIC = "conroe/water/station_01/pressure"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

try:
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    print("🚀 Starting Sensor Transmission... (Ctrl+C to stop)")
    while True:
        # Simulate realistic pressure: 50.0 to 60.0 PSI
        current_psi = round(random.uniform(50.0, 60.0), 2)
        
        # Publish the data
        client.publish(TOPIC, current_psi)
        print(f"📡 [STATION 01] Sending Pressure: {current_psi} PSI")
        
        time.sleep(2) # Send every 2 seconds

except KeyboardInterrupt:
    print("\n🛑 Shutting down sensor...")
finally:
    client.loop_stop()
    client.disconnect()