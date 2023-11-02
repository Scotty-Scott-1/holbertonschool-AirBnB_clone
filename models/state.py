#!/usr/bin/python3
"""class State that inherits from BaseModel"""


from models.base_model import BaseModel


class State(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
