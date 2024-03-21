#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    result = {}
    for k in a_dictionary:
        result.update({k: a_dictionary.get(k) * 2})
    return result
