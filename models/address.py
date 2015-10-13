__author__ = 'rchibana'

from app import db


class Address(db.Model):
    latitude = db.Column(db.String(30))
    longitude = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
