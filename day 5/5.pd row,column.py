import pandas as pd
path = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/lemonade.csv'
df = pd.read_csv(path)
print(df.shape)
print(df['온도'].shape)
print(df)
print(df['온도'])

print(df[['온도']].shape)
print(df[['온도']])

print(df[['온도', '판매량']])

print(df.loc[0:3])
print(df.iloc[0:3])
print(df.loc[2:4])
print(df.iloc[2:4])
print(df.iloc[2])

print(df.iloc[3,1])
print(df.iloc[2:4, :])
print(df.iloc[2:4, 1:])

df_sorted = df.sort_values(by=['판매량'], ascending=False)
print(df_sorted.head())
print(df_sorted.iloc[0])
print(df_sorted.loc[0])