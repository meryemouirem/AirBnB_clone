#!/usr/bin/python3

from models.base_model import BaseModel

"""
City class
"""


class City(BaseModel):
    """Subclass of BaseModel """
    state_id: str = ""
    name: str = ""
