import paho.mqtt.client as mqtt

MQTT_SERVER = "localhost"
MQTT_PATH = "ID_channel"

# The callback for when the client receives a connect response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_PATH)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # Decode the payload from bytes to string
    message = msg.payload.decode('utf-8')
    print(f"{msg.topic} {message}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()

