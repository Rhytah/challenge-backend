from multiprocessing.sharedctypes import Value
from sqlite3 import paramstyle
from .models import User
from flask import jsonify, json, request, current_app as app, abort


from .utilities import UserValidator
import datetime

validator = UserValidator()
user_obj = User()

USERS_PER_PAGE = 10


def paginate_users(page, selection):
    '''
        Method to pagenate questions.
    '''
    USERS_PER_PAGE = 10

    start = (page - 1) * USERS_PER_PAGE
    end = start + USERS_PER_PAGE

    allRecords = []

    for item in selection:
        item = item.format()
        allRecords.append(item)

    current_records = allRecords[start:end]

    return current_records


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
        existent_user = user_obj.search_user(email)

        if existent_user:
            return existent_user
        new_user = user_obj.create_user(
            firstname, lastname, username, password, email)

        return jsonify({"data": {
            "user": new_user,
            "message": "signup successful"}
        }), 201

    def fetch_users(self):

        page = request.args.get('page', 1, type=int)
        start = (page - 1) * 10
        end = start + 10
        results = user_obj.get_users()
        if results:
            return jsonify({

                "data": results[start:end],
                "message": "You are viewing registered users",
                "page": page})
        return jsonify({

            "error": "No registered users at this time"
        }), 404

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

