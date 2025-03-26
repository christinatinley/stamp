from flask import Flask
from flask_cors import CORS

# Initialize the database


def create_app():
    app = Flask(__name__)
    # Load configurations

    # Initialize extensions
    CORS(app)  # Enable CORS

    return app
