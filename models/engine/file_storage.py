#!/usr/bin/python3
"""
Definimos el modulo FileStorage
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """
    Esta clase cumple con el objetivo de Serialización-
    Deserialización un archivo .json.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returna el diccionario objetos"""
        self.reload()
        return (self.__objects)

    def new(self, obj):
        """
        Crea una nueva clave (class.id) y valor
        (diccionario de atributos de instancia)
        """
        clave = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[clave] = obj

    def save(self):
        """
        Serializa __objetos en el archivo JSON
        Agrega todas las clases y valores a __objets para
        guardarlo en un archivo .json
        """
        diccionarioCarlos = {}
        for clave, valor in FileStorage.__objects.items():
            diccionarioCarlos[clave] = valor.to_dict()

        with open(self.__file_path, "w", encoding='utf-8') as Jsonfile:
            json.dump(diccionarioCarlos, Jsonfile)

    def reload(self):
        """
        Deserializa el archivo JSON a __objects
        Configura todas las claves y valores y recrea las instancias
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as pepe:
                objeto = json.load(pepe)
            for clave, val in objeto.items():
                FileStorage.__objects[clave] = eval(val["__class__"])(**val)
        else:
            return

    def classes(self):
        """Returna un diccionario de clases para verificar
        """
        classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                   "City": City, "Place": Place, "Review": Review,
                   "State": State}
        return classes
