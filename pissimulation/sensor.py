from sense_hat import SenseHat
from upload_json import SetUpload
import json
import time
import os
import glob


#test#test#test#test#test
condArray = []
i = 0
start = int(time.time()*1000000)
while i < 10:
    i = i + 1
    sense = SenseHat()
    meter_id = sense.meter_id
    timestamp = sense.timestamp
    fileName = meter_id + str(timestamp)
    condArray.append(sense.getJSONData())
    #time.sleep(1)
stop = int(time.time()*1000000)

data = condArray

inPath = './collect/'+fileName+'.json'
with open(inPath, 'w') as fp:
    json.dump(data, fp)


upload = SetUpload()

#
#upload.getJsonSet()[0] is in a bad structure
# add an iteration trough the Set of Sensor meassurements
#
if( upload.post(upload.getJsonSet()[0]) ):
    os.remove(upload.getJsonSet()[0].files[0])
