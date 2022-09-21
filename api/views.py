from flask import Flask, json, jsonify, Blueprint,request, current_app as app


from .controllers import User_controller

user_controller = User_controller()
user = Blueprint("user", __name__)
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
@user.route('/api/v1/signup', methods=['POST'])
def signup():
    request_data = request.get_json()
    return user_controller.add_reporter(request_data)


@user.route('/api/v1/users', methods=['GET'])
def fetch_users():
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10
    return user_controller.fetch_users()



@user.route('/api/v1/login', methods=['POST'])
def login():
    user_data = request.get_json()
    return user_controller.signin(user_data)


@user.route('/api/v1/users/<int:userid>', methods=['GET'])
def get_a_reporter(userid):
    return user_controller.fetch_user(userid)