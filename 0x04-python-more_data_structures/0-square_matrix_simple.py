#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    wordA function that computes the square
    value of all integers of a matrix.
    """
    nw_matrix = []
    for col in matrix:
        result = list(map(lambda x: x**2, col))
        nw_matrix.append(result)
    return nw_matrix
