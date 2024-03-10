#!/usr/bin/python3
"""
Parent Class to all other children classes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Parent class for the entire project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        save(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """initialize a BaseModel instance """
        if not kwargs or len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.save(self)
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    iso_format = datetime.fromisoformat(value)
                    setattr(self, key, iso_format)
                else:
                    setattr(self, key, value)

    def __str__(self):
        """String representation of BaseModel """
        str_ = "[{}] ({}) {}"
        str_ = str_.format(self.__class__.__name__, self.id, self.__dict__)
        return str_

    def save(self):
        """public method that updates instance attribute
            update_at with the current date
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict_ = self.__dict__.copy()
        dict_["__class__"] = self.__class__.__name__
        dict_["created_at"] = self.created_at.isoformat()
        dict_["updated_at"] = self.updated_at.isoformat()
        return dict_
