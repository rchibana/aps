__author__ = 'rchibana'

from app import db
from datetime import datetime

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.String(30))
    longitude = db.Column(db.String(30))
    date = db.Column(db.DateTime, default=datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    @property
    def serialize(self):
        return {
            'id': self.id,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'date': self.date}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(16), unique=True)

    addresses = db.relationship('Address', backref='person', lazy='dynamic')

    # addresses = db.relationship('Address', secondary=user_address, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'phone': self.phone}
