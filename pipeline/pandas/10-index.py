#!/usr/bin/env python3
"""Takes a pd.DataFrame and sets the Timestamp column as the index of the dataframe."""


def index(df):
    """Takes a pd.DataFrame and sets the Timestamp column as the index of the dataframe."""
    return df.set_index('Timestamp')
