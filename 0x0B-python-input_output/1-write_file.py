#!/usr/bin/python3
"""Defines a function that writes a new file."""

def write_file(filename="", text=""):
    """Writes a new utf-8 file with content (text arg)"""
    with open(filename, encoding="utf-8" as f:
            f.write(text)

