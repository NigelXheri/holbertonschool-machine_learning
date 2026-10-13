#!/usr/bin/env python3
"""Takes a pd.DataFrame and:
    Removes any entries where Close has NaN values.
    Returns: the modified pd.DataFrame
"""


def prune(df):
    """Takes a pd.DataFrame and:
        Removes any entries where Close has NaN values.
        Returns: the modified pd.DataFrame
    """
    return df.dropna(subset=['Close'])
