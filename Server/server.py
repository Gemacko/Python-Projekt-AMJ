import paho.mqtt.client as mqtt
import struct

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("some/topic", qos=1)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # if we subscribe to more than one topic we need
    # to check which topic sent this message
    if msg.topic == "some/topic":
        # By using unpack with the same format as we used for pack
        # we will get a tuple back with our data
        from time import gmtime, strftime
        (SensorID, temp, tid, index) = struct.unpack("!bqqq", msg.payload)
        print(f"Sensor {SensorID:#} \nTemperature {temp /1000 } C \nindex {index} \ntime {tid}")
        resultwr = (f"Sensor {SensorID:#} \nTemperature {temp /1000 } C \nindex {index} \ntime {tid}")
        #print (strftime("Time: %Y-%m-%d %H:%M:%S", gmtime()))
        print ("\n")

        lines = [resultwr]

    with open('temp.csv', 'a') as f:
        for line in lines:
            f.write(line)
            f.write('\n')


# Create a MQTT client with callbacks for
# connecting to the MQTT server and receiving data
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", port=1883, keepalive=60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
client.loop_forever()