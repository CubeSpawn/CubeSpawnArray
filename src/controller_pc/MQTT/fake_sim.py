import paho.mqtt.client as mqtt
import time

# MQTT Configuration
BROKER_IP = "192.168.1.50"
STATE_TOPIC = "cubespawn/state"

# Create and configure the MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(BROKER_IP, 1883, 60)

# Function to publish a fake state message
def publish_fake_state(conveyor_id, position):
    state_message = f"ST:{conveyor_id}P{position}"
    client.publish(STATE_TOPIC, state_message)
    print(f"Published fake state: {state_message}")

# Move PM-01 from P1 to P5 and back
for position in range(1, 6):
    publish_fake_state("Conveyor-01", position)
    time.sleep(3)

for position in range(4, 0, -1):
    publish_fake_state("Conveyor-01", position)
    time.sleep(3)

# Move PM-02 from P6 to P2 and back
for position in range(6, 1, -1):
    publish_fake_state("Conveyor-06", position)
    time.sleep(3)

for position in range(2, 7):
    publish_fake_state("Conveyor-06", position)
    time.sleep(3)

