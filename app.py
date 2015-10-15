# coding: utf-8

__author__ = 'rchibana'

from flask import Flask
from flask_restful import Api
from resources.overflow import Overflow


app = Flask(__name__)
api = Api(app)

# Register the api's here
api.add_resource(Overflow, '/overflow', '/overflow/<string:overflow_id>')

if __name__ == '__main__':
    app.run(debug=True)
