#!/usr/bin/python3
"""function that creates an object from JSON file"""


import json


def load_from_json_file(filename):
    """creates an object"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
