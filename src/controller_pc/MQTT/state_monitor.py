import paho.mqtt.client as mqtt

# MQTT Configuration
BROKER_IP = "192.168.1.50"
STATE_TOPIC = "cubespawn/state"

# Callback when a message is received
def on_message(client, userdata, message):
    print(f"Received message on {STATE_TOPIC}: {message.payload.decode()}")

# Create and configure the MQTT client
client = mqtt.Client()
client.on_message = on_message

# Connect to the MQTT broker and subscribe to the state topic
client.connect(BROKER_IP, 1883, 60)
client.subscribe(STATE_TOPIC)

# Start the MQTT client loop to listen for messages
client.loop_forever()

