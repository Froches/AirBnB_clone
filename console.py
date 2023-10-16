#!/usr/bin/python3
"""Command interpreter for AirBnB project"""
import cmd
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """AirBnB console file"""

    prompt = "(hbnb) "

    def quit(self, arg):
        """Quit the command interpreter"""
        return True

    def EOF(self, arg):
        """Exit on EOF(Ctrl-D)"""
        print()
        return True

    def emptyline(self):
        """Empty command - do nothing"""
        pass

    def create(self, arg):
        """Creates new instance"""
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        else:
            try:
                if arg == "BaseModel":
                    new_instance = BaseModel()
                else:
                    new_insstance = User()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def show(self, arg):
        """Print string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            models_storage = BaseModel.load()
            key = "{}.{}".format(args[0], args[1])
            if key in models_storage:
                print(models_storage[key])
            else:
                print("** no instance found **")

    def destroy(self, arg):
        """Delete an instance based on class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            models_storage = BaseModel.load()
            key = "{}.{}".format(args[0], args[1])
            if key in models_storage:
                del models_storage[key]
                BaseModel.save(models_storage)
            else:
                print("** no instance found **")

    def all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        models_storage = BaseModel.load()
        if not arg:
            for key in models_storage:
                print(models_storage[key])
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")

    def update(self, arg):
        """Update an instance based on class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attributes name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            models_storage = BaseModel.load()
            key = "{}.{}".format(args[0], args[1])
            if key in models_storage:
                obj = models_storage[key]
                attribute_name = args[2]
                attribute_value = args[3]

                if hasattr(obj, attribute_name):
                    attribute_type = type(getattr(obj, attribute_name))
                    if attribute_type is str:
                        attribute_value = attribute_value.strip('"')
                    elif attribute_type is int:
                        attribute_value = int(attribute_value)
                    elif attribute_value is float:
                        attribute_value = float(attribute_value)
                    setattr(obj, attribute_name, attribute_value)
                    obj.save()
                else:
                    print("** attribute name doesn't exist **")
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
