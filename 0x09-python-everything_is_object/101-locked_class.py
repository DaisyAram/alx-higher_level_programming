#!/usr/bin/python3
class LockedClass:
    def __init__(self):
        # You can add any instance attribute here.
        self.first_name = None

    def __setattr__(self, name, value):
        if name == 'first_name' or hasattr(self, name):
            super().__setattr__(name, value)
        else:
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
