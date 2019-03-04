# -*- coding: utf-8 -*-
"""
Pandas Basics

"""

import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style


web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats)

df.head()

df.tail()

df.set_index('Day', inplace=True)
df = df.set_index('Day')

print(df['Visitors'])

df['Visitors'].plot()
plt.show()

df.plot()
plt.show()

print(df[['Visitors','Bounce Rate']])