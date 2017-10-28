import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIOPIN = 24
GPIO.setup(GPIOPIN, GPIO.OUT)

try:
     for x in range(0,2):
        time.sleep(5)
        GPIO.output(GPIOPIN,GPIO.HIGH)
        print " Pin set high"
        time.sleep(5)
        GPIO.output(GPIOPIN,GPIO.LOW)
        print " Pin set low"

except KeyboardInterrupt:
    print "KeyboardInterrupt occured"finally:
    GPIO.cleanup()
