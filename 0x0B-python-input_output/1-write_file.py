#!/usr/bin/python3
"""Defines a function that writes a string to a file."""

def write_file(filename="", text=""):
    """Writes the string to the file."""
    with open(filename, encoding="utf-8") as f:
        f.write(text)
