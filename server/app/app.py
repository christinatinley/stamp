from flask import Flask, request, jsonify
import requests
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)


if __name__ == "__main__":
    app.run(debug=True)
