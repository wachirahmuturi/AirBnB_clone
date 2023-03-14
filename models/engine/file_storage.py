#!/usr/bin/python3
"""
Here you can find the FileStorage Class
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
           "City": City, "Place": Place, "Review": Review, "State": State}


class FileStorage:
    """that serializes instances to a JSON file and deserializes
    JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in FileStorage.__objects:
            json_objects[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path)"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                js = json.load(f)
            for key in js:
                FileStorage.__objects[key] = classes[js[key]
                                                     ["__class__"]](**js[key])
        except Exception:
            pass
