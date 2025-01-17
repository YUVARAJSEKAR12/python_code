# -*- coding: utf-8 -*-
"""readdatafromnumpyconverttodataframewriteinexcelandcsv.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sKocllROYRFoPtjAYMiPW2jgqhoKV2n7
"""

import pandas as pd
import numpy as np

# Create numpy arrays
a = np.array([11, 99, 303, 44, 55, 6])
b = np.array([1, 2, 3, 4, 5, 6])
c = a + b
d = np.array(["Abi", "Bala", "Coulins", "Dinesh", "Elger", "Ganesh"])

# Create a DataFrame
frame = {"Name": d, "A": a, "B": b, "C": c}
g = pd.DataFrame(frame)

# Display the DataFrame
print(g)

# Specify the file paths
excel_file_path = r'D:\Data and task\Data\panda\output1.xlsx'
csv_file_path = r'D:\Data and task\Data\panda\file1.csv'

# Write the DataFrame to Excel and CSV files
g.to_excel(excel_file_path, index=False)
g.to_csv(csv_file_path, index=False)

print("Files saved successfully.")

