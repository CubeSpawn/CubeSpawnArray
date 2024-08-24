import paho.mqtt.client as mqtt
import time

# MQTT Broker details
BROKER_IP = "192.168.1.50"
CMD_TOPIC = "cubespawn/command"
STATE_TOPIC = "cubespawn/state"

#print("Controller script started...")

# Initial state and position tracking
conveyor_positions = {
    "Conveyor-01": 1,  # Initial position for Conveyor-01
    "Conveyor-06": 6   # Initial position for Conveyor-06
}

conveyor_states = {
    "Conveyor-01": "stopped",
    "Conveyor-06": "stopped"
}

# MQTT callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe(CMD_TOPIC)

def on_message(client, userdata, msg):
    global conveyor_positions, conveyor_states
    message_payload = msg.payload.decode()
    print(f"Received message: {message_payload}")  # Log incoming state messages

    # Parse the state message
    if message_payload.startswith("ST:"):
        parts = message_payload.split(":")
        conveyor_id = parts[1][:10]
        state_info = parts[1][10:]

        if state_info.startswith("S"):
            position = int(state_info[1:])
            conveyor_positions[conveyor_id] = position
            conveyor_states[conveyor_id] = "stopped"
            print(f"Updated {conveyor_id} position to {position}")
        elif "moving" in state_info:
            conveyor_states[conveyor_id] = state_info
            print(f"{conveyor_id} is moving: {state_info}")
def check_for_collision(pm_id, target_position):
    global conveyor_positions
    if pm_id == "PM-01":
        if conveyor_positions["Conveyor-06"] < target_position:
            return False
    elif pm_id == "PM-02":
        if conveyor_positions["Conveyor-01"] > target_position:
            return False
    return True

def send_command(client, pm_id, target_position):
    global conveyor_positions, conveyor_states

    if pm_id == "PM-01":
        conveyor_id = "Conveyor-01"
    elif pm_id == "PM-02":
        conveyor_id = "Conveyor-06"
    else:
        print("Invalid PM ID")
        return

    if not check_for_collision(pm_id, target_position):
        print(f"Collision detected for {pm_id} moving to {target_position}. Command not sent.")
        return

    # Create the command and publish it
    command = f"{conveyor_id} C{target_position}"
    client.publish(CMD_TOPIC, command)
    print(f"Command sent: {command}")

# Main loop
def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_IP, 1883, 60)

    # Start the MQTT client loop
    client.loop_start()

    try:
        while True:
            # Example: PM-02 move to Conveyor-04
            command = input("Enter command (e.g., PM-02 C4): ")
            pm_id, target = command.split()
            target_position = int(target[1:])

            send_command(client, pm_id, target_position)

            # Short delay to process commands
            time.sleep(1)

    except KeyboardInterrupt:
        print("Controller stopped by user.")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()

