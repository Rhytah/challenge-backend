import psycopg2 
from flask import current_app as app,abort
# from config import app_configuration
from psycopg2.extras import RealDictCursor
from .relations_commands import sqlcommands
import os

class DatabaseConnect:

    def __init__(self):
        
        self.credentials = dict(
                dbname =os.environ['DATABASE'],
                user = os.environ['USER'],
                password=os.environ['PASSWORD'],
                host=os.environ['HOST'],
                port =os.environ['PORT']
            )
        # self.credentials=os.getenv('DATABASE_URL')
        print(self.credentials)
        # self.credentials['user']=app_configuration['production'].USER
        # self.credentials['password']=app_configuration['production'].PASSWORD
        # self.credentials['host']=app_configuration['production'].HOST
        # self.credentials['port']=app_configuration['production'].PORT
        
        self.conn =  psycopg2.connect(**self.credentials, cursor_factory=RealDictCursor)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def drop_table(self,tablename):
        command = f"""
        DROP TABLE IF EXISTS {tablename} CASCADE
        """
        return self.cursor.execute(command)