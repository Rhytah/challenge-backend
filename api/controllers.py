from multiprocessing.sharedctypes import Value
from sqlite3 import paramstyle
from .models import User, Dog, Duty, db
from flask import jsonify, json, request, current_app as app, abort
from .utilities import UserValidator
import datetime



validator = UserValidator()
user_obj = User
dog_obj = Dog
duty_obj = Duty



class User_controller:

    def add_user(self, *args):
        user_data = request.get_json()
        firstname = user_data.get('firstname')
        lastname = user_data.get('lastname')
        email = user_data.get('email')
        city = user_data.get('city')
        invalid_user = validator.validate_add_user(
            firstname, lastname, city, email)
        if invalid_user:
            return invalid_user
        existent_user = user_obj.search_user(email)

        if existent_user:
            return existent_user
        new_user = user_obj(
            firstname, lastname, city, email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"data": {
            "user": new_user,
            "message": "signup successful"}
        }), 201

    def fetch_users(self,page):

        page = request.args.get('page', page, type=int)
        results = user_obj.get_all(page=page)
        if results:
            return jsonify({

                "data": results,
                "message": "You are viewing registered users",
                "count":len(results),
                "page": page})
        return jsonify({

            "error": "No registered users at this time"
        }), 404

    def fetch_user(self, userid):
        user = user_obj.get_by_id_full(userid)
        if user:
            return jsonify({
                "data": user,
                "message": "User details displayed"
            })
        return jsonify({

            "error": "user_id out of range, try again with a valid id"
        }), 404
    
    def filter_users(self,*args):
        city = request.args.get('city')
        firstname = request.args.get('firstname')
        lastname = request.args.get('lastname')
        return user_obj.read_list(**request.args)
class Dog_controller:

    def fetch_dogs(self):

        page = request.args.get('page', 1, type=int)
        results = dog_obj.get_all()
        if results:
            return jsonify({

                "data": results,
                "message": "You are viewing registered dogs",
                "page": page})
        return jsonify({

            "error": "No registered dogs at this time"
        }), 404

    def fetch_dog(self, dogid):
        dog = dog_obj.get_by_id_full(dogid)
        if dog:
            return jsonify({
                "data": dog,
                "message": "Dog details displayed"
            })
        return jsonify({

            "error": "dog_id out of range, try again with a valid id"
        }), 404

class Duty_controller:

    def fetch_duties(self):

        page = request.args.get('page', 1, type=int)
        results = duty_obj.get_all()
        if results:
            return jsonify({

                "data": results,
                "message": "You are viewing registered users",
                "page": page})
        return jsonify({

            "error": "No registered duties at this time"
        }), 404

    def fetch_duty(self, dutyid):
        duty = duty_obj.get_by_id_full(dutyid)
        if duty:
            return jsonify({
                "data": duty,
                "message": "Duty details displayed"
            })
        return jsonify({

            "error": "duty_id out of range, try again with a valid id"
        }), 404
