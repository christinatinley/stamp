from flask import Flask, jsonify
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from knowledge_base import model

app = Flask(__name__)

class Persona:
    def __init__(self, days, culture, history, art, nature, walking_tours, shopping):
        self.days = days
        self.culture = culture
        self.history = history
        self.art = art
        self.nature = nature
        self.walking_tours = walking_tours
        self.shopping = shopping

@app.route("/")
def home():
    city_name = "Chicago"
    persona = Persona(
        days=2,
        culture=10,
        history=7,
        art=5,
        nature=2,
        walking_tours=3,
        shopping=2
    )

    itinerary = model.generate_itinerary(city_name, persona.days, persona.culture, persona.history, persona.art, persona.nature, persona.walking_tours, persona.shopping)
    return jsonify(itinerary)


# @app.route('/itinerary', methods=['GET'])
# def generate_itinerary(city_name, persona):
#     itinerary = model.generate_itinerary(city_name, persona.days, persona.culture, persona.history, persona.art, persona.nature, persona.walking_tours, persona.shopping)
#     return jsonify(itinerary)

if __name__ == "__main__":
    app.run(port=5000, debug=True)