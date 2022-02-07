# word = 'aabbaccc'  # 답 7
word = 'ababcdcdababcdcd'  # 답 9
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
            if(row['num'] == 1):
                row['num'] = ''
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
    last = ''
    for j in range(0, len(result[i])):
        last += str(result[i][j]['num'])
        last += result[i][j]['str']
        print(result[i][j]['num'])
    result2.append(last)

print('정답')
print(len(min(result2)))