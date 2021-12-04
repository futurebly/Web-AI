import random
sales = [random.randint(1, 100) for i in range(17)]
sales.sort()
print(sales)

n = (len(sales) // 4)
print("count", n)
print(f"{sales[n]}, {sales[2*n]}, {sales[3*n]}")

import pandas as pd
df = pd.DataFrame(sales, columns = ['sales'])
print(df)

print(df['sales'].quantile([0, .25, .5, .75, 1]))
print(df.describe())