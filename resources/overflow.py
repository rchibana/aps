__author__ = 'rchibana'

from flask import request, jsonify
from flask_restful import Resource
from database import db_session as db
from models.address import Address
from models.user import User


class Overflow(Resource):

    def get(self, overflow_id):
        """
        Will get all the overflow at last 1 hour
        :return:
        """


        return {'teste': 'isso foi um get'}

    def post(self):

        request_user = request.json
        request_address = request.data['address']

        user = User(request_user.get('email', ''), request_user.get('phone', ''))
        address = Address(request_address.get('latitude'), request_address.get('longitude'))

        # Creating the user
        db.session.add(user)

        address.user_id = user.id
        db.session.add(address)

        db.commit()

        return jsonify({
                    'status': 'ok',
                    'response': 'success'
                })
