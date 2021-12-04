import pandas as pd
path = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/boston.csv'
df = pd.read_csv(path)
df_selected = df[(df['chas'] == 1)]
print(df_selected.sort_values(by=['medv'], ascending=False).head(10))

# import pandas as pd
# path = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/boston.csv'
# df = pd.read_csv(path)
# df_sorted = df.sort_values(by=['medv'], ascending=False)
# print(df_sorted[df_sorted['chas'] == 1])
# print(df_sorted[df_sorted['chas'] == 1].head(10))