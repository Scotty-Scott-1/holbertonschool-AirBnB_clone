#!/usr/bin/python3
"""contains the entry point of the command interpreter"""


import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    class_list = ["BaseModel"]

    def do_quit(self, arg):
        """for quit command interpreter"""
        return True

    def do_EOF(self, arg):
        """Handle the EOF (Ctrl+D) to exit the program"""
        return True

    def emptyline(self):
        pass

    def help_quit(self):
        print("Quit command to exit the program")
        print(' ')

    def help_EOF(self):
        print("Quit command to exit the program")
        print(' ')

    def do_create(self, arg):
        """create an instance of basemodel and print id"""
        args_list = arg.split(" ")
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            storage.new(obj)
            storage.save()
            print(obj.id)

    def do_show(self, arg):
        args_list = arg.split()

        if len(args_list) == 0:
            print("** class name missing **")
        else:
            class_name = args_list[0]
            if class_name not in HBNBCommand.class_list:
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
