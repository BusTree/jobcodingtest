import string
import random

n = input()
name_len = 3
array = []

for i in range(int(n)):
    input_value = ''.join(random.choices(string.ascii_uppercase + string.digits, k=name_len)) + ' ' + str(random.randrange(1, 101))
    el = input_value.split(' ')
    array.append((el[0], int(el[1])))

array = sorted(array, key=lambda el: el[1])
print(array)

for i in array:
    print(i[0], end=' ')
