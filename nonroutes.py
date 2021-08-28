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
    #print(driving_routes)
    distance_of_trip = driving_routes['features'][0]['properties']['distance']
    total = distance_of_trip * co2_per_km
    #print(f"You will be usng {total} grams of CO2")
    # add something about those carbon tokens
    # multiply to get in tonnes
    out["total_co2"] = total * 0.000001
    return out

def power_calculator(source, GJ, total_tonnes):
    out = {}

    # somehow got to change it so it can work with the site, here it is

    source = input("Enter in source: ")
    GJ = float(input("Enter how much power has been used in gigajoules in the last 24 hours: "))
    if source == "solar":  
        print("No carbon coins deducted")
    elif source == "wind":
        print("No carbon coins deducted")
    elif source == "hydro":
        print("No carbon coins deducted")
    elif source == "natural gas"
        natural_gas_estimate = 0.0537 # 0.0537 tonnes of CO2 from 1 GJ of Natural Gas
        total_tonnes = natural_gas_used * GJ
        print(total_tonnes) 
    elif source == "diesel":
        diesel_estimate = 0.069337442218798 # tonnes of CO2 from 1 GJ of Diesel
        total_tonnes = diesel_estimate * GJ
        print(total_tonnes)
    elif source == "nuclear":
        print("No carbon coins deducted")
    elif source == "black coal":
        black_coal_estimate = 0.088547008547009
        total_tonnes = black_coal_estimate * GJ
        print(total_tonnes)
    elif source == "brown coal":
        brown_coal_estimate = 0.09387222946545
        total_tonnes = brown_coal_estimate * GJ
        print(total_tonnes)
    else:
        print("Some fields are blank. Please go back")

