import pandas as pd
from geopy.geocoders import Nominatim
from geopy import distance

workbook = pd.read_excel("./indirizzi.xlsx", index_col=0)

values = []

for index, row in workbook.iterrows():
    values.append((row['indirizzo']))

geolocator = Nominatim(user_agent="My_locator")

coordinates = []

for address in values:
    location = geolocator.geocode(address, timeout=5)
    # print((location.latitude, location.longitude))
    coordinates.append(([location.latitude], [location.longitude]))

print(coordinates)
# print(distance.distance((coordinates[0][0], coordinates[0][1]), (coordinates[1][0], coordinates[1][1])).km)
