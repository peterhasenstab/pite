import requests
import os
import glob
import json
import time

class SetUpload():

    def __init__(self):
        self.url = 'http://httpbin.org/post'
        self.jsonSet = []

    def post(self, aSensorSet):
        r = requests.post(self.url, data = aSensorSet)
        #return(r.text)
        print(r.text)

    def getJsonSet(self):
        self.readFile()
        return self.jsonSet

    def readFile(self):
        files = glob.glob("./collect/*.json")
        files.sort(key=os.path.getmtime)
        first = files[len(files)-1]
        last = files[0]
        with open(first, 'r') as fp:
            self.jsonSet = json.load(fp)

        #print json.dumps(data, indent=4, sort_keys=True)

