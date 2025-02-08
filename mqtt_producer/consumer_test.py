import paho.mqtt.client as mqtt

BROKER = "mqtt.eclipseprojects.io"
PORT = 1883
TOPIC = "sensor/temperature"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Received: {msg.topic} → {msg.payload.decode()}")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()  # Keeps listening for messages
