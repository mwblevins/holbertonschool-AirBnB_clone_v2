#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="delete")
    else:
        @property
        def cities(self):
            """uhhhhhh"""
            city_list = []
            for x in models.storage.all(City).values():
                if x.state_id == self.id:
                    city_list.append(x)
            return city_list
