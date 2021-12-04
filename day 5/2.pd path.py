import pandas as pd
path = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/lemonade.csv'
df = pd.read_csv(path)
print(df)

print(df.shape)
df.info()

print(df.head(2))
print(df.tail(2))
print(df.columns)