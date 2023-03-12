#!/usr/bin/python3
""" User class"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    """
    User details including email, password, first_name and last_name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
