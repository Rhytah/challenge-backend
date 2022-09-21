import datetime
from .database.server import DatabaseConnect
db = DatabaseConnect()

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

class User:

    def get_users(self):
        cmd = "SELECT * FROM users;"
        db.cursor.execute(cmd)
        all_users = db.cursor.fetchall()
        return all_users

    def get_user(self, userid):
        cmd = "SELECT * FROM users WHERE userid='{}';".format(userid)
        db.cursor.execute(cmd)
        user = db.cursor.fetchone()
        return user

    def create_user(self, firstname, lastname, username, password, email):
        add_user_cmd = "INSERT INTO users(firstname,lastname, username, password, email)\
       VALUES ('{}','{}','{}','{}','{}') RETURNING email;".format(firstname, lastname, username, password, email)
        db.cursor.execute(add_user_cmd)
        return db.cursor.fetchone()
