# -*- coding: utf-8 -*-
"""ReMultiWord.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pDQW6wdi335YLBtqEO_WofoA3EWuWmbw
"""

import re

text = " ".join(x)
print(text)

import re#multi word

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


import re#multi word

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|Spain|sta", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")