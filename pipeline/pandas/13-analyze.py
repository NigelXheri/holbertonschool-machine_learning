#!/usr/bin/env python3
"""Computes descriptive statistics for a pd.DataFrame"""


def analyze(df):
    """Takes a pd.DataFrame and:
        Computes descriptive statistics for all columns except the
        Timestamp column.
        Returns a new pd.DataFrame containing these statistics.
    """
    return df.drop(columns=['Timestamp']).describe()
