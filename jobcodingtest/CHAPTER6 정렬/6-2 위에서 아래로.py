import random

n = input()

array = []
# array = [3, 15, 27, 12]

for i in len(n):
    array.append(random.randrange(1, 501))

array.sort(reverse=True)

for i in array:
    print(i, end=' ')