#!/usr/bin/python3
"""
class named Amenity that inherits from BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.relationship_tables import place_amenity

class Amenity(BaseModel, Base):
    """Inherits from BaseModel class

    Attributes:
        name (string): the name of the amenity
    """

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    place_amenities = relationship("Place", secondary=place_amenity, viewonly=False, back_populates="amenities")
