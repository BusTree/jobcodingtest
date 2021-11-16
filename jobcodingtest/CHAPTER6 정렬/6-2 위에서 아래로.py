import random

n = input()

array = []

for i in range(int(n)):
    array.append(random.randrange(1, 501))

array.sort(reverse=True)

for i in array:
    print(i, end=' ')