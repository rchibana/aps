# coding: utf-8

__author__ = 'rchibana'

from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True)
    phone = Column(String(16), unique=True)
    addresses = relationship('address', backref='user')

    def __init__(self, email, phone):
        self.email = email
        self.phone = phone
