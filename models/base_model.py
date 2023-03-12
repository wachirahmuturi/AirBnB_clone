#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

"""
Module Basemodel
Parent of all classes
"""


class BaseModel:
    """
    Base class for AirBnB clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes attributes: random uuid, 2 dates-created_at & updated_at
        """

        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    self.id = str(uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                    models.storage.new(self)

    def __str__(self):
        """
        Return a string of the information of the model
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        Return string representation
        """
        return (self.__str__())

    def save(self):
        """
        Update an instance with updated time and save to a serialized file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary with string formats of times;
        add class information to the dictionary
        """
        dictionary = {}
        dictionary["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dictionary[k] = v.isoformat()
            else:
                dictionary[k] = v
        return dictionary
