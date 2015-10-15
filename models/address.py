
__author__ = 'rchibana'

from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime


class Address(Base):

    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    latitude = Column(String(30))
    longitude = Column(String(30))
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.date = datetime.now()
