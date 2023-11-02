#!/usr/bin/python3
"""class Review that inherits from BaseModel"""


from models.base_model import BaseModel


class review(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
