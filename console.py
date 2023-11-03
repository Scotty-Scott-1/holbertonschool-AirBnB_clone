#!/usr/bin/python3
"""contains the entry point of the command interpreter"""


import cmd
import shlex
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "State", "Review", "Place",
                  "City", "Amenity"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handle the EOF (Ctrl+D) to exit the program"""
        return True

    def emptyline(self):
        """Skip empty line"""
        pass

    def do_create(self, arg):
        """Create an instance of BaseModel and print its ID"""
        args_list = shlex.split(arg)
        if not args_list:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return

        if len(args_list) == 1:
            print("** value missing **")
            return

        obj = eval(class_name)()
        for arg in args_list[1:]:
            if "=" not in arg:
                print("** Invalid attribute format**")
                return

            attr_name, attr_value = arg.split('=')
            if not attr_value:
                print("** value missing **")
                return

            if attr_value[0] == '"' and attr_value[-1] == '"':
                attr_value = attr_value[1:-1]

            if hasattr(obj, attr_name):
                attr_type = type(getattr(obj, attr_name))
                try:
                    if attr_type == int:
                        attr_value = int(attr_value)
                    elif attr_type == float:
                        attr_value = float(attr_value)
                except (ValueError, TypeError):
                    print("** Invalid value for the attribute **")
                    return

                setattr(obj, attr_name, attr_value)

        storage.new(obj)
        storage.save()
        print(obj.id)

    def do_show(self, arg):
        """Show an instance"""
        args_list = shlex.split(arg)
        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            instance_id = args_list[1]
            key = "{}.{}".format(args_list[0], instance_id)
            if key not in storage.all():
                print("** no instance found **")
            else:
                instance = storage.all()[key]
                print(instance)

    def do_destroy(self, arg):
        """Delete an instance"""
        args_list = shlex.split(arg)
        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            instance_id = args_list[1]
            key = "{}.{}".format(args_list[0], instance_id)
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """List all instances or instances of a specific class"""
        my_list = []
        args_list = shlex.split(arg)
        if not args_list:
            for obj in storage.all().values():
                my_list.append(obj.__str__())
            print(my_list)
        elif args_list[0] in HBNBCommand.class_list:
            for obj in storage.all().values():
                if obj.__class__.__name__ == args_list[0]:
                    my_list.append(obj.__str__())
            print(my_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance's attributes"""
        args_list = shlex.split(arg)
        if not args_list:
            print("** class name missing **")
            return
        elif args_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        elif len(args_list) < 2:
            print("** instance id missing **")
            return

        class_name = args_list[0]
        instance_id = args_list[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        instance = storage.all()[key]
        if len(args_list) < 3:
            print("** attribute name missing **")
            return
        elif len(args_list) < 4:
            print("** value missing **")
            return

        attr_name = args_list[2]
        value = args_list[3]
        if attr_name in ["id", "created_at", "updated_at"]:
            return

        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            try:
                if attr_type == int:
                    value = int(value)
                elif attr_type == float:
                    value = float(value)
            except (ValueError, TypeError):
                print("** Invalid value for the attribute **")
                return

            setattr(instance, attr_name, value)
            instance.updated_at = datetime.now()
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
