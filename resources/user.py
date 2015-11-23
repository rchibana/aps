__author__ = 'rchibana'

from flask import jsonify, request
from flask_restful import Resource
from models import User
from app import db


class UserResource(Resource):

    def post(self):

        data = request.json

        email = data['user'].get('email', '')
        phone = data['user'].get('phone', '')

        user = User.query.filter_by(email=email, phone=phone).first()

        if user:
            return jsonify(user.serialize())

        user = User(email, phone)

        db.session.add(user)
        db.session.commit()

        return jsonify(user.serialize())
