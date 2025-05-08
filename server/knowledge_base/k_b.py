from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv('PLACES_API_KEY') 

PRICE_ORDER = {
    "PRICE_LEVEL_FREE": 0,
    "PRICE_LEVEL_INEXPENSIVE": 1,
    "PRICE_LEVEL_MODERATE": 2,
    "PRICE_LEVEL_EXPENSIVE": 3,
    "PRICE_LEVEL_VERY_EXPENSIVE": 4
}


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

def get_food(lat, lng, radius, price_level, include_unpriced = True):
    url = "https://places.googleapis.com/v1/places:searchNearby"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "places.displayName,places.location,places.rating,places.types,places.priceLevel"
    }

    body = {
        "locationRestriction": {
            "circle": {
                "center": {"latitude": lat, "longitude": lng},
                "radius": radius
            }
        },
        "includedTypes": ["restaurant"],
        "rankPreference": "POPULARITY"
    }

    response = requests.post(url, headers=headers, json=body)
    data = response.json()

    max_val = PRICE_ORDER.get(price_level, 4)

    all_filtered_places = []
    for place in data.get("places", []):
        price = place.get("priceLevel")
        if price is None:
            if include_unpriced:
                all_filtered_places.append(place)
        else:
            price_val = PRICE_ORDER.get(price)
            if price_val is not None and price_val <= max_val:
                all_filtered_places.append(place)

    return all_filtered_places

#get the list of places by the latitude and longitude
def get_all_places(lat, lng, radius, price_level, include_unpriced=True):
    url = "https://places.googleapis.com/v1/places:searchNearby"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "places.displayName,places.location,places.rating,places.types,places.priceLevel"
    }

    all_filtered_places = []
    next_page_token = None

    while True:
        body = {
            "locationRestriction": {
                "circle": {
                    "center": {"latitude": lat, "longitude": lng},
                    "radius": radius
                }
            },
            "includedTypes": [
                "tourist_attraction", "museum", "art_gallery", "park", "shopping_mall",
                "library", "book_store", "cafe", "clothing_store", "university",
                "train_station", "shoe_store", "mosque", "synagogue", "church"
            ],
            "rankPreference": "POPULARITY"
        }

        if next_page_token:
            body["pageToken"] = next_page_token

        response = requests.post(url, headers=headers, json=body)
        data = response.json()

        max_val = PRICE_ORDER.get(price_level, 4)

        for place in data.get("places", []):
            price = place.get("priceLevel")
            if price is None:
                if include_unpriced:
                    all_filtered_places.append(place)
            else:
                price_val = PRICE_ORDER.get(price)
                if price_val is not None and price_val <= max_val:
                    all_filtered_places.append(place)

        next_page_token = data.get("nextPageToken")
        if not next_page_token:
            break

    return all_filtered_places


