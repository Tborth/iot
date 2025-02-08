import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point
import json
from mysite.settings import influxdb_url,influxdb_username,influxdb_password,influxdb_ORG,influxdb_BUCKET,influxdb_POINT

_influxdb_client = InfluxDBClient(
            url=influxdb_url,
            username=influxdb_username,
            password=influxdb_password,
            verify_ssl=False)


def is_numeric(value):
    return isinstance(value, (int, float))

def consume_mqtt(topic,port,broker):
    print("--------------------consume----mqtt--")
    from .models import RuleModel,AlertName
    def on_connect(client, userdata, flags, rc):
        client.subscribe(topic)

    def on_message(client, userdata, msg):
        data=json.loads(msg.payload.decode())
        write_api = _influxdb_client.write_api()
        query_api = _influxdb_client.query_api()
        print("---------------data------------>>>>",data)
        #  data formate {"sensor_id": "temprature", "temprature": 20}
        sensor_id = data.pop("sensor_id")
        if sensor_id:
            all_rules=RuleModel.objects.filter(sensor_id=sensor_id).all() #all rules
            
            point = (
                Point("sensor_data")
                .tag("sensor_id", str(sensor_id))
            )
        
            for key, value in data.items():
                print("-------------key--value--",key,value)
                for rule in all_rules:

                    if rule.field_name == key:
                        match=str(value) + " "+ str(rule.condition)+" "+ str(rule.thrashold)
                        print("-----------------rull match------>>>>>",match)
                        condition= eval(match)
                        if condition:

                            if not rule.duration or  rule.duration <= 0 :
                                AlertName.objects.create(
                                    type =rule.status,
                                    rule_name=rule.rule_name,
                                    sensor_id=rule.sensor_id,
                                    content=f"Alert {rule.rule_name} thrashold reached {match}"
                                )
                            elif rule.duration > 0:
                                query= f'''from(bucket: "{influxdb_BUCKET}")
                                        |> range(start: -{rule.duration})
                                        |> filter(fn: (r) => r["_field"] == "{key}")
                                        |> filter(fn: (r) => r["_measurement"] == "{influxdb_POINT}")
                                        |> group(columns: ["_field", "_measurement", "sensor_id"])
                                        '''
                                
                                print("------------query--------->>>>>>>",query)
                                result = query_api.query(query,org=influxdb_ORG)
                                print("------------result------->>>>>",result)
                                found =False
                                for table in result:
                                    for record in table.records:
                                        print("--------------record--->>>",record)
                    
                                        if record.get_field() == key:
                                            value1=record.get_value()
                                            match=str(value) + " "+ str(rule.condition)+" "+ str(rule.thrashold)
                                            condition= eval(match)
                                            if condition :
                                                AlertName.objects.create(
                                                    type =rule.status,
                                                    rule_name=rule.rule_name,
                                                    sensor_id=rule.sensor_id,
                                                    content=f"Alert {rule.rule_name} thrashold reached {match}"
                                                )
                                                found=True
                                                break
                                    if found:
                                        break
             
                if is_numeric(value):
                    point.field(key, float(value))
                elif value.isalnum():
                    point.field(key, str(value))
                else:
                    point.field(key, value)
           
            write_api.write(bucket=influxdb_BUCKET, org=influxdb_ORG, record=point)


    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port, 60)
    client.loop_forever()