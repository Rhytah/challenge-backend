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


app_configuration = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
}