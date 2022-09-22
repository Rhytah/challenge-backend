from flask import Blueprint,request, current_app as app,jsonify
from werkzeug.exceptions import HTTPException
from ..controllers import Dog_controller,db,dog_obj

dog_controller = Dog_controller()
dog = Blueprint("dog", __name__)


@dog.route('/api/v1/dogs', methods=['POST'])
def add_dog():
    dog_data = request.get_json()
    name = dog_data.get('name')
    breed = dog_data.get('breed')
    age = dog_data.get('age')
    new_dog = dog_obj(name=name, breed=breed, age=age)
    db.session.add(new_dog)
    db.session.commit()

    return jsonify({
        "dog": new_dog.serialize(),
        "message": "Added dog successfully"}), 201


@dog.route('/api/v1/dogs', methods=['GET'])
def fetch_dogs():
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10
  
    return dog_controller.fetch_dogs()
