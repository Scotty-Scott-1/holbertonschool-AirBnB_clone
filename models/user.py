#!/usr/bin/python3
"""class User that inherits from BaseModel"""


from base_model import BaseModel


class User(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = str()
        self.passord = str()
        self.firt_name = str()
        self.last_name = str()
