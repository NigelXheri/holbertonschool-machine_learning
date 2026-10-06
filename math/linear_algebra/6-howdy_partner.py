#!/usr/bin/env python3
"""Contains cat_arrays"""


def cat_arrays(arr1, arr2):
    """Concatenates two arrays"""
    return [arr1[i] if i in range(len(arr1)) else arr2[i-len(arr1)]
            for i in range(len(arr1)+len(arr2))]
