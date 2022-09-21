import datetime
from flask import jsonify, json
from .database.server import DatabaseConnect
db = DatabaseConnect()


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


class User:

    def get_users(self):
        cmd = "SELECT firstname,lastname, username, email FROM users;"
        db.cursor.execute(cmd)
        all_users = db.cursor.fetchall()
        return all_users

    def get_user(self, userid):
        cmd = "SELECT  *FROM users WHERE userid='{}';".format(userid)
        db.cursor.execute(cmd)
        user = db.cursor.fetchone()
        return user

    def create_user(self, firstname, lastname, username, password, email):
        add_user_cmd = "INSERT INTO users(firstname,lastname, username, password, email)\
       VALUES ('{}','{}','{}','{}','{}') RETURNING email;".format(firstname, lastname, username, password, email)
        db.cursor.execute(add_user_cmd)
        return db.cursor.fetchone()

    def search_user(self, email):
        cmd = "SELECT * FROM users WHERE email='{}'".format(email)
        db.cursor.execute(cmd)
        result = db.cursor.fetchone()
        if result:
            return jsonify({
                "error": (email)+"  User already exists"}), 409

    def filter_search_user(self,value):

        # value=value[1]
        print(value)

        cmd = "SELECT * FROM users WHERE firstname='{}'".format(value)
        db.cursor.execute(cmd)
        result = db.cursor.fetchall()

        if result:
            return jsonify({
                "message": result,
                "number":len(result)}), 200
   
    

