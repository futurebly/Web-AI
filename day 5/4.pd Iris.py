import pandas as pd
path = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/iris.csv'
df = pd.read_csv(path)
print(df)

print(df.shape)
print(df.info())

print(df.head(2))
print(df.tail(2))
print(df.columns)