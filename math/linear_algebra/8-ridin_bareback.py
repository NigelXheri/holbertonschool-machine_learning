#!/usr/bin/env python3
"""Module for matrix multiplication."""


def mat_mul(mat1, mat2):
    """Multiply two 2D matrices and return a new matrix.

    Returns:
        A new 2D list representing the product of mat1 and mat2,
        or None if the matrices cannot be multiplied.
    """
    if not mat1 or not mat2:
        return None

    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])

    if cols1 != rows2:
        return None

    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            total = 0
            for k in range(cols1):
                total += mat1[i][k] * mat2[k][j]
            row.append(total)
        result.append(row)

    return result