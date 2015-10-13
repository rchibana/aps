__author__ = 'rchibana'

from app import db

from flask import Flask, request
from flask_restful import Resource
from models.user import User
from models.address import Address


class Overflow(Resource):

    def get(self):
        """
        Will get all the overflow at last 1 hour
        :return:
        """

    def post(self):
        request_user = request.data['user']
        request_address = request.data['address']

        user = User(request_user.get('email', ''), request_user.get('phone', ''))
        address = Address(request_address.get('latitude'), request_address.get('longitude'))

        # Creating the user
        db.session.add(user)

        address.user_id = user.id
        db.session.add(address)

        db.commit()
