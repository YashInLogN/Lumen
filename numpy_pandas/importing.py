import pandas as pd
import numpy as np

df = pd.read_csv('trial/data.csv', index_col=['Name'])

# print(df.to_string())

print("Flying type count: ", len(df[df['Type2'] == 'Flying']))

print(df.loc['Pikachu', ['Type1', 'Type2']])

print(df[df['Height'] >= 2].to_string())


