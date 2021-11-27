# 성적이 낮은 순서로 학생 출력하기

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


# sorted()는 전역함수로 사용되고 key로 lambda를 사용가능하다.
# sort()는 array객체에 있는 함수이다.
# 파이썬 형변환에 주의해야한다.
