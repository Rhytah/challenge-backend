import json
import dateutil.parser
import babel
import sys
from flask import Flask, jsonify
from .config import app_configuration
from .database.relations_commands import sqlcommands
from .database.server import DatabaseConnect
from flask_cors import CORS
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

# app = Flask(__name__)
# app.config.from_object('config')
# db.init_app(app)

def create_app(mode):
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(app_configuration)

        CORS(app)

        db = DatabaseConnect()
        for command in sqlcommands:
            db.cursor.execute(command)

        print(f"connection successful on {db.credentials}")
        from .views import user
        app.register_blueprint(user)
    return app


app = create_app(mode='development')



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
