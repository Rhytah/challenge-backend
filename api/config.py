import os


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = b'\xc9$,\xa9\xdd;\xfeVz\xa0\x8f\xd5A,\x11\xf8\xf4\xceh\x94\xa9\x13\x80['
    DATABASE_URI = os.getenv('DATABASE_URL')
    PORT = 5432


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    DATABASE_URI = 'challenge_db'
    TESTING = False


class TestingConfig(Config):
    DEBUG = True
    ENV = 'testing'
    DATABASE_URI = 'test_db'
    TESTING = True






SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# Connect to the database

SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
# SQLALCHEMY_DATABASE_URI = 'postgres://ritanamono@localhost:5432/challenge_db'

SQLALCHEMY_TRACK_MODIFICATIONS = False 

app_configuration = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
}


template = {
    "swagger": "2.0",
    "info": {
        "title": "INU API",
        "description": "API for INU",
        "contact": {
            "responsibleOrganization": "",
            "responsibleDeveloper": "",
            "email": "ritanamono@gmail.com",
            "url": "www.twitter.com/ritanamono",
        },
        "termsOfService": "www.twitter.com/ritanamono",
        "version": "1.0"
    },
    "basePath": "/api/v1",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
        }
    },
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}