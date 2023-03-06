#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60))
    user_id = Column(String(60))
    name = Column(String(128))
    description = Column(String(1024))
    number_rooms = Column(int, default=0, nullable=False)
    number_bathrooms = Column(int, default=0, nullable=False)
    max_guest = Column(int, default=0, nullable=False)
    price_by_night = Column(int, default=0, nullable=False)
    latitude = Column(float, nullable=True)
    longitude = Column(float, nullable=True)
    amenity_ids = []
