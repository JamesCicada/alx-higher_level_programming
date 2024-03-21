#!/usr/bin/python3

def best_score(a_dictionary):
    best_score = 0
    name = ""
    if bool(a_dictionary):
        for key in a_dictionary:
            score = a_dictionary.get(key)
            if score > best_score:
                best_score = score
                name = key
        return name
    else:
        return None
