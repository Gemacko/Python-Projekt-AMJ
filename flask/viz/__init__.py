from flask import Flask, render_template, flash
import datetime
from werkzeug import datastructures

UPLOAD = "C:/Users/3amer/Documents/YRGO/Git/our-project/Python-Projekt-AMJ/flask-example/viz/w.txt"



# This creates the flask application and configures it
# flask run will use this to start the application properly
app = Flask(__name__)
app.config.from_mapping(
    # This is the session key. It should be a REALLY secret key!
    SECRET_KEY="553e6c83f0958878cbee4508f3b28683165bf75a3afe249e"
)

# The mapping of units in accordance with our specification
UNITS = {
    0: "°C",
    1: "RH"
}

# This is a placeholder that returns a fixed set of meters
# in a proper system this would look in a database or in
# the file system for a list of meters in the system
def get_meters():
    meters = [ ("Första", 0),
               ("2", 1),
               ("3", 2),
               ("4", 3)]
    return meters



def read__temp():
    lista = []
   # lista = set()
    with open(UPLOAD,"r") as file:
        for lines in file:
            data = lines.split(" ")
            ratuple = tuple((data))
           
        
        
            print(ratuple)
            print(data)

        return lista


    
# This is a placeholder that returns a fixed set of 
# measurement data. In a proper system this would read
# the data from a database or the file system
def get_measurements(meter, channel):
    if (meter, int(channel)) not in get_meters():
        # the function flash() is part of the flask system and lets us
        # register error/warning messages that should be shown on the
        # web page.
        flash(f"The meter {meter} with channel {channel} does not exist.")
        return []

    # this just generates a fixed set of measurement values
    # to have something to show...
    #measurements = []
    #with open(UPLOAD,"r") as file:
     #       for line in file:
      #          data = line.split(" ")
       #         time = data[4]
        #        date = datetime.datetime.fromtimestamp(time)
         #       value = time % 27
          #      measurements.append((date, value, UNITS[0]))
           #     time = time - 10 * 60
    #return measurements

# @app.route registers a handler for a specific URL
# in this case the URL / (i.e. the root of the server)

@app.route("/")
def start_page():
    meters = get_meters()
    return render_template("start.html", meters=meters)
# using @app.route with <something> makes "something" into
# a path variable. In the case /meter/1234/channel/5678
# the meter-argument would be set to (the string!) 1234
# and channel to 5678.

@app.route("/meter/<meter>/channel/<channel>")

def show_measurements(meter, channel):
    for i in line(4):
        measurements = []
        data = []
        data = read__temp()
        
        celcius = data[4]
        
        date = data[2]
        time = [3]
        measurements.append((date, celcius, UNITS[0]))
    #measurements.append((list_3[1], list_3[3], UNITS[0]))
        meter = data[0]
        channel = data[3]
    
    return render_template("meter.html", meter=meter, channel=channel, measurements=measurements)

#def show_measurements(meter, chaS