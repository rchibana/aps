# coding: utf-8

__author__ = 'rchibana'

from app import db


class User(db.Model):
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(16), unique=True)
    addresses = db.relationship('Address', backref='user', lazy='dynamic')

    def __init__(self, email, phone):
        self.email = email
        self.phone = phone
