#!/usr/bin/python3
"""define inherited list"""


class MyList(list):
    """implemet sorted printing for builtin list class"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
