#!/usr/bin/python3
"""This script defines a function for retrieving object attributes."""


def lookup(obj):
    """Retrieve and return a list of available attributes for the given object."""
    return dir(obj)
