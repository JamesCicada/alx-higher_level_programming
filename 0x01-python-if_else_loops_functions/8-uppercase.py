#!/usr/bin/python3

def uppercase(str):
    output = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        output += char
    print("{}".format(output))
