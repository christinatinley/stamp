from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/places', methods=['GET'])
def get_places():
    input_text = request.args.get('input')
    api_key = "AIzaSyCjZ_ClVlhmfOTrzkbjpjk8LV_UHD68zgk"

    url = f"https://maps.googleapis.com/maps/api/place/queryautocomplete/json?input=pizza%20near%20par&key=AIzaSyCjZ_ClVlhmfOTrzkbjpjk8LV_UHD68zgk"
    params = {
        "input": input_text,
        "key": api_key
    }

    response = requests.get(url)
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=True)
