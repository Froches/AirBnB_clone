#!/usr/bin/python3
"""The Console file for AirBnB"""
import cmd
import sys
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """The prompt"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, User,
        State, City, Amenity, Place, or Review
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
        elif arg not in ['BaseModel', 'User', 'State',
                         'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
        else:
            if arg == 'BaseModel':
                new_instance = BaseModel()
            elif arg == 'User':
                new_instance = User()
            elif arg == 'State':
                new_instance = State()
            elif arg == 'City':
                new_instance = City()
            elif arg == 'Amenity':
                new_instance = Amenity()
            elif arg == 'Place':
                new_instance = Place()
            elif arg == 'Review':
                new_instance = Review()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        Usage: show <class_name> <instance_id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ['BaseModel', 'User', 'State',
                             'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in models.storage.all().keys():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ['BaseModel', 'User', 'State',
                             'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all().keys():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances"""
        if arg != 'BaseModel' and len(arg) > 0:
            print("** class doesn't exist **")
        else:
            for value in models.storage.all().values():
                print(value)

    def do_update(self, arg):
        """Updates an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ['BaseModel', 'User', 'State',
                             'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in models.storage.all().keys():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                setattr(storage.all()[key], args[2], args[3])
                storage.all()[key].save()

    def default(self, line):
        """
        Method called on an input line when
        the command prefix is not recognized.
        """
        if len(line.split(".")) != 2:
            print("*** Unknown syntax: {}".format(line))
            return
        args = line.split(".")
        class_name = args[0]
        command = args[1]
        if command == "all()":
            self.do_all(class_name)
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
