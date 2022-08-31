#CAll grid grabber

#!/usr/bin/env python3


import requests
import json

callGet = ""

while 1==1:

    callGet = input("Enter Callsign: <q> to QUIT  >> ")
    
    if callGet == "q" :
        break

    else:
        try:
            api_url = f"https://api.hamdb.org/v1/{callGet}/json/CallGridGet"
            response = requests.get(api_url)
            hamdb = response.json()["hamdb"]
            callsign = hamdb["callsign"]
            grid = callsign["grid"]

            print (f"{callGet} GRID is {grid}")
            
        except:
            print (f"CALLSIGN {callGet} INVALID  <q> to QUIT")
