#!/usr/bin/python3
"""
Modulo de la clase Review que hereda de BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Clase Review que contiene varios atributos.
    """
    place_id = ""
    user_id = ""
    text = ""
