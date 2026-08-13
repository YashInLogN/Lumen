import pandas as pd

# Data cleaning = the process of fixing/removing:
# incomplete, incorrect, or irrelevant data.
# ~75% of work done with Pandas is data cleaning

df = pd.read_csv('trial/data.csv', index_col=['Name'])

# drop irrelevant dataframe
df = df.drop(columns=['No'])

check = df[df['Type2'] == 'Fairy']
mean_val = check['Height'].mean()
# handle missing data
# df = df.dropna(subset=['Type2'])
group = df.groupby('Type1')['Height']
df = df.fillna({'Type2': df['Type2'].min()})
df = df.fillna({'Height': mean_val})

# fix inconsistent values
df['Type2'] = df['Type2'].replace('Fairy', 'FAIRY')

# standardise text
df['Type2'] = df['Type2'].str.lower()

# Fix data types
df['Legendary'] = df['Legendary'].astype(bool)

print(df.head(10))

