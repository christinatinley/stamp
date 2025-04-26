from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests

load_dotenv()

def get_places():
    input_text = request.args.get('input')
    api_key = os.getenv('PLACES_API_KEY') 

    url = f"https://maps.googleapis.com/maps/api/place/autocomplete/json"
    params = {
        "input": input_text,
        "key": api_key
    }

    response = requests.get(url, params=params)
    return jsonify(response.json())
