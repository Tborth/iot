Django App: Rule-Based Alerts with MQTT and InfluxDB

Overview

This Django application is designed to:

Define rules and alerts.

Consume messages from an MQTT broker.

Store data in InfluxDB.

Trigger alerts based on predefined rules.

Features

Rule Management: Users can create, update, and delete rules.

MQTT Integration: Subscribes to topics and processes incoming messages.

InfluxDB Storage: Stores sensor data and logs.

Alert System: Triggers alerts when conditions in rules are met.

Technology Stack

Backend: Django

Messaging: MQTT (via paho-mqtt)

Database: InfluxDB (via influxdb-client)

Caching: Redis (optional, for performance optimization)

#TODO Task Scheduling: Celery (optional, for background processing)



Installation & Setup

1. Clone the Repository

git clone https://github.com/your-repo/django-mqtt-influx.git
cd django-mqtt-influx

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Dependencies

pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file and add:

MQTT_BROKER_URL=mqtt.example.com
MQTT_BROKER_PORT=1883
MQTT_TOPIC=sensor/data
INFLUXDB_URL=http://localhost:8086
INFLUXDB_TOKEN=your-token
INFLUXDB_ORG=your-org
INFLUXDB_BUCKET=your-bucket

5. Run Migrations

python manage.py migrate
