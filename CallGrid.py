#CAll grid grabber

#!/usr/bin/env python3


import requests
import json

callsign = ""

while 1==1:

    callsign = input("Enter Callsign: <q> to QUIT  >> ")


    
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


        callsign=""
