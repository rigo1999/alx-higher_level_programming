#!/usr/bin/python3
"""
creation  MyList class
"""


class MyList(list):
    """a subclass of list class"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
