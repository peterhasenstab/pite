
import json
import sys
import time
import random
import sqlite3
#from sense_hat import SenseHat

class SenseHat():

    def __init__(self):
        self.meter_id = "x4711"
        self.timestamp = time.time()*1000000
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

    def get_data(self):
        self.get_accelerometer_raw()
        self.get_compass_raw()
        self.get_gyroscope_raw()
        self.get_humidity()
        self.get_pressure()
        self.get_temperature()
        return self

    def get_JSON_data(self):
        return self.get_data().__dict__