import json


with open('data/buslist.json') as file_object:
    bus_info = json.load(file_object)
    #print(bus_info)
    #print(f"bus list {bus_info['buslist']}")
    for bus in bus_info['buslist']:
        print(f"source = {bus['source']}, destination = {bus['destination']} ")