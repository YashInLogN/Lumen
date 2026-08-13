import pandas as pd

df = pd.read_csv('trial/data.csv', index_col=['Name'])

print('Sum:')
print(df.sum(numeric_only=True))
print('\nMean:')
print(df.mean(numeric_only=True))
print('\nCount:')
print(df.count(numeric_only=True))
print('\nMax:')
print(df.max(numeric_only=True))
print('\nMin:')
print(df.min(numeric_only=True))

print(df.head())

group = df.groupby(['Type1'])

print(group['Weight'].mean())
print(group['Weight'].max())
print(group['Weight'].min())
print(group['Weight'].sum())
print(group['Weight'].count())

print(df[df['Type1'] == 'Poison'].count())

print(df[(df['Type1'] == 'Poison') & (df['Type2'] == 'Fairy')].count())

group1 = df.groupby('Type1')['Height']