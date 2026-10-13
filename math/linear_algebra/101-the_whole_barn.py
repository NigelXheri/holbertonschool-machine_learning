#!/usr/bin/env python3
"""Includes add_matrices(mat1, mat2):"""


def add_matrices(mat1, mat2):
    """Adds two matrices element-wise"""
    if get_shape(mat1) != get_shape(mat2):
        return None
    return add_recursive(mat1, mat2)


def add_recursive(mat1, mat2):
    """Recursively adds two nested lists element-wise"""
    if isinstance(mat1, list):
        return [add_recursive(a, b) for a, b in zip(mat1, mat2)]
    return mat1 + mat2


def get_shape(mat):
    """Returns a list with the matrix's dimensions"""
    temp_dimensions = []
    while not isinstance(mat, int):
        temp_dimensions.append(len(mat))
        mat = mat[0]
    return len(temp_dimensions)
