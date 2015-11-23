__author__ = 'rchibana'

from flask import request, jsonify
from flask_restful import Resource
from models import Address, User
from app import db

import datetime


class Overflow(Resource):

    def get(self, time):

        date = datetime.datetime.now() - datetime.timedelta(minutes=time)
        addresses = Address.query.filter(Address.date >= date)

        return jsonify(result=[address.serialize for address in addresses.all()])

    def post(self):

        data = request.json
        user_id = data['user_id']
        address_data = data['address']

        user = User.query.get(user_id)

        if not user:
            return jsonify({
                'status': 'error',
                'message': 'User not found'
            })

        longitude = address_data.get('longitude', None)
        latitude = address_data.get('latitude', None)

        address = Address(
            longitude=longitude,
            latitude=latitude)

        user.addresses.append(address)

        db.session.add(user)
        db.session.add(address)

        db.session.commit()

        return jsonify({
            'status': 'ok',
            'message': 'success'
        })
