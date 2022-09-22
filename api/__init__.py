
import os
import sys
from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from .models import db, setup_db, User
from faker import Faker
import sqlalchemy
from sqlalchemy.orm import Session, sessionmaker


fake = Faker()
database_path = os.environ['DATABASE_URL']

engine = sqlalchemy.create_engine(database_path)
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = Session()


def add_records():
    number_of_records = 300000
    records = []
    for i in range(0, number_of_records):
        name = fake.name().split(' ')
        record = {
            'firstname': name[0],
            'lastname': name[1],
            'email': f'{name[0]}.{name[1]}@rita.com',
            'city': fake.address()
        }
        records.append(User(**record))

    s = Session()
    s.begin()
    s.bulk_save_objects(records)
    s.commit()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    with app.app_context():

        app = Flask(__name__)
        migrate = Migrate(app, db)

        setup_db(app)
        # add_records()

        CORS(app, resources={r"/*": {"origins": "*"}})

        from .views.users import user
        from .views.dogs import dog
        from .views.duties import duty

        app.register_blueprint(user)
        app.register_blueprint(dog)
        app.register_blueprint(duty)

    @app.after_request
    def add_header(response):
        """ enabling cache-control"""
        response.cache_control.max_age = 300

        """ configuring CORS"""
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def index():
        return jsonify({
            "message": "Welcome Inu. Please read the README.md file to get started "
        })

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": error.description
        }), 400

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": 'Internal Server Error. Contact admin!'
        }), 500

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": 'Method Not Allowed. Double check that you are using the appropriate method for resource.'
        }), 405

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource not found"
        }), 404

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
