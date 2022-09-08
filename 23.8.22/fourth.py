import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
diamonds['Quality – color'] = diamonds.cut + ', ' + diamonds.color
print(diamonds.head())