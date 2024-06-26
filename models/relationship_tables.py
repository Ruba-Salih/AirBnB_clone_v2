#!/usr/bin/python3
"""
Module for defining relationship tables
"""
from sqlalchemy import Column, Table, String, ForeignKey
from models.base_model import Base

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
                      Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False),
                      extend_existing=True)
