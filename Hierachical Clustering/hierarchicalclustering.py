# -*- coding: utf-8 -*-
"""HierarchicalClustering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zSmvQLjTGx5pb7XVB92ItPQOByYif8Wz
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

x = [1,2,3,6,7,8]
y = [4,5,6,7,8,5]

data = list(zip(x, y))
hierarchical_cluster = AgglomerativeClustering(n_clusters=2, metric='euclidean', linkage='ward')
labels = hierarchical_cluster.fit_predict(data)

plt.scatter(x, y, c=labels)
plt.show()