#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage

"""
Parent Class to all other children classes
"""


class BaseModel:
    """ Parent class for the entire project 
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        save(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """ initialize a BaseModel instance """
        if kwargs:
            for key in kwargs.keys():
                if key == "created_at":
                    self.created_at = datetime.strptime("%Y-%m-%dT%H:%M:%S.%f", kwargs["created_at"])
                elif key == "updated_at":
                    self.updated_at = datetime.strptime("%Y-%m-%dT%H:%M:%S.%f", kwargs["updated_at"])
                elif "__class__" == key:
                    pass
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ String representation of BaseModel """
        str_ = "[{}] ({}) {}"
        str_ = str_.format(self.__class__.__name__, self.id, self.__dict__)
        return str_

    def save(self):
        """ public method that updates instance attribute
            update_at with the current date
         """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict_ = self.__dict__.copy()
        dict_["__class__"] = self.__class__.__name__
        dict_["created_at"] = self.created_at.isoformat()
        dict_["updated_at"] = self.updated_at.isoformat()
        return dict_
