#!/usr/bin/python3
"""contains the entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
