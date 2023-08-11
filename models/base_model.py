#!/usr/bin/python3
""" AirBnB BaseModel"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Definition of the BaseModel """

    def __init__(self, *args, **kwargs):
        """ Initializes a new instance of BaseModel """
        if kwargs:
            self.deserialize(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def deserialize(self, data_dict):
        """ Deserializes attributes from a dictionary """
        date_keys = ["created_at", "updated_at"]
        for key, value in data_dict.items():
            if key in date_keys:
                setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
            elif key == "id":
                self.id = value
            elif key == "__class__":
                self.__class__.__name__ = value
            else:
                setattr(self, key, value)

    def save(self):
        """ updates the instance attribute updated_at with current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing instance attributes """
        instance_dict = self.__dict__.copy()
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        instance_dict["__class__"] = self.__class__.__name__
        return instance_dict

    def __str__(self):
        """ String representation of BaseModel instances """
        classname = self.__class__.__name__
        return "[<{}>] (<{}>) <{}>".format(classname, self.id, self.__dict__)
