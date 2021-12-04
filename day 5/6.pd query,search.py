import pandas as pd
path = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/lemonade.csv'
df = pd.read_csv(path)
print(df)

print(df[(df['온도'] > 23)])
print(df[(df['온도'] > 23) | (df['판매량'] == 40)])

d = {'col1': [0,1,2,3],
     'col2': ['Gold', 'Bronze', 'Gold', 'Silver']}
df1 = pd.DataFrame(d)
print(df1)

print(df1['col2'].str.contains('o'))
print(df1[df1.col2.str.contains('o')])