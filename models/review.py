#!/usr/bin/python3
from models.base_model import BaseModel
"""
Review class
"""


class Review(BaseModel):
    """ Subclass of BaseModel """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
