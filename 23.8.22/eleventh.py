import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print("Original Dataframe:")
print(diamonds.head())
print("\nAfter droping those rows where any value in a row is missing in carat and cut columns:")
print(diamonds.dropna(subset=['carat', 'cut'], how='any').shape)
print("\nAfter droping those rows where all values in a row are missing in carat and cut columns:")
print(diamonds.dropna(subset=['carat', 'cut'], how='all').shape)