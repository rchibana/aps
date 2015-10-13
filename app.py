# coding: utf-8

__author__ = 'rchibana'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Api
from resources.overflow import Overflow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:////tmp/test.db'

db = SQLAlchemy(app)

api = Api(app)

# Register the api's here
api.add_resource(Overflow, '/overflow', '/overflow/')
api.add_resource(Overflow, '/overflow', '/overflow/create/')

if __name__ == '__main__':
    app.run(debug=True)
