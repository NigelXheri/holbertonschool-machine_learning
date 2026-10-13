#!/usr/bin/env python3
"""Slices a matrix along specific axes."""


def np_slice(matrix, axes={}):
    """Slice a matrix along specific axes"""
    slices = [slice(None)] * matrix.ndim
    for k, v in axes.items():
        slices[k] = slice(*v)
    return matrix[tuple(slices)]
