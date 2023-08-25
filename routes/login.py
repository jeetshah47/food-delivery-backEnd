from flask import Blueprint, request, jsonify
from db.login import check_credentials_restaurant, check_credentials_user

login_bp = Blueprint('login', __name__)


@login_bp.route('/login/restaurant', methods=['POST'])
def loginRestaurant():
    try:
        data = request.get_json()

        if 'email' not in data or 'password' not in data:
            return jsonify({"error": "Email and password are required fields"}), 400

        email = data['email']
        password = data['password']

        authenticated, data = check_credentials_restaurant(email, password)

        if authenticated:
            return jsonify(data)
        else:
            return jsonify(data), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@login_bp.route('/login/user', methods=['POST'])
def loginUser():
    try:
        data = request.get_json()

        if 'email' not in data or 'password' not in data:
            return jsonify({"error": "Email and password are required fields"}), 400

        email = data['email']
        password = data['password']

        authenticated, data = check_credentials_user(email, password)

        if authenticated:
            return jsonify(data)
        else:
            return jsonify(data), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500
