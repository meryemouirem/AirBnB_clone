#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
"""
Prent Class to all other children clases
"""

class BaseModel:
    """ Parent class for the entire project 
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        save(self)
        __repr__(self)
        to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        """ initialize a BaseModel instance """
        self.id = uuid4()
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime("%Y-%m-%dT%H:%M:%S.%f", kwargs["created_at"])
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime("%Y-%m-%dT%H:%M:%S.%f", kwargs["updated_at"])
                elif "__class__" == key:
                    pass
                