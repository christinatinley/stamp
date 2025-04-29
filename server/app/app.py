from flask import Flask, jsonify
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from knowledge_base import model

app = Flask(__name__)

@app.route('/itinerary', methods=['GET'])
def generate_itinerary(city_name, persona):
    return jsonify(model.generate_itinerary(city_name, persona.days, persona.culture, persona.history, persona.art, persona.nature, persona.walking_tours, persona.shopping))

if __name__ == "__main__":
    app.run(debug=True)
