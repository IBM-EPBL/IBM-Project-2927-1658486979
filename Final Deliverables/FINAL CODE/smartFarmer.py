import wiotp.sdk.device
import time
import os
import datetime
import random

myConfig = {
    "identity":{
        "orgId":"nqhzg5",
        "typeId":"Node-red",
        "deviceId":"1234"
        },
    "auth":{
        "token":"12345678"
        }
    }
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

def myCommandCallback(cmd):
    print("Message received from IBM IoT platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if(m=="motoron"):
        print("Motor is Switched on")
    elif(m=="motoroff"):
        print("Motor is Switched off")
    print(" ")
while True:
    soil=random.randint(0,100)  
    temp=random.randint(-20,125)
    hum=random.randint(0,100)
    myData={'soil_moisture':soil,'temperature':temp,'humidity':hum}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data successfully: %s", myData)
    time.sleep(2)
    client.commandCallback = myCommandCallback
client.disconnect()
