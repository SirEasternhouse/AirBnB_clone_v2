#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class for storing state information """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        # For database storage, define a relationship to City
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete-orphan"
        )
    else:
        @property
        def cities(self):
            """Getter attribute for file storage.

            Returns the list of City instances where
            state_id equals the current State.id
            """
            from models import storage
            from models.city import City
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
