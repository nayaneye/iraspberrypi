import plotly.plotly as py
import json
import time
import datetime
import os
import glob

#START#### Temp Sensor: DS18B20 #####
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
#device_file = base_dir + '10-000800c4cEab/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        #return temp_c, temp_f
        return temp_c

#END#### Temp Sensor: DS18B20 #####


##### Read config.json #####
with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

url = py.plot([
    {
        'x': [], 'y': [], 'type': 'scatter',
        'stream': {
            'token': plotly_user_config['plotly_streaming_tokens'][0],
            'maxpoints': 200
        }
    }], filename='Raspberry Pi Streaming Temp Values')

print "View your streaming graph here: ", url

# temperature sensor middle pin connected channel 0 of mcp3008
stream = py.Stream(plotly_user_config['plotly_streaming_tokens'][0])
stream.open()

#the main sensor reading and plotting loop
while True:
    temp_C = read_temp()
    print(temp_C)

    # write the data to plotly
    stream.write({'x': datetime.datetime.now(), 'y': temp_C})

    # delay between stream posts
    time.sleep(0.25)
