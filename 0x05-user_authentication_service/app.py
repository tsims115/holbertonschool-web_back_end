#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """POST"""
    email = list(request.form)[0]
    password = list(request.form)[1]
    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": "<registered email>", "message": "user created"}), 200


@app.route('/', methods=['GET'], strict_slashes=False)
def simple() -> str:
    """ GET /
    Return:
      - Simple Message
    """
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
