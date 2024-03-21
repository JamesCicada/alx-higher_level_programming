#!/usr/bin/python3

def roman_to_int(roman_string):
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,"D": 500, "M": 1000}
    result = 0
    for ind, i in enumerate(roman_string):
        i_pos = list(romans.keys()).index(i)
        if ind < len(roman_string) - 1:
            pos = list(romans.keys()).index(roman_string[ind + 1])
        else:
            pos = 0
        if pos > i_pos:
            result = result - romans.get(i)
            pos = i_pos
        else:
            result = result + romans.get(i)
            pos = i_pos
    return result
