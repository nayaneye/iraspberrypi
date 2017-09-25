# Instructions:
# Create login on pubnub.com
# Copy the publish and subscribe keys from the demo project.
# Replace the keys in this code (demo and demo) with your keys

# On Raspberry Pi terminal - sudo pip install pubnub
# Execute this file (with your keys) - A message will be published and the same terminal will also show the message as received.
# You can use this same file on another raspberry pi or your computer and execute the file on both of them to exchange messages

import json, re


from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
 
import RPi.GPIO as GPIO
import time
import sys

pnconfig = PNConfiguration()
 

pnconfig.subscribe_key = 'sub-c-74c2a3a2-9b76-11e7-bec3-c65ebd354f7d'
pnconfig.publish_key = 'pub-c-73a9c60e-26a6-4e5e-a92a-858d0a7247e2'


pubnub = PubNub(pnconfig)


GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False) 
LED_PIN = 20

GPIO.setup(LED_PIN,GPIO.OUT) 


channel = 'Channel-rqbvqvvdo'

 
def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        print ("Message published\n")
        #pass  # Message successfully published to specified channel.
    else:
        print "Message publish failed" 
        #pass  # Handle message publish error. Check 'category' property to find out possible issue
        # because of which request did fail.
        # Request can be resent using: [status retry];
 
 
class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass  # handle incoming presence data
 
    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            pass  # This event happens when radio / connectivity is lost
 
        elif status.category == PNStatusCategory.PNConnectedCategory:
            # Connect event. You can do stufrf like publish, and know you'll get it.
            # Or just use the connected event to confirm you are subscribed for
            # UI / internal notifications, etc
            print "Connected"
            pubnub.publish().channel(channel).message({'led':0}).async(my_publish_callback)
        elif status.category == PNStatusCategory.PNReconnectedCategory:
            pass
            # Happens as part of our regular operation. This event happens when
            # radio / connectivity is lost, then regained.
        elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
            pass
            # Handle message decryption error. Probably client configured to
            # encrypt messages and on live data feed it received plain text.
 
    def message(self, pubnub, message):
        v = json.dumps(message.message)
        v=json.loads(v)
        #json_line = json.dump(json.loads(v))
        print v['led']#type(v)
        
        #cmd = v['led']
        #print cmd
        if v['led'] == 1 :
            for i in range(6):
	        GPIO.output(LED_PIN,True)
	        time.sleep(0.5)
	        GPIO.output(LED_PIN,False)
	        time.sleep(0.5)
		print('blink')
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels(channel).execute()

#pubnub.publish().channel('awesomeChannel').message(['hello', 'there']).async(publish_callback)
