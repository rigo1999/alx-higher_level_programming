#!/usr/bin/python3
"""
 function that appends
a string at the end of a text file and
returns number of characters added
"""


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return (my_file.write(str(text)))
