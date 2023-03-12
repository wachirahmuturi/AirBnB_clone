#!/usr/bin/python3
"""File Storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes and Deserializes json files"""

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"Basemodel": BaseModel, "User": User, "Place": Place, 
                  "State": State, "City": City, "Amenity": Amenity, "Review": Review}

    def all(self):
        """Return dictionary of <class>.<id> : object instance"""
        return self.__objects

    def new(self, obj):
        """Add new obj to existing dictionary of instamnces"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Save obj dictionaries to json file"""
        my_dict = {}

        for key, obj in self.__object.items():
            my_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """if json file exists, convert obj dicts back to instances"""
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
