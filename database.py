__author__ = 'rchibana'

import flask
from settings import DB_URI
from app import db


def create_db():
    app = flask.Flask("app")
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return None


if __name__=='__main__':
    create_db()