import paho.mqtt.client as mqtt

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

# Example usage: Publish a fake state message
publish_fake_state("Conveyor-05", 5)  # PM-02 moved to position 5
publish_fake_state("Conveyor-01", 2)  # PM-01 moved to position 2

