import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
PIR_PIN=23
GPIOPIN = 24
GPIO.setup(GPIOPIN, GPIO.OUT)
GPIO.setup(PIR_PIN, GPIO.IN)

def switchstatus(state):
    GPIO.output(GPIOPIN,state)



try:
    print "PIR Module Test (CTRL+C to exit)"
    time.sleep(2)
    print "Ready"
    while True:
    status = GPIO.input(PIR_PIN)
        if status:
        print "Motion Detected!"
#            LoadImagefromCam()
#            tweetImage()
                print "Ready to detect another Motion"
        switchstatus(status)
    time.sleep(1)

except KeyboardInterrupt:
               print "Quit"
               GPIO.cleanup()

finally:
    GPIO.cleanup()
 
