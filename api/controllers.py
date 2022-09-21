from .models import User
from flask import jsonify, json, request, current_app as app


from .utilities import UserValidator
import datetime

validator = UserValidator()
user_obj = User()


class User_controller:

    def add_user(self, *args):
        user_data = request.get_json()
        firstname = user_data.get('firstname')
        lastname = user_data.get('lastname')
        email = user_data.get('email')
        username = user_data.get('username')
        password = user_data.get('password')
        invalid_user = validator.validate_add_user(
            firstname, lastname, username, email, password)
        if invalid_user:
            return invalid_user
        existent_user = user_obj.signup_search_user(email)

        if existent_user:
            return existent_user
        new_user = user_obj.create_user(
            firstname, lastname, username, password, email)

        return jsonify({"data": {
            "user": new_user,
            "message": "signup successful"}
        }), 201

    def fetch_users(self):
        result = user_obj.get_users()
        if result:
            return jsonify({

                "data": result,
                "message": "You are viewing registered users"})

    def fetch_user(self, userid):
        user = user_obj.get_user(userid)
        if user:
            return jsonify({
                "data": user,
                "message": "User details displayed"
            })
        return jsonify({

            "error": "user_id out of range, try again with a valid id"
        }), 404