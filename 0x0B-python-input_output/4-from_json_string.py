#!/usr/bin/python3
"""function that returns abn object representation by a JSON string"""


import json


def from_json_string(my_str):
    """return object rep by json"""
    return json.loads(my_str)
