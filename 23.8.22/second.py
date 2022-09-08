import pandas as pd
user_cols = ['carat', 'cut', 'x', 'y', 'z']
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print("First 6 rows:")
print(diamonds[user_cols].head(6))