#!/usr/bin/python3
<<<<<<< HEAD
=======
"""The Console file for AirBnB"""
>>>>>>> 67a02826cdd52eef8fb9c180b13b32dc0ca5d827
import cmd
import models
from models.base_model import BaseModel
<<<<<<< HEAD
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
from models.city import City
=======
>>>>>>> 67a02826cdd52eef8fb9c180b13b32dc0ca5d827


class HBNBCommand(cmd.Cmd):
    """The prompt"""
    prompt = '(hbnb) '

<<<<<<< HEAD
    def quit(self, arg):
        """Quit the command interpreter"""
        return True

    def EOF(self, arg):
        """Exit on EOF(Ctrl-D)"""
        print()
=======
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
>>>>>>> 67a02826cdd52eef8fb9c180b13b32dc0ca5d827
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

<<<<<<< HEAD
    def create(self, arg):
=======
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, User,
        State, City, Amenity, Place, or Review"""
>>>>>>> 67a02826cdd52eef8fb9c180b13b32dc0ca5d827
        if not arg:
            print("** class name missing **")
        elif arg not in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
        else:
<<<<<<< HEAD
            try:
                if arg == "BaseModel":
                    new_instance = BaseModel()
                elif arg == "User":
                    new_instance = User()
                elif arg == "State":
                    new_instance = State()
                elif arg == "City":
                    new_instance = City()
                elif arg == "Amenity":
                    new_instance = Amenity()
                elif arg == "Place":
                    new_instance = Place()
                elif arg == "Review":
                    new_instance = Review()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def show(self, arg):
        """Print string representation of an instance"""
=======
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
        """Prints the string representation of an instance"""
>>>>>>> 67a02826cdd52eef8fb9c180b13b32dc0ca5d827
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in models.storage.all().keys():
                print(storage.all()[key])
            else:
                print("** no instance found **")

<<<<<<< HEAD
    def destroy(self, arg):
        """Delete an instance based on class name and id"""
=======
    def do_destroy(self, arg):
        'Deletes an instance'
>>>>>>> 67a02826cdd52eef8fb9c180b13b32dc0ca5d827
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']:
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

<<<<<<< HEAD
    def all(self, arg):
        """Prints all string representations of instances"""
        args = arg.split()
        models_storage = BaseModel.load()
        if not arg:
            for key in models_storage:
                print(models_storage[key])
        elif args[0] not in ["BaseModel", "User"]:
=======
    def do_all(self, arg):
        """Prints all instances"""
        if arg != 'BaseModel' and len(arg) > 0:
>>>>>>> 67a02826cdd52eef8fb9c180b13b32dc0ca5d827
            print("** class doesn't exist **")
        else:
            for value in models.storage.all().values():
                print(value)

<<<<<<< HEAD
    def update(self, arg):
        """Update an instance based on class name and id"""
=======
    def do_update(self, arg):
        """Updates an instance"""
>>>>>>> 67a02826cdd52eef8fb9c180b13b32dc0ca5d827
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
<<<<<<< HEAD
        elif args[0] not in ["BaseModel", "User"]:
=======
        elif args[0] not in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']:
>>>>>>> 67a02826cdd52eef8fb9c180b13b32dc0ca5d827
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

