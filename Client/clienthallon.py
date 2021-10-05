import paho.mqtt.client as mqtt
import time
import random
import struct

# initialize random number generator
random.seed()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# Create a MQTT client and register a callback
# for connect events
client = mqtt.Client()
client.on_connect = on_connect

# Connect to a broker
client.connect("192.168.43.55", port=1883, keepalive=60)

# Start a background loop that handles all
# communication with the MQTT broker
client.loop_start()

# send a random value every second
while True:
    time.sleep(0.01)
    id = 1
    rnd = 69
    print(str(rnd))
    # to pack data into a "C struct" (i.e. bytes object)
    # use the struct package. The first argument is
    # a format string describing the data format
    # and then all the data that should be packed into
    # it. In this case we have ! = network byte order
    # Q = unsigned 8 bytes, b = signed 1 byte
    data = struct.pack("!Qb", id, rnd)

    # publish the data to the topic some/topic
    # using the packed struct as payload and
    # MQTT QoS set to 1
    client.publish("some/topic", payload=data, qos=1)