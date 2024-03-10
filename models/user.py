#!/usr/bin/python3

from models.base_model import BaseModel

"""
User class
"""


class User(BaseModel):
    """User credentails """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
