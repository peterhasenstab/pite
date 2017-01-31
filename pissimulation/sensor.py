import json
import sys
import time
import datetime
import random
import sqlite3
#from sense_hat import SenseHat

class SenseHat():

    def __init__(self):
        self.meter_id = "x4711"
        self.timestamp = datetime.datetime
        self.gyroscope_raw = {'x':"", 'y':"", 'z':""}
        self.accelerometer_raw = {'x':"", 'y':"", 'z':""}
        self.compass_raw = {'x':"", 'y':"", 'z':""}
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def get_gyroscope_raw(self):
        self.gyroscope_raw['x'] = random.random() * 1000
        self.gyroscope_raw['y'] = random.random() * 1000
        self.gyroscope_raw['z'] = random.random() * 1000
        return self.gyroscope_raw

    def get_accelerometer_raw(self):
        self.accelerometer_raw['x'] = random.random() * 1000
        self.accelerometer_raw['y'] = random.random() * 1000
        self.accelerometer_raw['z'] = random.random() * 1000
        return self.accelerometer_raw

    def get_compass_raw(self):
        self.compass_raw['x'] = random.random() * 1000
        self.compass_raw['y'] = random.random() * 1000
        self.compass_raw['z'] = random.random() * 1000
        return self.compass_raw

    def get_temperature(self):
        self.temperature = random.random() * 1000
        return self.temperature

    def get_humidity(self):
        self.humidity = random.random() * 1000
        return self.humidity

    def get_pressure(self):
        self.pressure = random.random() * 1000
        return self.pressure

    def clear(self):
        self = {}

    def getData(self):
        self.get_accelerometer_raw()
        self.get_compass_raw()
        self.get_gyroscope_raw()
        self.get_humidity()
        self.get_pressure()
        self.get_temperature()
        return self

def save2db(aSensSet):
    # Open Connection to DB
    conn = sqlite3.connect('measurements.db')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS sensordata
             (meter_id text)''')#, gyroscope_raw text, accelerometer_raw text, compass_raw text, temperature real, humidity real, pressure real)''')

    # Insert a row of data
    aInsArg = aSensSet#str(aSensSet.meter_id)
    c.execute("INSERT INTO sensordata VALUES (?)", (aInsArg,))
    conn.commit()
    #conn.close()

newConditions = []
i=0
data=[]
mOutfilePath = '/Users/peterhasenstab/Documents/workspace/pite/pissimulation/data.txt'
with open(mOutfilePath, 'w') as outfile:
    json.dump([], outfile)

sense = SenseHat()

sense.clear()



#test#test#test#test#test

start = time.time()  
while ( i<1000000):       
    i=i+1
    condArray = sense.getData()
    save2db(("condArray"+str(i)))

end = time.time()
duration = end - start
    # Open Connection to DB
conn = sqlite3.connect('measurements.db')
c = conn.cursor()
    
for row in c.execute("SELECT * FROM sensordata"):
    print row
print(duration)