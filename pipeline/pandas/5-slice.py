#!/usr/bin/env python3
"""Contains function def slice(df): that takes a pd.DataFrame and:
    Extracts the columns High, Low, Close, and Volume_(BTC).
    Selects every 60th row from these columns.
    Returns: the sliced pd.DataFrame
"""


def slice(df):
    """Takes a pd.DataFrame and:
        Extracts the columns High, Low, Close, and Volume_(BTC).
        Selects every 60th row from these columns.
        Returns: the sliced pd.DataFrame
    """
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']].loc[::60]
