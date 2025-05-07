from flask import Flask, jsonify
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from knowledge_base import model
from itinerary import generate_day

app = Flask(__name__)

class Persona:
    def __init__(self, days, culture, history, art, nature, walking_tours, shopping, price_level):
        self.days = days
        self.culture = culture
        self.history = history
        self.art = art
        self.nature = nature
        self.walking_tours = walking_tours
        self.shopping = shopping
        self.price_level = price_level

@app.route("/")
def home():
    city_name = "New York City"
    persona = Persona(
        days=2,
        culture=7,
        history=7,
        art=5,
        nature=7,
        walking_tours=4,
        shopping=5,
        price_level=2
    )
    itinerary = []
    lat, lng = model.build_places(city_name, persona.price_level, itinerary)

    whole_trip = []
    itinerary, day = generate_day.generate_day([], city_name, lat, lng, persona)
    for d in range(persona.days - 1):
        whole_trip += [day]
        itinerary, day = generate_day.generate_day(itinerary, city_name, lat, lng, persona)
    
    whole_trip += [day]
    return jsonify(whole_trip)

@app.route('/itinerary', methods=['GET'])
def generate_itinerary(city_name, persona):
    whole_trip = []
    itinerary, day = generate_day.generate_day([], city_name, persona)
    for d in range(persona.days):
        whole_trip += [day]
        itinerary, day = generate_day.generate_day(itinerary, city_name, persona)
    
    return jsonify(whole_trip)


if __name__ == "__main__":
    app.run(port=5000, debug=True)