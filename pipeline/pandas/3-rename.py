#!/usr/bin/env python3
"""Takes a DataFrame as an input and does the following:
    - df is a pd.DataFrame containing a column named Timestamp.
    - The function should rename the Timestamp column to Datetime.
    - Convert the timestamp values to datetime values
    - Display only the Datetime and Close column
    - Returns: the modified pd.DataFrame
"""
import pandas as pd


def rename(df):
    """Takes a DataFrame as an input and does the following:
        - df is a pd.DataFrame containing a column named Timestamp.
        - The function should rename the Timestamp column to Datetime.
        - Convert the timestamp values to datetime values
        - Display only the Datetime and Close column
        - Returns: the modified pd.DataFrame
    """
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')
    df = df.rename(columns={"Timestamp": "Datetime"})
    return df[['Datetime', 'Close']]
