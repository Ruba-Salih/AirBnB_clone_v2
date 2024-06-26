#!/usr/bin/python3
"""
class named city that inherits from BaseModel and Base
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """A class named City that represents a city

    Attributes:
        state_id (string): state id, can't be null, foreign key to states.id
        name (string): name of the city, can't be null
        places (relationship): The relationship to Place objects
    """

    __tablename__ = 'cities'

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    places = relationship("Place", backref="city", cascade="all, delete")
