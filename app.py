# coding: utf-8

__author__ = 'rchibana'

from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy

from settings import DB_URI

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

    db.init_app(app)

    api_register(app)

    return app


def api_register(app):
    from resources.overflow import Overflow
    from resources.user import UserResource

    api = Api(app)

    # Overflow
    api.add_resource(Overflow, '/overflow', '/overflow/<int:time>')

    #User
    api.add_resource(UserResource, '/user', '/user/')

    return api