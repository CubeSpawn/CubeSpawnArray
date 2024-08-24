import paho.mqtt.publish as publish
MQTT_SERVER = "192.168.1.50"
MQTT_PATH = "ID_channel"
publish.single(MQTT_PATH, "Lathe", hostname=MQTT_SERVER)

