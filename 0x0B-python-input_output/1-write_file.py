#!/usr/bin/python3
"""
 contains functiom
that returns the number of lines
of a text file
"""


def number_of_lines(filename=""):
    """
    returns number of lines
    """
    i = 0
    with open(filename, encoding="utf-8") as my_file:
        for line in my_file:
            i += 1
    return (i)
