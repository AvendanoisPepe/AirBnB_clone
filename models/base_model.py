#!/usr/bin/python3
"""
Clase que define el modulo base
"""
from datetime import datetime
import uuid


class BaseModel():
    """
    Como su nombre lo indica es la clase base de este proyecto
    y su funcion es contener tanto los atributos y metodos
    comunes de otras clases.
    """
    def __init__(self, *args, **kwargs):
        """Initialize the instance attributes
        """
        if len(kwargs) > 0 and kwargs is not None:
            for llave, valor in kwargs.items():
                if llave == "created_at" or llave == "updated_at":
                    valor = datetime.strptime(valor, '%Y-%m-%dT%H:%M:%S.%f')
                if llave != "__class__":
                    setattr(self, llave, valor)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models.__init__ import storage
            storage.new(self)

    def __str__(self):
        """Cancela el comportamiento normal de __str__"""
        return ("[{}] ({}) {}".format(type(self).__name__, self.id,
                                      self.__dict__))

    def save(self):
        """Actualiza el atributo update con la hora y fecha actual"""
        self.updated_at = datetime.now()
        from models.__init__ import storage
        storage.save()

    def to_dict(self):
        """Returna un diccionario con todas las clases/valor de la instancia"""
        di = self.__dict__.copy()
        di.update({'__class__': type(self).__name__,
                  'created_at': self.created_at.isoformat(),
                   'updated_at': self.updated_at.isoformat()})
        return di
