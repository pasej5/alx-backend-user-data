#!/usr/bin/env python3
"""
Basic Flask_app
"""


from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> str:
    """_basic flask app
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['GET'])
def users() -> str:
    """_endpoint to register a user
    """
    email = request.form.get('email')
    password = request.form.get('password')

    # lets register the user if they dont exist
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
