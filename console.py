#!/usr/bin/python3
"""Módulo para el punto de entrada del intérprete de comandos."""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    Clase para el interprete del comando para manipular la consola.
    """
    prompt = '(hbnb) '
    list_class = ['BaseModel', 'User', 'Amenity', 'City',
                  'Place', 'Review', 'State']

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        sys.exit(0)

    def emptyline(self):
        """
        si pasan un ina linea vacia seguida de un enter no hace nada
        """
        pass

    def do_EOF(self, arg):
        """
        comando para salir una vez leido todo
        """
        sys.exit(0)

    def do_create(self, arg):
        """
        Crea una nueva instancia si los argumentos son validos.
        """
        argum = arg.split()
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        elif storage.classes():
            nuevaInstancia = eval("{}()".format(argum[0]))
            nuevaInstancia.save()
            print(nuevaInstancia.id)

    def do_show(self, arg):
        """
        Imprime la representancion de la cadena de una instancia
        """
        argum = arg.split(' ')
        if arg == "" or arg is None:
            print("** class name missing **")
        elif argum[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(argum) < 2:
            print("** instance id missing **")
        else:
            llave = "{}.{}".format(argum[0], argum[1])
            if llave not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[llave])

    def do_destroy(self, arg):
        """
        Elimina una instancia según el nombre de la clase y el id.
        """
        argum = arg.split(' ')
        if arg == "" or arg is None:
            print("** class name missing **")
        elif argum[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(argum) < 2:
            print("** instance id missing **")
        else:
            llave = "{}.{}".format(argum[0], argum[1])
            if llave not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(llave)
                storage.save()

    def do_update(self, arg):
        """
        Actualiza una instancia basada en el nombre de
        la clase y la identificación agregando o actualizando
        el atributo.
        """
        argum = arg.split()
        args_size = len(argum)

        if arg == "" or arg is None:
            print("** class name missing **")
        elif argum[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(argum) < 2:
            print("** instance id missing **")
        elif len(argum) == 2:
            print("** attribute name missing **")
        elif len(argum) == 3:
            print("** value missing **")
        else:
            llave = "{}.{}".format(argum[0], argum[1])
            argum[3] = int(argum[3]) if argum[3][0] != '"' else argum[3][1:-1]
            if llave in storage.all().keys():
                val = storage.all()[llave]
                val.__dict__[argum[2]] = argum[3]
                storage.all()[llave] = val
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not
        on the class name.do_all
        """
        args = arg.split()
        list_strings = []
        objects = storage.all()
        for key in objects.keys():
            value = objects.get(key)
            if args:
                if args[0] in self.list_class:
                    if value.__class__.__name__ == args[0]:
                        list_strings.append(value.__str__())
                else:
                    print("** class doesn't exist **")
                    return
            else:
                list_strings.append(objects[key].__str__())
        print(list_strings)

    def default(self, arg):
        storage.reload()
        to_default = arg.split("(", 1)
        if len(to_default) > 0:
            to_arguments = to_default[1].replace("\"", "", 2)
            to_arguments = (
                to_arguments if ")" not in to_arguments
                else to_arguments.replace(")", "")
            )
            to_default = to_default[0].split(".", 1)
            if len(to_default) > 0:
                if to_default[1] == "all":
                    return self.do_all(to_default[0])
                elif to_default[1] == "count":
                    return self.count(to_default[0])
                elif to_default[1] == "show":
                    return self.do_show(to_default[0] + " " + to_arguments)
                elif to_default[1] == "destroy":
                    return self.do_destroy(to_default[0] + " " + to_arguments)
                else:
                    return super().default(arg)
        else:
            return super().default(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
