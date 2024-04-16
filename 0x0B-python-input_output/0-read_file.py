#!/usr/bin/python3

'''Reads and Prints the content of a file''' 
def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
