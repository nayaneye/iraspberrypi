import RPi.GPIO as GPIO
import dht11
import time
import datetime

import os
import time
import sys
from pubnub import Pubnub

pubnub = Pubnub(publish_key='demo',
			 subscribe_key='demo')


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=4)

def getTempHumidity():
	result = instance.read()
	if result.is_valid():
		return result.temperature , result.humidity
	
	return -1,-1
def callback(message):
	print(message)


while True:
    t , h = getTempHumidity()

    if ( t != -1 ):
    	print ( " temperature = %d \n " % t )
    	print ( " humidity = %d \n " % h )
	print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t, h)
    	pubnub.publish('tempeon', {
        	'columns': [
            	'x': time.time(),
            	'temperature_celcius': t
            	]

        	})
    	pubnub.publish('humeon', {
        	'columns': [
            	['humidity', h]
            	]

        	})

    time.sleep(1)
