#!/usr/bin/python3
"""
class named place that inharits from BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey


class Place(BaseModel, Base):
    """Inherits from BaseModel class

     Attributes:
        city_id (string): the City id
        user_id (string): the User id
        name (string): the name of the place.
        description (str): the description of the place
        number_rooms (int):the  number of rooms of the place
        number_bathrooms (int):the  number of bathrooms of the place
        max_guest (int):the  maximum number of guests of the place
        price_by_night (int): the price by night of the place
        latitude (float): the latitude of the place
        longitude (float): the longitude of the place
        amenity_ids (list): the list of Amenity ids

    """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("user.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0,nullable=False)
    number_bathrooms = Column(Integer, default=0,nullable=False)
    max_guest = Column(Integer, default=0,nullable=False)
    price_by_night = Column(Integer, default=0,nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
