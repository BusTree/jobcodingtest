import random

n = input()

array = []

for i in len(n):
    array.append(random.randrange(1, 501))

array.sort(reverse=True)

for i in array:
    print(i, end=' ')