#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
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
    class_list = ["BaseModel", "User", "State", "Review",
                  "Place", "City", "Amenity"]

    def do_quit(self, arg):
        """for quit command interpreter"""
        return True

    def do_EOF(self, arg):
        """Handle the EOF (Ctrl+D) to exit the program"""
        return True

    def emptyline(self):
        """skip empty line"""
        pass

    def help_quit(self):
        """quit"""
        print("Quit command to exit the program")
        print(' ')

    def help_EOF(self):
        """help for eof"""
        print("Quit command to exit the program")
        print(' ')

    def do_create(self, arg):
        """create an instance of basemodel and print id"""
        args_list = arg.split()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.class_list:
            """elif args_list[0] not in HBNBCommand.class_list:"""
            print("** class doesn't exist **")
        else:
            if args_list[0] == "BaseModel":
                obj = BaseModel()
            elif args_list[0] == "User":
                obj = User()
            elif args_list[0] == "State":
                obj = State()
            elif args_list[0] == "Review":
                obj = Review()
            elif args_list[0] == "Place":
                obj = Place()
            elif args_list[0] == "City":
                obj = City()
            elif args_list[0] == "Amenity":
                obj = Amenity()

            storage.new(obj)
            storage.save()
            print(obj.id)

    def do_show(self, arg):
        """show an instance"""
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

    def do_destroy(self, arg):
        """delete an instance"""
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
                    key = "{}.{}".format(class_name, instance_id)
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        my_list = []
        args_list = arg.split()
        if len(args_list) == 0:
            for ob in storage.all():
                my_list.append(print(storage.all()[ob]))
            print(my_list)
        elif len(args_list) == 1:
            if args_list[0] in HBNBCommand.class_list:

                for ob in storage.all():
                    if args_list[0] == "BaseModel":
                        if ob[:9] == "BaseModel":
                            my_list.append(print(storage.all()[ob]))
                    if args_list[0] == "City":
                        if ob[:4] == "City":
                            my_list.append(print(storage.all()[ob]))
                    if args_list[0] == "User":
                        if ob[:4] == "User":
                            my_list.append(print(storage.all()[ob]))
                    if args_list[0] == "State":
                        if ob[:5] == "State":
                            my_list.append(print(storage.all()[ob]))
                    if args_list[0] == "Review":
                        if ob[:6] == "Review":
                            my_list.append(print(storage.all()[ob]))
                    if args_list[0] == "Place":
                        if ob[:5] == "Place":
                            my_list.append(print(storage.all()[ob]))
                    if args_list[0] == "Amenity":
                        if ob[:7] == "Amenity":
                            my_list.append(print(storage.all()[ob]))

            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        args_list = arg.split()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            class_name = args_list[0]
            instance_id = args_list[1]
            key = "{}.{}".format(class_name, instance_id)
            if key not in storage.all():
                print("** no instance found **")
                return
            else:
                instance = storage.all()[key]

            if len(args_list) < 3:
                print("** attribute name missing **")
                return
            else:
                attr_name = args_list[2]
                if len(args_list) < 4:
                    print("** value missing **")
                else:
                    value = args_list[3]
                    if hasattr(instance, attr_name):
                        setattr(instance, attr_name, value)
                        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
