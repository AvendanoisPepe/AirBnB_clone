#!/usr/bin/python3
"""
Modulo de la clase City que hereda de BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Clase City que contiene el atributo name y state_id.
    """
    state_id = ""
    name = ""
