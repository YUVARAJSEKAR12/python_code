# -*- coding: utf-8 -*-
"""GA&FuzzyAlgorithm.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sKocllROYRFoPtjAYMiPW2jgqhoKV2n7
"""

#pip install fuzzywuzzy
#pip install python-Levenshtein
#conda install -c conda-forge fuzzywuzzy
#conda install -c conda-forge python-levenshtein
#GA
import pandas as pd

def A():
  A = pd.read_excel("Consumables_Registers.xlsx")
  print(A)
  return A
def B():
  B = pd.read_excel("Employee_Attendance.xlsx")
  print(B)
  return B
def C():
  C = pd.read_excel("Feedback_and_Customer_Details,xlsx")
  print(C)
  return C
def D():
  D = pd.read_excel("Income_Tax_Detail.xlsx")
  print(D)
  return D
def E():
  E = pd.read_exccel("Salary_Detail.xlsx")
  print(E)
  return E
def F():
  F = pd.read_excel("Sales_and_Profit.xlsx")
  print(F)
  return F
def G():
  G = pd.read_excel("Stock_Register.xlsx")
  print(G)
  return(G)

Z = input("Enter your value = ")

Y = Z.lower()

T = ['show','the','a','list','details','give','report','detail','register']

X = Y.split()

filter = [word for word in X if word.lower() not in T]

key = " ".join(filter)

if key =='consumables' or key == 'consumable':
  A()
elif key == 'employee attendance' or key == 'employee' or key == 'attendance' or key == 'staff attendance':
  B()
elif key == 'feedback' or key == 'customer' or key == 'feedback and customer' or key == 'customer and feedback':
  C()
elif key == 'income tax' or key == 'tax':
  D()
elif key == 'salary':
  E()
elif key == 'sales and profit' or key == 'sales' or key == 'profit' or key == 'profit and sales':
  F()
elif key == 'stock' or key == 'stocks':
  G()
else:
  print("Invalid input")


#fuzzy
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def A():
  A = pd.read_excel("Consumables_Registers.xlsx")
  print(A)
  return A
def B():
  B = pd.read_excel("Employee_Attendance.xlsx")
  print(B)
  return B
def C():
  C = pd.read_excel("Feedback_and_Customer_Details.xlsx")
  print(C)
  return C
def D():
  D = pd.read_excel("Income_Tax_Detail.xlsx")
  print(D)
  return D
def E():
  E = pd.read_exccel("Salary_Detail.xlsx")
  print(E)
  return E
def F():
  F = pd.read_excel("Sales_and_Profit.xlsx")
  print(F)
  return F
def G():
  G = pd.read_excel("Stock_Register.xlsx")
  print(G)
  return(G)

Z = input("Enter your value = ")

Z1 = "consumable register"
Z2 = "employee attendance"
Z3 = "feedback and customer"
Z4 = "income tax"
Z5 = "salary"
Z6 = "sales and profit"
Z7 = "stocks"

Y1=fuzz.WRatio(Z, Z1)
print("consumable =",Y1)
Y2=fuzz.WRatio(Z, Z2)
print("employee attendance =",Y2)
Y3=fuzz.WRatio(Z, Z3)
print("feedback and customer =",Y3)
Y4=fuzz.WRatio(Z, Z4)
print("income tax =",Y4)
Y5=fuzz.WRatio(Z, Z5)
print("salary =",Y5)
Y6=fuzz.WRatio(Z, Z6)
print("sales and profit =",Y6)
Y7=fuzz.WRatio(Z, Z7)
print("stocks =",Y7)

if Y1 > 80 :
  M = A()
elif Y2 > 80 :
  Z= B()
elif Y3 > 80 :
  Y = C()
elif Y4 > 80 :
  X = D()
elif Y5 > 80 :
  W = E()
elif Y6 > 80 :
  V = F()
elif Y7 > 80 :
  T = G()
else:
  print("Invalid input")

pip install fuzzywuzzy

