#!/usr/bin/python3

from models.base_model import BaseModel

class City(BaseModel):
    """Subclass of BaseModel """
    state_id :str = ""
    name :str = ""
