from flask import Blueprint,request, current_app as app,jsonify
from ..controllers import User_controller, validator,user_obj,db

user_controller = User_controller()
user = Blueprint("user", __name__)


@user.route('/api/v1/users', methods=['POST'])
def signup():
    user_data = request.get_json()
    firstname = user_data.get('firstname')
    lastname = user_data.get('lastname')
    email = user_data.get('email')
    city = user_data.get('city')
    new_user = user_obj(
        firstname=firstname, lastname=lastname, city=city, email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        "user": new_user.serialize(),
        "message": "Registration successful"}), 201


@user.route('/api/v1/users', methods=['GET'])
def fetch_users():
    page = request.args.get('page', 1, type=int)
    return user_controller.fetch_users(page)

@user.route('/api/v1/users/filter', methods=['GET'])
def filter_users():
        city = request.args.get('city')
        firstname = request.args.get('firstname')
        lastname = request.args.get('lastname')
        
        return user_obj.read_list(**request.args)

