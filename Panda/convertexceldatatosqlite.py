# -*- coding: utf-8 -*-
"""convertexceldatatosqlite.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sKocllROYRFoPtjAYMiPW2jgqhoKV2n7
"""

import pandas as pd
import sqlite3
df= pd.read_excel('mark.xlsx')
#database = "mark.sqlite"
conn = sqlite3.connect("mark.sqlite")
df.to_sql(name='Users',con=conn,if_exists='replace',index=False)

conn.close()

