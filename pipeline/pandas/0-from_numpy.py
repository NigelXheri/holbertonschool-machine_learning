#!/usr/bin/env python3
"""Creates a pd.DataFrame from a np.ndarray"""
import pandas as pd


def from_numpy(array):
    """Creates a pd.DataFrame from a np.ndarray"""
    cols = [chr(ord('A') + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=cols)