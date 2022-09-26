#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from flask import Flask, jsonify, abort, request, make_response
from flask_cors import (CORS, cross_origin)
import os
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ POST /
    Return:
      - Json message verifying status
    """
    email = request.form[list(request.form)[0]]
    password = request.form[list(request.form)[1]]
    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    m = {"email": email, "message": "user created"}
    return jsonify(m), 200

@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ POST /
    Return:
      - Json message verifying status
    """
    email = request.form[list(request.form)[0]]
    password = request.form[list(request.form)[1]]
    if AUTH.valid_login(email, password):
        sid = AUTH.create_session(email)
        resp = make_response()
        resp.set_cookie('session_id', sid)
        return jsonify({"email": email, "message": "logged in"}), 200
    abort(401)


@app.route('/', methods=['GET'], strict_slashes=False)
def simple() -> str:
    """ GET /
    Return:
      - Simple Message
    """
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
