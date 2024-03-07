#!/usr/bin/python3
import cmd

"""
The Command line interface of the entire application
"""


class HBNBCommand(cmd.Cmd):
    """
    The command line interface of the application

    """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """
        End Of File
        """
        return True

    def do_quit(self, arg):
        """
        quit command to exit the shell
        """
        return True

    def emptyline(self) -> bool:
        """ Do nothing upon a new lie """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
