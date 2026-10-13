#!/usr/bin/env python3
"""Contains function def flip_switch(df): that takes a pd.DataFrame and:
    Sorts the data in reverse chronological order.
    Transposes the sorted dataframe.
    Returns: the transformed pd.DataFrame.
"""


def flip_switch(df):
    """Contains function def flip_switch(df): that takes a pd.DataFrame and:
        Sorts the data in reverse chronological order.
        Transposes the sorted dataframe.
        Returns: the transformed pd.DataFrame.
    """
    return df.sort_values(by='Timestamp', ascending=False).T
