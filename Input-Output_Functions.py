# -*- coding: utf-8 -*-
"""
I/O in Python

NASDAQOMX-XQC.csv taken from Quandl.
"""

import pandas as pd

df = pd.read_csv('NASDAQOMX-XQC.csv')
print(df.head())

df.set_index('Date', inplace = True)

# Saving to new csv file
df.to_csv('newcsv2.csv')

df['Value'].to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv')
print(df.head())

# Removing index from begining

df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head())

df.columns = ['House_Prices']
print(df.head())

df.to_csv('newcsv3.csv')

# With no header name

df.to_csv('newcsv4.csv', header=False)

# Overall , we may write like
df = pd.read_csv('newcsv4.csv', names = ['Date','House_Price'], index_col=0)
print(df.head())

#Let's rename columns

df = pd.read_csv('newcsv4.csv', names = ['Date','House_Price'])
print(df.head())

df.rename(columns={'House_Price':'Prices'}, inplace=True)
print(df.head())

