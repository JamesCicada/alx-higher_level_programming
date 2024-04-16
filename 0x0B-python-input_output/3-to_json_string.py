#!/usr/bin/python3
"""Defines a function for converting a string to JSON."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object."""
    return json.dumps(my_obj)
