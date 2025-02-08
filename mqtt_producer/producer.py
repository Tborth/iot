import paho.mqtt.client as mqtt
import time

BROKER = "mqtt.eclipseprojects.io"  # Free public broker
PORT = 1883
TOPIC = "sensor/temperature"

client = mqtt.Client()

client.connect(BROKER, PORT, 60)
import json
for i in range(5):  # Send 5 messages
    message = {'sensor_id':'temperature','temperature':27 + i}
    message=json.dumps(message)
    client.publish(TOPIC, message)
    print(f"Published: {message}")
    time.sleep(2)  # Delay for 2 seconds

client.disconnect()
