# 연산자 끼워넣기
from itertools import permutations
import math

n = 6
a = ['1', '2', '3', '4', '5', '6']
pomulser = [2, 1, 1, 1]

type = ['+', '+', '-', '*', '/']

typeArray = list(permutations(type, len(type)))

count = n + n-1


def search():
    row = []
    column = []
    for j in range(len(typeArray)):
        typeCount = 0
        numberCount = 0
        for i in range(count):
            if i % 2 == 0:
                row.append(a[numberCount])
                numberCount += 1
            else:
                row.append(typeArray[j][typeCount])
                typeCount += 1
        column.append(row)
        row = []
    return column


def solution(array):
    result = []
    for i in array:
        el = i[0]
        for j in range(2, len(i)):
            if j % 2 == 0:
                temp = eval(str(el) + i[j - 1] + i[j])
                el = math.trunc(temp)
        result.append(el)

    print('result')
    print(result)
    return max(result), min(result)


searchResult = search()
solution(searchResult)
max, min = solution(searchResult)
print('result')
print(max)
print(min)

