import imp
from flask import Flask, json, jsonify, Blueprint,request, current_app as app
from werkzeug.exceptions import HTTPException
from flask_cachecontrol import (
    cache,
    cache_for,
    dont_cache,
    Always, 
    ResponseIsSuccessfulOrRedirect)

from .controllers import User_controller
from flasgger import  swag_from

user_controller = User_controller()
user = Blueprint("user", __name__)


@user.route('/api/v1/signup', methods=['POST'])
def signup():
    request_data = request.get_json()
    return user_controller.add_reporter(request_data)


@user.route('/api/v1/users', methods=['GET'])
@swag_from('./docs/user/user.yaml')
def fetch_users():
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10
    print("users")
    return user_controller.fetch_users()



@user.route('/api/v1/login', methods=['POST'])
def login():
    user_data = request.get_json()
    return user_controller.signin(user_data)


@user.route('/api/v1/users/<int:userid>', methods=['GET'])
@swag_from('./docs/user/specific_user.yaml')
def get_a_reporter(userid):
    return user_controller.fetch_user(userid)

