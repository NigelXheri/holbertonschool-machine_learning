#!/usr/bin/env python3
"""Contains from_numpy"""
import pandas as pd


def from_numpy(array):
    """Creates a Pandas DataFrame from a Numpy ndarray"""
    return pd.DataFrame(array)
