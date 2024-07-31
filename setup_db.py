#!/usr/bin/python3
"""Script to set up the database"""

from models import storage
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

def setup_database():
    """Set up the database with the tables defined in models."""
    # Create all tables
    Base.metadata.create_all(storage._DBStorage__engine)

if __name__ == "__main__":
    setup_database()
