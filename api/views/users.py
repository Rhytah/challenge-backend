from flask import Blueprint,request, current_app as app,jsonify
from ..controllers import User_controller, validator,user_obj,db
from flasgger import  swag_from

user_controller = User_controller()
user = Blueprint("user", __name__)


@user.route('/api/v1/users', methods=['POST'])
def signup():
    user_data = request.get_json()
    firstname = user_data.get('firstname')
    lastname = user_data.get('lastname')
    email = user_data.get('email')
    city = user_data.get('city')
    # invalid_user = validator.validate_add_user(
    #     firstname, lastname, email)
    # if invalid_user:
    #     return invalid_user
    # existent_user = user_obj.exists(email=email)

    # if existent_user:
    #     return existent_user
    new_user = user_obj(
        firstname=firstname, lastname=lastname, city=city, email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"data": {
        "user": new_user.serialize(),
        "message": "Registration successful"}
    }), 201


@user.route('/api/v1/users', methods=['GET'])
@swag_from('api/docs/user/user.yaml')
def fetch_users():
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10
  
    return user_controller.fetch_users()


@user.route('/api/v1/users/<int:userid>', methods=['GET'])
@swag_from('api/docs/user/specific_user.yaml')
def get_a_reporter(userid):
    return user_controller.fetch_user(userid)

