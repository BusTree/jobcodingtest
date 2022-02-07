word = 'aabbaccc'  # 답 7
array = []
result = []
result2 = []
def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]


for i in range(1, len(word)):
    array.append(list_chunk(word, i))

print('array')
print(array)

for i in range(0, len(array)):
    row = {
        'num': 1,
        'str': ''
    }
    change = []
    for j in range(1, len(array[i])):
        if array[i][j] == array[i][j - 1]:
            row['num'] += 1
            # print('같은 문자열 반복')
            print(row['num'])

        else:
            # print('문자열 끊김')
            print(array[i][j - 1])
            row['str'] = array[i][j - 1]
            change.append(row)
            row = {
                'num': 1,
                'str': ''
            }

        if (len(array[i]) - 1 == j):
            row['str'] = array[i][j - 1]
            change.append(row)

            print(array[i][j - 1])
            result.append(change)

                
print(result)

for i in range(0, len(result)):
    count = 0
    for j in range(0, len(result[i])):
        count += result[i][j]['num']
        print(result[i][j]['num'])
    result2.append(count)


print(result2)