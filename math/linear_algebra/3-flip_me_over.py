#!/usr/bin/env python3
"""Transposes a given matrix"""


def matrix_transpose(matrix):
    """Returns the transposed matrix of the given argument"""

    if not matrix:
        return []
    return [[row[j] for row in matrix] for j in range(len(matrix[0]))]
