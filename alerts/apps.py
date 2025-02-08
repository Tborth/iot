from django.apps import AppConfig
import threading
from .utility import consume_mqtt
from mysite.settings import MQTT_BROKER,MQTT_PORT,MQTT_TOPIC

import os
from django.core.signals import request_started
from django.dispatch import receiver



class AlertsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alerts'

   
    def ready(self):
        if os.environ.get('RUN_MAIN') != 'true':  # Prevent duplicate execution
            return  
        print("----------connection rady---")
        # Start Kafka consumer thread
        thread = threading.Thread(target=consume_mqtt,args = (MQTT_TOPIC,MQTT_PORT,MQTT_BROKER), daemon=True)
        thread.start()
        # consume_messages(KAKFA_BROKER,KAFKA_TOPIC,KAFKA_GROUP_ID)

 