# 괄호 변환
# 답안이랑 뭐가다른지 찾아볼것
# 민우 문제풀이 방법대로 풀어볼 것

import copy

global u  # 균형잡힌 괄호 문자열로 더이상 분리할수 없어야 함
u = ''
global v  # 빈 문자열이 될수도있다.
v = '()))((()'

global result
result = ''

def u_append(u, v):
    startCount = 0
    endCount = 0
    for (i, val) in enumerate(v):
        if (val == '('):
            startCount += 1
            u += val
        else:
            endCount += 1
            u = u + val
        if(startCount > 0 and startCount == endCount):
            v = v[i+1:]
            print('u 값')
            print(u)
            print('v 값')
            print(v)
            return u, v


def checkCorrect(u):
    count = 0
    for (i, val) in enumerate(u):
        if val == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            print('False')
            return False
    print('True')
    return True


u, v = u_append(u, v)
test = 5
while test > 0:
    test -= 1
    correct = checkCorrect(u)

    if correct:
        result = copy.deepcopy(u)
        u, v = u_append(u, v)
        result += v
        print('correct')
        print(result)
    else:
        print('4-1 진행')
        u, v = u_append(u, v)
        v = '(' + v + ')'
        print('v 값 확인')
        print(v)
        u = u[1:-1]
        print('u 확인')
        print(u)
        temp = list(u)
        for i in range(len(u)):
            if temp[i] == '(':
                temp[i] = ')'
            else:
                temp[i] = '('
        temp = "".join(temp)
        print('result')
        print(v + temp)
        break;