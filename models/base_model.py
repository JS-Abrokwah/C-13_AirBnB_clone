#!/usr/bin/python3
""" Base Model Module """
from uuid import uuid4
from datetime import datetime
from models import storage  # Import the storage object


class BaseModel:
    """Base Model Class"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  # Use the storage object

    def __str__(self):
        """Return string representation of BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save the current instance"""
        self.updated_at = datetime.now()
        storage.save()  # Use the storage object

    def to_dict(self):
        """Return dictionary representation of BaseModel"""
        base_dict = dict(self.__dict__)
        base_dict["__class__"] = self.__class__.__name__
        base_dict["created_at"] = base_dict["created_at"].isoformat()
        base_dict["updated_at"] = base_dict["updated_at"].isoformat()
        return base_dict
