# -*- coding: utf-8 -*-
"""
Getting data from Quandl to create a dataframe
"""

import quandl
import pandas as pd
# Getting data from Quandl webpage
api_key = open('quandlapikey.txt','r').read()

df = Quandl.get("FMAC/HPI_TX", authtoken=api_key)

print(df.head())

# Dataframe in form of list having umber of dataframes within it
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(fiddy_states)

# reading one datarame i.e 1st one. This is eventually a dataframe

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(fiddy_states[0])

# Taking a column our of dataframe 
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(fiddy_states[0][0])

for abbv in fiddy_states[0][0][1:]:
    print(abbv)

for abbv in fiddy_states[0][0][1:]:
    #print(abbv)
    print("FMAC/HPI_"+str(abbv))