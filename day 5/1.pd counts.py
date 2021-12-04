fruit = ['배', '배', '배', '배', '사과', '사과', '귤', '귤', '귤']
print(set(fruit))

fruit_count = [(s, fruit.count(s)) for s in set(fruit)]
print(fruit_count)

fruit_count = dict([(s, fruit.count(s)) for s in set(fruit)])
print(fruit_count)


import pandas as pd
df = pd.DataFrame(fruit, columns=['과일'])
print(df)

print(df['과일'].value_counts())

print(df['과일'].value_counts(normalize=True)) #normalize: 확률 계산