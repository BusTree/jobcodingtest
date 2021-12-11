import random

# n = random.randrange(1, 1000)
n = 3
x = n
y = 2

dp = []

tail_type = [[1, 2], [2, 1], [2, 2]]

for i in range(y):
    for j in range(x):
        print()
