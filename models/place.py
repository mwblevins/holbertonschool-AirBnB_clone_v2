#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    city_id = column(string(60)
    user_id = column(string(60)
    name = column(string(128)
    description = column(string(1024)
    number_rooms = column(integer, default=0, nullable=false
    number_bathrooms = column(integer, default=0, nullable=false
    max_guest = column(integer, default=0, nullable=false
    price_by_night = column(integer, default, nullable=false
    latitude = column(float,0 nullable=true)
    longitude = column(float, nullable=true)
    amenity_ids = []
