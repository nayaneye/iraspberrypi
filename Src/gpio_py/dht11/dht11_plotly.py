## Plotly Example of basic temperature sensor ##
## iRaspberrypi

#Import required modules
import plotly.plotly as myplot
import RPi.GPIO as GPIO
import json
import time
import datetime
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=14)


##### Read config.json #####
with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

myplot.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

url = myplot.plot([
    {
        'x': [], 'y': [], 'type': 'scatter',
        'stream': {
            'token': plotly_user_config['plotly_streaming_tokens'][0],
            'maxpoints': 200
        }
    }], filename='Raspberry Pi Streaming Temp Values')

print "View your streaming graph here: ", url

# open stream to write sensor values to given streaming token.
stream = myplot.Stream(plotly_user_config['plotly_streaming_tokens'][0])
stream.open()

#the main sensor reading and plotting loop
while True:
    result = instance.read()
    temp_C = result.temperature
    print(temp_C)

    # write the data to plotly
    stream.write({'x': datetime.datetime.now(), 'y': temp_C})

    # delay between stream posts
    time.sleep(1)
