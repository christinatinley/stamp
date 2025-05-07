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
        culture=10,
        history=7,
        art=5,
        nature=2,
        walking_tours=3,
        shopping=2,
        price_level=2
    )

    itinerary, day = generate_day.generate_day([], city_name, persona)
    return jsonify(day)

@app.route('/itinerary', methods=['GET'])
def generate_itinerary(city_name, persona):
    suggestion = model.generate_first(city_name, persona.days, persona.culture, persona.history, persona.art, persona.nature, persona.walking_tours, persona.shopping, [])
    
    
    itinerary = [suggestion[0]]
    itinerary += [model.generate_itinerary(city_name, lat, lng, persona.days, persona.culture, persona.history, persona.art, persona.nature, persona.walking_tours, persona.shopping)[1]]
    return jsonify(itinerary)

if __name__ == "__main__":
    app.run(port=5000, debug=True)