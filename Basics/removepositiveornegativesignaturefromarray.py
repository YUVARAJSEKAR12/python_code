# -*- coding: utf-8 -*-
"""removepositiveornegativesignaturefromarray.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sKocllROYRFoPtjAYMiPW2jgqhoKV2n7
"""

import numpy as np
arr = np.array([-1, -2, 1, 2, +3, -4])
newarr = np.absolute(arr)#polarity will be removed
print(newarr)

