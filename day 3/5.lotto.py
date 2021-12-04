import random
lotto = []
while len(lotto) < 6:
    num = random.randint(1, 45)
    if num not in lotto:
        lotto.append(num)
print(lotto)


# import random
# lotto = random.sample(range(1, 46), 6)
# lotto.sort()
# print(lotto)