n = 2
m = 15

moeny_type = [2, 3]
dp = [m]

while m > 0:
    array = []
    for i in range(n):
        value = dp[-1] - moeny_type[i]
        array.append(value)
    dp.append(min(array))
    if dp[-1] <= 0:
        break

if dp[-1] == 0:
    print(dp[-2])

else:
    print(-1)

print(dp)
