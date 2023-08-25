from flask import Blueprint, request, jsonify
from db.restaurant import add_restaurant, fetch_restaurant_records

restaurant_bp = Blueprint('restaurant', __name__)


@restaurant_bp.route('/restaurant', methods=['POST'])
def newRestaurant():
    try:
        data = request.json
        if 'name' in data and 'caption' in data and 'logoUrl' in data and 'email' in data and 'password' in data:
            add_restaurant(data)
            return jsonify({"message": "Record created successfully"}), 201
        else:
            return jsonify({"error": "Missing data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@restaurant_bp.route('/restaurants', methods=['GET'])
def getRestaurant():
    try:
        hotels = fetch_restaurant_records()
        return jsonify(hotels)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
