import random
sales = [random.randint(1, 10) for i in range(10)]
print(sales)
mean = sum(sales) / len(sales)
print(mean)

deviations = [s - mean for s in sales]
print(deviations)

import math
std = sum([d ** 2 for d in deviations]) / len(deviations)
표준편차 = math.sqrt(std)
print(std, 표준편차)

import pandas as pd
df = pd.DataFrame(sales, columns = ['sales'])
print(df)
df['sales'].std()
print(df['sales'].std())