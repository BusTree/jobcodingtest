array = [3, 9, 8, 7, 8]
temp = []

for (i, value) in enumerate(array):

    if i == 0:
        continue

    if value == 0:
        continue

    if i != len(array) - 1:
        a = array[i - 1] + array[i + 1]

        if a > value:
            array[i] = 0
        else:
            array[i - 1] = 0
            array[i + 1] = 0
    else:
        print('마지막요소')
        a = array[i - 1] = 0

        if a > value:
            array[i] = 0
        else:
            array[i - 1] = 0

print('array')
print(array)
print(sum(array))