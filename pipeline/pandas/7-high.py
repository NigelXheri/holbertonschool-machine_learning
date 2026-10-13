#!/usr/bin/env python3
"""Takes a pd.DataFrame and:
    Sorts it by the High price in descending order.
    Returns: the sorted pd.DataFrame.
"""


def high(df):
    """Takes a pd.DataFrame and:
        Sorts it by the High price in descending order.
        Returns: the sorted pd.DataFrame.
    """
    return df.sort_values(by='High', ascending=False)
