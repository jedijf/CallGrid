#CAll grid grabber

#!/usr/bin/python3


import requests
import json

callsign = ""



callsign = input("Enter Callsign: <enter> to QUIT  >> ")

while len(callsign) is true:
    
    if callsign == "q" :
        break

    else:
        try:
            api_url = f"https://callook.info/{callsign}/json"
            response = requests.get(api_url)
            location = response.json()["location"]
            grid = location["gridsquare"]
            print (f"{callsign} GRID is {grid}")
            
        except:
            print (f"CALLSIGN {callsign} INVALID  <q> to QUIT")
