import paho.mqtt.client as mqtt
import time 
import sys
import random

# The function after connected with Broker
def on_Connect(client, userdata, flags, rc):
    print ("Connected with result code " + str(rc))

# The function while publishing MQTT message
def on_Publish(client, userdata, mid):
    print("Publish OK")  

# Set up call back functions
client = mqtt.Client()
client.on_connect = on_Connect
client.on_publish = on_Publish

# Connect with Broker
client.connect("127.0.0.1", 1883, 60)

while True:
    try:
        # Produce number 0 to 99 randomly 
        data = random.randint(0, 99)
        # Publish MQTT message
        client.publish("Nkfust/Building_F/GS_Lab/Cash", int(data))
        print(data)
        time.sleep(0.5)
    except:
        print("EXIT")
        sys.exit(0)