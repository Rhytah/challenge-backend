import re
from flask import jsonify


class UserValidator:
    def validate_add_user(
            self,
            firstname,
            lastname,
        email,
    ):
        if not re.match(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                email):
            return jsonify({
                "error": "Use valid email address format. ...janedoe@int.com"
            }), 422
        if not firstname or firstname.isspace():
            return jsonify({
                "error": "firstname is missing"}), 422
        if not lastname or lastname.isspace():
            return jsonify({
                "error": "lastname is missing"}), 422

        if not re.match(
                r"^([a-zA-Z\d]+[-_])*[a-zA-Z\d*]+$",
                firstname) or not isinstance(
                firstname,
                str):
            return jsonify({
                "error": "firstname cannot be integers, have white spaces or symbols"
            }), 422

        if not re.match(
                r"^([a-zA-Z\d]+[-_])*[a-zA-Z\d*]+$",
                lastname) or not isinstance(
                lastname,
                str):
            return jsonify({
                "error": "lastname cannot be integers have white spaces or symbols"
            }), 422
