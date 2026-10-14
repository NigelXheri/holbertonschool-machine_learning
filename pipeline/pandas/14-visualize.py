#!/usr/bin/env python3
"""Preprocess and visualize Coinbase Bitcoin data.

Loads the one-minute Coinbase USD candle data and cleans it:

* removes the ``Weighted_Price`` column
* renames ``Timestamp`` to ``Date`` and converts it to a datetime index
* fills missing values
* keeps data from 2017 onward
* resamples to daily intervals

The resulting DataFrame is printed and plotted.
"""
import matplotlib.pyplot as plt
import pandas as pd

from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Remove the unneeded column
df = df.drop(columns=['Weighted_Price'])

# Rename Timestamp to Date and convert Unix seconds to datetime index
df = df.rename(columns={'Timestamp': 'Date'})
df['Date'] = pd.to_datetime(df['Date'], unit='s')
df = df.set_index('Date')

# Forward-fill missing Close values from the previous row
df['Close'] = df['Close'].ffill()

# Missing High, Low, Open take the same row's Close value
for col in ['High', 'Low', 'Open']:
    df[col] = df[col].fillna(df['Close'])

# No trades occurred where volume is missing, so set it to 0
df[['Volume_(BTC)', 'Volume_(Currency)']] = (
    df[['Volume_(BTC)', 'Volume_(Currency)']].fillna(0)
)

# Keep only data from 2017 onward
df = df.loc['2017':]

# Aggregate minute data into daily rows
df = df.resample('D').agg({
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum',
})

print(df)

# Plot every column against the Date index
df.plot()
plt.show()
