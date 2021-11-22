
x = 26
step = [26]
result = []
result.append(26)
count = 0

def search(x, count):
    array = []
    print('xxxx')
    print(x)
    if x % 5 == 0:
        array.append(x // 5)

    if x % 3 == 0:
        array.append(x // 3)

    if x % 2 == 0:
        array.append(x // 2)

    array.append(x - 1)
    count += 1

    return array, count

while True:
    print('count', count)
    step, step_count = search(step[count], count)
    for i in step:
        search(i, count)
    count += step_count
    # result.append(step)
    # print(result)

    if step.count(1):
        break

print('result')
print(result)
