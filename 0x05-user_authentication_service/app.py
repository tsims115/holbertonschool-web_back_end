#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from flask import Flask, jsonify, abort, request, make_response, redirect
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
        resp = make_response({"email": email, "message": "logged in"})
        resp.set_cookie('session_id', sid)
        return resp, 200
    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ DELETE /
    Return:
      - Json message verifying status
    """
    cookie = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(cookie)
    if user is None or cookie is None:
        abort(403)
    AUTH.destroy_session(cookie)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """ GET /
    Return:
      - Json message verifying status
    """
    cookie = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(cookie)
    if user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """get reset_token"""
    email = request.form[list(request.form)[0]]
    try:
        token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)
    if token is not None:
        return jsonify({"email": email, "reset_token": token})


@app.route('/', methods=['GET'], strict_slashes=False)
def simple() -> str:
    """ GET /
    Return:
      - Simple Message
    """
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
