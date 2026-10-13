#!/usr/bin/env python3
"""Contains function np_cat"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenate two matrices across the specified axis"""

    return np.concatenate((mat1, mat2), axis=axis)
