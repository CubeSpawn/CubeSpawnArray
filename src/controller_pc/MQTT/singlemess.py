import paho.mqtt.client as mqtt

broker_ip = "192.168.1.50"
command_topic = "cubespawn/command"

client = mqtt.Client()

client.connect(broker_ip)

# Publish a test message
client.publish(command_topic, "Conveyor-01 C2")
print(f"Published 'Conveyor-01 C2' to {command_topic}")

client.disconnect()
