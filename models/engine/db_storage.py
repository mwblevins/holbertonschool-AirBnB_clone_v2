#!/usr/bin/python3
import os
from os import getenv
from models.base_model import Base, BaseModel
from models.review import Review
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.user import User
from models.place import Place
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        # create the engine
        user = os.environ.get('HBNB_MYSQL_USER')
        password = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
        db = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                       format(user, password, host, db),
                                       pool_pre_ping=True)
        # drop all tables if environment variable HBNB_ENV is equal to test
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        from models import classes
        objs = {}
        if cls is None:
            for c in classes:
                objs.update({o.__class__.__name__ + '.' + o.id: o for o in self.__session.query(c)})
        else:
            objs.update({o.__class__.__name__ + '.' + o.id: o for o in self.__session.query(cls)})
        return objs

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()
