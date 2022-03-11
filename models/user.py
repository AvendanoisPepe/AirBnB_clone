#!/usr/bin/python3
"""modulo que administra la clase usuario"""
from models.base_model import BaseModel


class User(BaseModel):
    """Clase que representa usuario"""

    email = str()
    password = str()
    first_name = str()
    last_name = str()

    def __init__(self, *args, **kwargs):
        """Method Init"""
        super().__init__(*args, **kwargs)
