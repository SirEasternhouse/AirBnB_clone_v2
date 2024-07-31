#!/usr/bin/python3
""" Data base storage """

from models.base_model import BaseModel, Base
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


classes = {
    'BaseModel': BaseModel,
    'User': User,
    # Add other model classes here if necessary
}


class DBStorage:
    """This class manages storage of hbnb models in MySQL"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the database connection"""
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        HBNB_ENV = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
            pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects depending on the class name"""
        if cls:
            return {obj.to_dict()['__class__'] + '.' + obj.id: obj
                    for obj in self.__session.query(cls).all()}
        else:
            objects = {}
            for class_name in classes:
                for obj in self.__session.query(classes[class_name]).all():
                    objects[obj.to_dict()['__class__'] + '.' + obj.id] = obj
            return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the session"""
        self.__session.remove()
