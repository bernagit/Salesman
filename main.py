import pandas as pd
from geopy.geocoders import Nominatim
from geopy import distance
import requests
import json

workbook = pd.read_excel("./indirizzi.xlsx", index_col=0)

values = []

for index, row in workbook.iterrows():
    values.append((row['indirizzo']))

geolocator = Nominatim(user_agent="My_locator")

coordinates = []

for address in values:
    location = geolocator.geocode(address, timeout=5)
    # print((location.latitude, location.longitude))
    coordinates.append([location.latitude, location.longitude])

print(coordinates)

body = {"locations":coordinates, "metrics":["distance"],"units":"km"}

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': '',
    'Content-Type': 'application/json; charset=utf-8'
}
call = requests.post('https://api.openrouteservice.org/v2/matrix/driving-car', json=body, headers=headers)

print(call.status_code, call.reason)
response = call.text

#write response in an outfile
with open('data.json', 'w') as outfile:
    json.dump(response, outfile)

print(response)

