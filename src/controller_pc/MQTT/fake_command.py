import paho.mqtt.client as mqtt
import time

# MQTT Configuration
BROKER_IP = "192.168.1.50"
COMMAND_TOPIC = "cubespawn/command"  # Command topic for all conveyors

# Create and configure the MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(BROKER_IP, 1883, 60)

# Function to publish a fake command to a conveyor
def publish_fake_command(conveyor_id, position):
    command_message = f"{conveyor_id} C{position}"
    client.publish(COMMAND_TOPIC, command_message)
    print(f"Published fake command: {command_message}")

# Example usage: Move Conveyor-06 to position 5
publish_fake_command("Conveyor-06", 5)
time.sleep(2)  # Wait for a bit before sending the next command

# Example usage: Move Conveyor-05 to position 4
publish_fake_command("Conveyor-05", 4)

# You can add more commands as needed for testing

