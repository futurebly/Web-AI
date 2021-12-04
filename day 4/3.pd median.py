import random
sales = [random.randint(1, 100) for i in range(10)]
sales.sort()
print(sales)

n = len(sales) // 2
if len(sales) % 2 == 0:
    print(sum(sales[n-1:n+1]) / 2)
else:
    print(sales[n])

print(sum(sales) / len(sales))


import pandas as pd
df = pd.DataFrame(sales, columns = ['sales'])
print(df)

df['sales'].median()
print(df['sales'].median())