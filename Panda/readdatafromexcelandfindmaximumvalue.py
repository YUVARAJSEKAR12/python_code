# -*- coding: utf-8 -*-
"""readdatafromexcelandfindmaximumvalue.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sKocllROYRFoPtjAYMiPW2jgqhoKV2n7
"""

import pandas as pd
df =pd.read_excel('mark.xlsx')
df1 = df[["Bio","Phy","Math","Tamil","Eng"]]
ma=df1.max()
print(ma)

