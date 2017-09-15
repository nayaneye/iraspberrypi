import sys
sys.path.append('../../')

import time
import requests # This must be installed with pip install requests (or pip3 for python 3)
from devices.distancesensors import hcsr04

Dweet_Thing_Name = "RaspiDweets"

Dweet_Base_URL = "https://dweet.io/dweet/for/"
Dweet_For_URL = Dweet_Base_URL + Dweet_Thing_Name + "?"
Dweet_Follow_URL = "https://dweet.io/follow/"

dweet_data = {'Name': 'Sensors'}

def send_dweet(data = dweet_data, thing_name = Dweet_Thing_Name):

    if Dweet_Thing_Name == "":
        print ("Error: Thing name not defined. Use some random name for your Thing")
        sys.exit(0)

    r = requests.post(Dweet_For_URL, data=dweet_data)
    return r


if __name__ == "__main__":
    try:
        print ("Dweeting various sensor readings")

        while True:
            distance = hcsr04.get_distance()
            print ("Distance is {0} cm".format(distance))
            dweet_data.update({'Distance': distance})

            dweet_response = send_dweet(Dweet_Thing_Name, dweet_data)
            if (dweet_response.status_code == requests.codes.ok):
                print ("Dweet successful. Please check {0}{1}".format(Dweet_Follow_URL, Dweet_Thing_Name))
            else:
                print ("Dweet failed, please check your data")
            time.sleep(1)
    except KeyboardInterrupt:
        hcsr04.cleanup()
        print ("Done")
