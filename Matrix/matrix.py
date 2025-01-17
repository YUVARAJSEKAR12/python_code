# -*- coding: utf-8 -*-
"""Matrix.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zSmvQLjTGx5pb7XVB92ItPQOByYif8Wz
"""

import numpy as np
a = np.array([[1,2],[2,4],[10,20]])
print(a)
s=a.shape
s1=a.size
print("\nShape=",s)
print("\nSize=",s1)

#slice
import numpy as np#3x4
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])

c=a[0,0]
print(c)

import numpy as np#3x4
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])
print(a)
s=a.shape
s1=a.size
print("\nShape=",s)
print("\nSize=",s1)

#math
import numpy as np#3x4
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])
c=a+1
print(c)



#math
import numpy as np#3x4
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])
c=a/3
print(c)


import numpy as np#3x4
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])
b= np.array([[11,21,31,4],[21,14,5,6],[10,210,319,31]])
c=a+1
add=a+b
print(add)


import numpy as np#3x4
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])
b= np.array([[11,21,31,4],[21,14,5,6],[10,210,319,31]])
c=a+b
print(c)
a=a>b
print(a)

import numpy as np#sort
x = np.array([[10,2,3,4],[20,4,5,6],[10,20,39,3]])
print("Original mat:")
print(x)
print("sort:")
y = np.sort(x)
print(y)


import numpy as np#sort
x = np.array([[10,2,3,4],[20,4,5,6],[10,20,39,3]])
print("Original mat:")
print(x)

y = np.min(x)
z=np.max(x)
a=np.mean(x)
print("Min",y)
print("Average",a)
print("max",z)


import numpy as np#reverse
x = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])
print("Original mat:")
print(x)
print("Reverse mat:")
y = x[::-1]# -1 inside colon
print(y)

import numpy as np
import pandas as pd
a = np.array([[1, 2, 3, 4], [2, 4, 5, 6], [10, 20, 39, 3]])

# Convert the matrix to a Pandas DataFrame
df = pd.DataFrame(a, columns=['Col1', 'Col2', 'Col3', 'Col4'])
print(df)