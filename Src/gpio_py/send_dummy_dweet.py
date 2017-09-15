import random
import time
import requests # This must be installed with pip install requests (or pip3 for python 3)

Dweet_Thing_Name = "DummyDweets"

Dweet_Base_URL = "https://dweet.io/dweet/for/"
Dweet_For_URL = Dweet_Base_URL + Dweet_Thing_Name + "?"
Dweet_Follow_URL = "https://dweet.io/follow/"

dweet_data = {'Name': 'Dummy Data Dweets from Raspberry Pi'}

def send_dweet(data = dweet_data, thing_name = Dweet_Thing_Name):

    if Dweet_Thing_Name == "":
        print ("Error: Thing name not defined. Use some random name for your Thing")
        sys.exit(0)

    r = requests.post(Dweet_For_URL, data=dweet_data)
    return r

trinity_lat = 12.972623
trinity_long = 77.618152

mgroad_lat = 12.976230
mgroad_long = 77.602928

map_movement_lat = [trinity_lat, mgroad_lat]
map_movement_long = [trinity_long, mgroad_long]

# img_url = "https://thumbs.dreamstime.com/z/aircraft-dashboard-view-inside-pilot-s-cabin-42906072.jpg"
img_url = "http://cdn.playbuzz.com/cdn/a123d728-dd6e-46b1-85c2-5907d9fbb488/3e33a68c-a6a8-46e0-81d8-229bd2490032.jpg"

if __name__ == "__main__":
    try:
        print ("Dweeting dummy data")

        map_position = 0
        angle_counter = 0
        while True:
            x = random.randint(0,126)
            y = random.randint(100,251)
            z = angle_counter
            angle_counter = angle_counter + 3
            if (angle_counter == 359):
                angle_counter = 0

            dweet_data.update({'Random_x': x})
            dweet_data.update({'Random_y': y})
            dweet_data.update({'Random_z': z})

            dweet_data.update({'Latitude': map_movement_lat[map_position]})
            dweet_data.update({'Longitude': map_movement_long[map_position]})
            map_position = map_position + 1
            if (map_position == len(map_movement_lat)):
                map_position = 0

            dweet_data.update({'Image': img_url})

            dweet_response = send_dweet(Dweet_Thing_Name, dweet_data)
            if (dweet_response.status_code == requests.codes.ok):
                print ("Dweet successful. Please check {0}{1}".format(Dweet_Follow_URL, Dweet_Thing_Name))
            else:
                print ("Dweet failed, please check your data")
            time.sleep(1)
    except KeyboardInterrupt:
        print ("Done")
