from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv('PLACES_API_KEY') 

# get the latitude and longitude using the city name
def get_city(city_name):
    url = "https://places.googleapis.com/v1/places:searchText"
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "places.location"  # Only ask for lat/lng to keep response minimal
    }
    data = {
        "textQuery": city_name
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        places = response.json().get("places", [])
        if places:
            location = places[0]["location"]
            lat = location["latitude"]
            lng = location["longitude"]
            return lat, lng

#get the list of places by the latitude and longitude
def get_places(lat, lng, radius):
    url = "https://places.googleapis.com/v1/places:searchNearby"
    
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "places.displayName,places.location,places.formatted_address,places.rating,places.types,places.reviews,places.photos,places.types"
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

    response = requests.post(url, headers=headers, json=body)
    return response.json()
