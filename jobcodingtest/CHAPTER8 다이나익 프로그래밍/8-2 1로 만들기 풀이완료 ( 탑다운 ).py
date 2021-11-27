
result = []
result.append([26])
def search(list):
    array = []
    for x in list:
        if x % 5 == 0:
            array.append(x // 5)

        if x % 3 == 0:
            array.append(x // 3)

        if x % 2 == 0:
            array.append(x // 2)

        array.append(x - 1)
    return array

while True:
    array = search(result[-1])
    result.append(array)

    if (min(result[-1])) == 1:
        break

print(result)
print(len(result) - 1)

