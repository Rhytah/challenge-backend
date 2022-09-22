from flask import Blueprint,request, current_app as app,jsonify
from werkzeug.exceptions import HTTPException
from ..controllers import Duty_controller,db,duty_obj
from datetime import datetime
duty_controller = Duty_controller()
duty = Blueprint("duty", __name__)


@duty.route('/api/v1/duties', methods=['POST'])
def add_duty():
    duty_data = request.get_json()
    dog_id = duty_data.get('dog_id')
    user_id = duty_data.get('user_id')
    new_duty = duty_obj(user_id=user_id, dog_id=dog_id, start_time=datetime.now())
    db.session.add(new_duty)
    db.session.commit()

    return jsonify({"data": {
        "duty": new_duty.serialize(),
        "message": "Added dutysuccessfully"}
    }), 201


@duty.route('/api/v1/duties', methods=['GET'])
def fetch_duties():
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10
  
    return duty_controller.fetch_duties()

