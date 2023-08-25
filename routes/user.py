from flask import Blueprint, request, jsonify

from db.user import add_user

user_bp = Blueprint('user', __name__)


@user_bp.route('/user', methods=['POST'])
def new_user():
    try:
        data = request.json
        if 'email' in data and 'password' in data and 'first_name' in data and 'last_name' in data and 'ph_number' in data and 'address' in data:
            add_user(data)
            return jsonify({"message": "User record created successfully"}), 201
        else:
            return jsonify({"error": "Missing data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
