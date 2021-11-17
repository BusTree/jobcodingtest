import random

user_input = input().split(' ')
a, b = [], []
n = int(user_input[0])
k = int(user_input[1])

for i in range(n):
    a.append(random.randrange(1, 10000000))
    b.append(random.randrange(1, 10000000))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))