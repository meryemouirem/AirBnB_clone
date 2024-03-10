#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Subclass of BaseModel """
    name: str = ""
