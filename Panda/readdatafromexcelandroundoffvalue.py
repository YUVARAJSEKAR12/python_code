# -*- coding: utf-8 -*-
"""readdatafromexcelandroundoffvalue.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sKocllROYRFoPtjAYMiPW2jgqhoKV2n7
"""

import pandas as pd
df =pd.read_excel('mark.xlsx')
c=df.round(0)
print(c)

