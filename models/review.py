#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Culumn, String, ForeignKey


class Review(BaseModel, Base):
    """ 
    Review class for storing review information
    """
    __tablename__ = "reviews"
    place_id = Column(String(1024), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
