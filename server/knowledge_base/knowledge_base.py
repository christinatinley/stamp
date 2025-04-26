from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv('PLACES_API_KEY') 

# get the latitude and longitude using the city name
def get_city(city_name):
    url = "https://places.googleapis.com/v1/places:searchText"
    params = {
        "query": city_name,
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        places = response.json()
        if places['results']:
            location = places["results"][0]["geometry"]["location"]
            lat = location["lat"]
            lng = location["lng"]
            return lat, lng

#get the list of places by the latitude and longitude
def get_places(lat, lng, radius):
    url = "https://places.googleapis.com/v1/places:searchNearby"
    
    headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": API_KEY,
    "X-Goog-FieldMask": "places.displayName,places.location"
    }
    
    body = {
        "locationRestriction": {
            "circle": {
                "center": {
                    "latitude": lat,
                    "longitude": lng
                },
                "radius": radius
            }
        }
    }

    response = requests.get(url, headers=headers, json=body)
    return response.json()