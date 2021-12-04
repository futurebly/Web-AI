# mean
print(list(range(10)))

import random
sales = [random.randint(1, 10) for i in range(10)]
print(sales)

mean = sum(sales) / len(sales)
print(mean)

# pandas mean
import pandas as pd
df = pd.DataFrame(sales, columns = ['sales'])
print(df)

df['sales'].mean()
print(mean)