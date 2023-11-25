from fastapi import FastAPI
import routes as router

import paho.mqtt.client as mqtt

# init fastapi
app = FastAPI()
app.include_router(router)


# init mqtt
client = mqtt.Client()
client.connect("localhost", 1883, 60)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("test")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client.on_connect = on_connect
client.on_message = on_message


# start mqtt loop
client.loop_start()
