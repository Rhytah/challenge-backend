import json
import dateutil.parser
import babel
import sys
from flask import Flask, jsonify
from .config import template, swagger_config
# from .database.relations_commands import sqlcommands
# from .database.server import DatabaseConnect
from flask_cors import CORS
from flasgger import Swagger, swag_from
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db,setup_db



def create_app():
    app = Flask(__name__)       
    db.init_app(app)
    with app.app_context():
        # app.config.from_object(app_configuration)
        SWAGGER={
            'title':"INU API"
        }
        app = Flask(__name__)
        # app.config.from_object('config')
        migrate = Migrate(app, db)

        setup_db(app)

        CORS(app, resources={r"/*": {"origins": "*"}})
      



        Swagger(app, config=swagger_config, template=template)

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
            "message": "Welcome"
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