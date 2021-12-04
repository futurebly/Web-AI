import pandas as pd
path = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/iris.csv'
df = pd.read_csv(path)
print(df['품종'].value_counts())
df_selected = df[(df['품종'] == 'setosa')]
df_selected2 = df[(df['품종'] == 'versicolor')]
df_selected3 = df[(df['품종'] == 'virginica')]
print(df_selected.sort_values(by=['꽃잎폭'], ascending=False).head(1))
print(df_selected2.sort_values(by=['꽃잎폭'], ascending=False).head(1))
print(df_selected3.sort_values(by=['꽃잎폭'], ascending=False).head(1))