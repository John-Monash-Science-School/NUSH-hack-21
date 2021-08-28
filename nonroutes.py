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

def travel_calculator(start_location, end_location, co2_per_km):
    access_token = "sk.eyJ1IjoiYm9iMTIzMSIsImEiOiJja3N2M3BndjcxNTgwMm9xenFiNzZvdWxoIn0.mTgzAAZ_sb_oz60TSocXzg"
    perm_geocoder = Geocoder(name='mapbox.places-permanent')
    geocoder = Geocoder(access_token=access_token)
    out = {}

    response1 = geocoder.forward(start_location)
    first = response1.geojson()['features'][0]
    out["firstPlace"] = first['place_name']
    #print(f"{first['place_name']} {first['geometry']}")

    
    response2 = geocoder.forward(end_location)
    second = response2.geojson()['features'][0]
    out["second_place"] = second['place_name']
    #print(f"{second['place_name']} {second['geometry']}")

    service = Directions(access_token=access_token)

    response = service.directions([first, second],'mapbox/driving')
    global driving_routes
    driving_routes = response.geojson()
    #print(driving_routes)

    #co2_g_per_km = input(float("Enter in how much CO2 is given per km in grams: "))
    distance_of_trip = driving_routes['distance']
    total = distance_of_trip * co2_per_km
    #print(f"You will be usng {total} grams of CO2")
    # add something about those carbon tokens
    out["total_co2"] = total
    return out


