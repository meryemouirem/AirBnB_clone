#!/usr/bin/python3
import json
from models.base_model import BaseModel

"""
File storage of created instances
"""


class FileStorage:
    """
     File storage class that serializes instances
     to a JSON file, and deserializes JSON file to instances

     """
    __file_path: str = "file.json"
    __objects: dict = {}
    __classes = {"BaseModel": BaseModel}

    def all(self):
        """ Returns the dictionary objects """
        return self.__objects

    def new(self, obj: object):
        """
        Sets in __objects the obj with key
         <obj class name>.id
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path:__file_path) """
        obj_dict = {}
        for k, ob_ in self.__objects.items():
            obj_dict[k] = ob_.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
        except FileNotFoundError:
            pass
        else:
            for key, value in obj_dict.items():
                obj = FileStorage.__classes[value["__class__"]](**value)
                self.__objects[key] = obj





