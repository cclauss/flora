from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import os

DB_NAME = 'sqlite:///test.db'

e = create_engine(DB_NAME)

app = Flask(__name__)
api = Api(app)

class NameRegistry(Resource):
		def get(self):
			name = request.form['name']
			conn = e.connect()
			#Perform query and return JSON data
			query = conn.execute("SELECT * FROM names WHERE name='{}'".format(name)).fetchone()
			if query != None:
				return True
			return False

app = Flask(__name__)
api = Api(app)

api.add_resource(NameRegistry, '/names')

if __name__ == '__main__':
    app.run(debug=True)