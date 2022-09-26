#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)


@app_views.route('/', methods=['GET'], strict_slashes=False)
def simple() -> str:
    """ GET /
    Return:
      - Simple Message
    """
    return flask.jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
