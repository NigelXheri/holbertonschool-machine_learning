#!/usr/bin/env python3
"""Contains cat_matrices2D"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two 2D matrices"""
    if not axis:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [mat1[i] if i in range(len(mat1)) else mat2[i-len(mat1)]
                for i in range(len(mat1)+len(mat2))]
    else:
        if len(mat1) != len(mat2):
            return None
        return [[mat1[i][j] if j in range(len(mat1[0]))
                 else mat2[i][j-len(mat1[0])]
                for j in range(len(mat1[0])+len(mat2[0]))]
                for i in range(len(mat1))]
