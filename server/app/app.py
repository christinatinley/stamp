from flask import Flask, jsonify, request
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
    city_name = "Paris, France"
    persona = Persona(
        start_day="2025-06-20",
        end_day="2025-06-21",
        culture=8,
        history=7,
        art=3,
        nature=4,
        walking_tours=5,
        shopping=9,
        price_level=2,
        breaks= ["2025-06-20 11:00–2025-06-19 12:00", "2025-06-20 11:00–2025-06-20 12:00"] 
    )
    itinerary = []
    lat, lng = model.build_places(city_name, persona.price_level, itinerary)

    whole_trip = []
    curr_day = datetime.strptime(persona.start_day, "%Y-%m-%d")
    end_day = datetime.strptime(persona.end_day, "%Y-%m-%d")
    itinerary = []
    while curr_day <= end_day:
        itinerary, day = generate_day.generate_day(itinerary, city_name, lat, lng, persona, curr_day)
        whole_trip += [day]
        curr_day = curr_day + timedelta(days=1)
        
    return jsonify(whole_trip)

@app.route('/itinerary', methods=['POST'])
def generate_itinerary():
    data = request.get_json()
    city_name = data['city_name']
    persona_data = data['persona']

    persona = Persona(
        start_day=persona_data['start_day'],
        end_day=persona_data['end_day'],
        culture=persona_data['culture'],
        history=persona_data['history'],
        art=persona_data['art'],
        nature=persona_data['nature'],
        walking_tours=persona_data['walking_tours'],
        shopping=persona_data['shopping'],
        price_level=persona_data['price_level'],
        breaks=persona_data['breaks']
    )

    itinerary = []
    lat, lng = model.build_places(city_name, persona.price_level, itinerary)

    whole_trip = []
    curr_day = datetime.strptime(persona.start_day, "%Y-%m-%d")
    end_day = datetime.strptime(persona.end_day, "%Y-%m-%d")
    itinerary = []
    while curr_day <= end_day:
        itinerary, day = generate_day.generate_day(itinerary, city_name, lat, lng, persona, curr_day)
        whole_trip += [day]
        curr_day = curr_day + timedelta(days=1)

    # whole_trip = []
    # itinerary, day = generate_day.generate_day([], city_name, persona)
    # for d in range(persona.days):
    #     whole_trip += [day]
    #     itinerary, day = generate_day.generate_day(itinerary, city_name, persona)
    
    return jsonify(whole_trip)


if __name__ == "__main__":
    app.run(port=5000, debug=True)