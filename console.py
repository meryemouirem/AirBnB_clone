#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

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
        quit command to exit the program
        """
        return True

    def emptyline(self) -> bool:
        """ Do nothing upon a new lie """
        pass

    def do_create(self, arg):
        """ creates new instance of a BaseModel, and save it into
         a JSON file
         """
        try:
            obj = eval(arg)()
            obj.save()
        except SyntaxError:
            print("** class missing **")
        except NameError:
            print("** class doesn't exist **")
        else:
            print(obj.id)



if __name__ == "__main__":
    HBNBCommand().cmdloop()
