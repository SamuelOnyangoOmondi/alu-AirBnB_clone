#!/usr/bin/python3
"""
Review Class that inherits from the BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class that inherits from the BaseModel
    """
    user_id = ""
    place_id = ""
    text = ""
