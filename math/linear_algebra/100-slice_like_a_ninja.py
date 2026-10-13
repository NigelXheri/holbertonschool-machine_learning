#!/usr/bin/env python3
"""Slices a matrix along specific axes."""


def np_slice(matrix, axes={}):
    """Slice a matrix along specific axes"""

    slices = [slice(None)] * matrix.ndim
    for axis, value in axes.items():
        value = tuple(value) + (None,) * (3 - len(value))
        slices[axis] = slice(*value)
    return matrix[tuple(slices)]