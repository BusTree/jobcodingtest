import time

# 1이 될 때까지
n = 17
k = 4
count = 0

while (n > 1):
    (a, b) = divmod(n, k)
    if b == 0:
        n = a
    else:
        n -= 1
    count += 1

print('result')
print(count)
