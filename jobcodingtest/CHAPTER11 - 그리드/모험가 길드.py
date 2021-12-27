headers = 5
fear = [2, 3, 1, 2, 2]
fear.sort()

count = 0
result = 0
for i, value in enumerate(fear):
    count += 1
    if  (count >= value):
        result += 1
        count = 0

print('result')
print(result)
