#!/usr/bin/python3
"""
Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Subclass of BaseModel """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
