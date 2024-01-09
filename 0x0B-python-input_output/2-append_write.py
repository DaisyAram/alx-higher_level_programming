#!/usr/bin/python3
"""function that appends string at the end of a text file"""


def append_write(filename="", text=""):
    """returns the number of characters"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
