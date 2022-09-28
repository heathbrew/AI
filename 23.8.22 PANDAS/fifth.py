import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print("Number of rows and columns:")
print(diamonds.shape)
print("\nData type of each column:")
print(diamonds.dtypes)