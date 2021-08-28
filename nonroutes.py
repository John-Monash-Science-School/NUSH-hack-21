from hashlib import sha256
import random

# This is for the calculator
from mapbox import Geocoder
from mapbox import Directions

def gen_hash(pass1, salt):
    m = sha256()
    m.update(pass1.encode())
    m.update(salt.encode())
    return m.hexdigest()

def calculator:
    access_token = "sk.eyJ1IjoiYm9iMTIzMSIsImEiOiJja3N2M3BndjcxNTgwMm9xenFiNzZvdWxoIn0.mTgzAAZ_sb_oz60TSocXzg"
    perm_geocoder = Geocoder(name='mapbox.places-permanent')
    geocoder = Geocoder(access_token=access_token)

    start = input(str("Enter in Starting Address: "))
    response1 = geocoder.forward(start)
    first = response1.geojson()['features'][0]
    print(f"{first['place_name']} {first['geometry']}")

    destination = input(str("Enter in Destination: "))
    response2 = geocoder.forward(destination)
    second = response2.geojson()['features'][0]
    print(f"{second['place_name']} {second['geometry']}")

    service = Directions(access_token=access_token)

    response = service.directions([first, second],'mapbox/driving')
    global driving_routes
    driving_routes = response.geojson()
    print(driving_routes)

    co2_g_per_km = input(float("Enter in how much CO2 is given per km in grams: "))
    distance_of_trip = driving_routes['distance']
    total = distance_of_trip * co2_g_per_km
    print(f"You will be usng {total} grams of CO2")
    # add something about those carbon tokens
