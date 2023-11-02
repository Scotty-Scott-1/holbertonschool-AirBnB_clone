#!/usr/bin/python3
"""class Amenity that inherits from BaseModel"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
