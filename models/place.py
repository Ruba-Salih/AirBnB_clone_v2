#!/usr/bin/python3
"""
class named Place that inherits from BaseModel and Base
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """A class named Place that represents a place

    Attributes:
        city_id (string): the City id, can't be null
        user_id (string): the User id, can't be null
        name (string): the name of the place, can't be null
        description (str): the description of the place, can be null
        number_rooms (int): the number of rooms of the place, can't be null, default 0
        number_bathrooms (int): the number of bathrooms of the place, can't be null, default 0
        max_guest (int): the maximum number of guests of the place, can't be null, default 0
        price_by_night (int): the price by night of the place, can't be null, default 0
        latitude (float): the latitude of the place, can be null
        longitude (float): the longitude of the place, can be null
    """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    # Relationships
    user = relationship("User", back_populates="places")
    city = relationship("City", back_populates="places")
