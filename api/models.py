import datetime
import os
from flask import jsonify, json
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

database_path = os.environ['DATABASE_URL']


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    email = db.Column(db.String(120))
    city = db.Column(db.String(120))

    @classmethod
    def get_by_id_full(cls, id):
        details = {}
        user = cls.get_by_id(id)
        details.update(user.serialize)

        return details

    @classmethod
    def search_user_name(cls, firstname):
        users = cls.query.filter(cls.firstname.ilike(f'%{firstname}%')).outerjoin(
            Duty, cls.id == Duty.user_id).all()
        return [
            {
                "id": user.id,
                "firstname": user.firstname,
                "lastname": user.lastname
            }
            for user in users
        ]

    @classmethod
    def get_all(cls):
        users = cls.query.all()
        results = [
            {
                'firstname': user.firstname,
                'lastname': user.lastname,
                'city': user.city,
                'email': user.email,
                'id': user.id
            }
            for user in users
        ]

        return results

    def exists(cls, email):
        return cls.query.filter(db.func.lower(cls.email) == db.func.lower(email)).count()

    @property
    def num_upcoming_shows(self):
        return self.query.join(Duty).filter_by(user_id=self.id).filter(
            Duty.start_time > datetime.now()).count()

    @property
    def num_past_shows(self):
        return self.query.join(Duty).filter_by(user_id=self.id).filter(
            Duty.start_time < datetime.now()).count()

    @property
    def past_shows(self):
        return Duty.get_past_by_user(self.id)

    @property
    def upcoming_shows(self):
        return Duty.get_upcoming_by_user(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'city': self.city,
        }

    def __repr__(self):
        return f'<User name: {self.firstname}>'


class Dog(db.Model):
    __tablename__ = 'Dog'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    breed = db.Column(db.String)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f'<Dog self.id {self.name}>'

    @classmethod
    def get_by_id_full(cls, id):
        details = {}
        dog = cls.get_by_id(id)
        details.update(dog.serialize)

        return details

    @classmethod
    def search_dog_name(cls, dog_name):
        dogs = cls.query.filter(
            cls.name.ilike(f'%{dog_name}%')
        ).all()
        return [
            {
                "id": dog.id,
                "name": dog.name,
                "breed": dog.breed
            }
            for dog in dogs
        ]

    @classmethod
    def get_all(cls):
        dogs = cls.query.all()
        results = [
            {
                'name': dog.name,
                'breed': dog.breed,
                'age': dog.age,
                'id': dog.id
            }
            for dog in dogs
        ]

        return results

    @property
    def num_upcoming_shows(self):
        return self.query.join(Duty).filter_by(dog_id=self.id).filter(
            Duty.start_time > datetime.now()).count()

    @property
    def num_past_shows(self):
        return self.query.join(Duty).filter_by(dog_id=self.id).filter(
            Duty.start_time < datetime.now()).count()

    @property
    def past_shows(self):
        return Duty.get_past_by_dog(self.id)

    @property
    def upcoming_shows(self):
        return Duty.get_upcoming_by_og(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'breed': self.breed,
            'age': self.age,
        }

    def __repr__(self):
        return f'<Dog name: {self.name}>'


class Duty(db.Model):
    __tablename__ = 'Duty'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    dog_id = db.Column(db.Integer, db.ForeignKey('Dog.id'))
    start_time = db.Column(db.DateTime)
    user = db.relationship('User', viewonly=True)
    dog = db.relationship('Dog', viewonly=True)

    def __repr__(self):
        return f'<Duty id: {self.id} user_id:{self.user_id} dog_id: {self.dog_id}'

    @classmethod
    def count_upcoming_by_dog_id(cls, dog_id):
        return cls.query.filter_by(dog_id=dog_id).filter(cls.start_time > datetime.now()).count()

    @classmethod
    def count_past_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).filter(cls.start_time < datetime.now()).count()

    @classmethod
    def get_past_by_dog(cls, dog_id):
        duties = cls.query.filter_by(dog_id=dog_id).filter(
            cls.start_time < datetime.now()).all()
        return [duty.duty_details for duty in duties]

    @classmethod
    def get_past_by_user(cls, user_id):
        duties = cls.query.filter_by(user_id=user_id).filter(
            cls.start_time < datetime.now()).all()
        return [duty.duty_details for duty in duties]

    @classmethod
    def get_upcoming_by_og(cls, dog_id):
        duties = cls.query.filter_by(dog_id=dog_id).filter(
            cls.start_time > datetime.now()).all()
        return [duty.duty_details for duty in duties]

    @classmethod
    def get_upcoming_by_user(cls, user_id):
        duties = cls.query.filter_by(user_id=user_id).filter(
            cls.start_time > datetime.now()).all()
        return [duty.duty_details for duty in duties]

    @classmethod
    def get_all(cls):
        return [duty.duty_details for duty in cls.query.order_by(cls.dog_id.desc()).all()]

    @property
    def duty_details(self):
        return {
            'id': self.id,
            'dog_id': self.dog_id,
            "user_id": self.user_id,
            'start_time': self.start_time
        }
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'dog_id': self.dog_id,
            'start_time': self.start_time,
        }

    def __repr__(self):
        return f'<Dog name: {self.name}>'