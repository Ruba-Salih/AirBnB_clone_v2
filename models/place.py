#!/usr/bin/python3
"""
class named Place that inherits from BaseModel and Base
"""
<<<<<<< HEAD
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """A class named Place that represents a place
=======
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


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
>>>>>>> a39e65add451a0b9600f33df42b0fba4c78da129

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
<<<<<<< HEAD
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
=======

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")
        amenities = relationship("Amenity", secondary='place_amenity',
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
        @property
        def amenities(self):
            """Get Amenities."""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, value):
            """ Appends amenity ids to the attribute """
            if type(value) == Amenity and value.id not in self.amenity_ids:
                self.amenity_ids.append(value.id)
>>>>>>> a39e65add451a0b9600f33df42b0fba4c78da129
