#!/usr/bin/python3
"""
State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """subclass BaseModel"""

    name: str = ""
