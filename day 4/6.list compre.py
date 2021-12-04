numbers = list(range(10))
print(numbers)

evens = [n for n in numbers if n % 2 == 0]
print(evens)

evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens)

odds = [n for n in numbers if n % 2 != 0]
print(odds)

odds = []
for n in numbers:
    if n % 2 != 0:
        odds.append(n)
print(odds)

square_evens = [n ** 2 for n in numbers if n % 2 == 0]
print(square_evens)