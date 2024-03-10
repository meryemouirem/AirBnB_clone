#!/usr/bin/python3
"""
User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User credentails """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
