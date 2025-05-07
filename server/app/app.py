from flask import Flask, jsonify
from flask_cors import CORS
import requests
import sys
import os
from datetime import timedelta, datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from knowledge_base import model
from itinerary import generate_day

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

class Persona:
    def __init__(self, start_day, end_day, culture, history, art, nature, walking_tours, shopping, price_level, breaks):
        self.start_day = start_day
        self.end_day = end_day
        self.culture = culture
        self.history = history
        self.art = art
        self.nature = nature
        self.walking_tours = walking_tours
        self.shopping = shopping
        self.price_level = price_level
        self.breaks = breaks

@app.route("/")
def home():
    city_name = "New York City"
    persona = Persona(
        start_day="2025-06-19",
        end_day="2025-06-20",
        culture=7,
        history=7,
        art=5,
        nature=7,
        walking_tours=4,
        shopping=5,
        price_level=2,
        breaks= ["2025-06-19 10:00–2025-06-19 10:30", "2025-06-20 12:00–2025-06-20 13:30"] 
    )
    itinerary = []
    lat, lng = model.build_places(city_name, persona.price_level, itinerary)

    whole_trip = []
    curr_day = datetime.strptime(persona.start_day, "%Y-%m-%d")
    end_day = datetime.strptime(persona.end_day, "%Y-%m-%d")
    itinerary = []
    while curr_day <= end_day:
        print("Today:", curr_day)
        itinerary, day = generate_day.generate_day(itinerary, city_name, lat, lng, persona, curr_day)
        whole_trip += [day]
        curr_day = curr_day + timedelta(days=1)
        
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