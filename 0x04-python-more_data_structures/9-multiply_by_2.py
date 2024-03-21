#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    result = {}
    for k in a_dictionary:
        result.update({key: a_dictionary.get(key) * 2})
    return result
