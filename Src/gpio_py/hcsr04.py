import RPi.GPIO as GPIO
import time

# Default pin allocations
TRIG = 2
ECHO = 3

#Function block to measure Distance
def get_distance(trigger_pin = TRIG, echo_pin = ECHO):

    GPIO.setwarnings(False)

    # Use BCM Mode for pin numbering
    GPIO.setmode(GPIO.BCM)

    #Set Trigger pin as output and echo pin as input
    GPIO.setup(trigger_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)

    print ("Using BCM Mode, Trigger on GPIO {0} and  Echo on GPIO {1}".format(trigger_pin, echo_pin))

    # Stop transmission already going on, if any
    GPIO.output(trigger_pin, False)
    print ("Waiting For Sensor To Settle")
    time.sleep(2)

    # 10 usec high-going pulse on trigger pin
    GPIO.output(trigger_pin, True)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)

    # Wait till echo pin goes high
    while GPIO.input(echo_pin)==0:
        pulse_start = time.time()

    # Now wait for the high period to be over i.e. till echo pin goes low
    while GPIO.input(echo_pin)==1:
        pulse_end = time.time()

    # Pulse width in seconds
    pulse_duration = pulse_end - pulse_start

    # Consider velocity 343m/sec
    # Distance = velocity * time
    # Time measured here is two way - Transmit and recieve
    # So Distance = velocity * (Time /2)
    # With the velocity in cm, the formula becomes
    # Distance = 34300 * (time / 2) = 17150 * time
    distance = pulse_duration * 17150

    distance = round(distance, 2)

    return distance

def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":

    print ("Distance Measurement In Progress")
    print ("Distance: {0} cm".format(get_distance(TRIG, ECHO)))
    cleanup()
