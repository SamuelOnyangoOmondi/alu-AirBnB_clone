#!/usr/bin/python3
"""
Place Class that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place Class that inherits from BaseModel
    """
    name = ""
    city_id = ""
    description = ""
    user_id = ""
    number_bathrooms = 0
    number_rooms = 0
    price_by_night = 0
    max_guest = 0
    longitude = 0.0
    latitude = 0.0
    amenity_ids = []
