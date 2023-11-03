#!/usr/bin/python3
"""contains the entry point of the command interpreter"""


import cmd
import shlex
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "Review": Review,
        "Place": Place,
        "City": City,
        "Amenity": Amenity
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of file command to exit the program"""
        return True

    def emptyline(self):
        """skip empty line"""
        pass

    def do_create(self, arg):
        """create an instance of class and print id"""
        args_list = shlex.split(arg)
        if len(args_list) == 0:
            print("** class name missing **")
            return
        class_name = args_list[0]
        if class_name not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.class_dict[class_name]()
            storage.new(obj)
            storage.save()
            print(obj.id)

    def do_show(self, arg):
        """show an instance"""
        args_list = shlex.split(arg)

        if len(args_list) == 0:
            print("** class name missing **")
        else:
            class_name = args_list[0]
            if class_name not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                instance_id = args_list[1]
                key = "{}.{}".format(class_name, instance_id)
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    instance = storage.all()[key]
                    print(instance)

    def do_destroy(self, arg):
        """delete an instance"""
        args_list = shlex.split(arg)

        if len(args_list) == 0:
            print("** class name missing **")
        else:
            class_name = args_list[0]
            if class_name not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                instance_id = args_list[1]
                key = "{}.{}".format(class_name, instance_id)
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        my_list = []
        args_list = shlex.split(arg)
        if len(args_list) == 0:
            for ob in storage.all().values():
                my_list.append(ob.__str__())
            print(my_list)
        elif len(args_list) == 1:
            if args_list[0] in HBNBCommand.class_dict:
                for ob in storage.all().values():
                    if args_list[0] in ob.__str__():
                        my_list.append(ob.__str__())
                print(my_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        args_list = shlex.split(arg)

        if len(args_list) == 0:
            print("** class name missing **")
            return
        class_name = args_list[0]
        if class_name not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        elif len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        instance = storage.all()[key]

        if len(args_list) < 3:
            print("** attribute name missing **")
            return
        else:
            attr_name = args_list[2]
            if len(args_list) < 4:
                print("** value missing **")
                return

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
            else:
                print("** Invalid value for the attribute **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
