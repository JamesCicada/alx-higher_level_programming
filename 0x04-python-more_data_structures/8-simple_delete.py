#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    result = a_dictionary
    if key in result:
        result.pop(key)
    return result
