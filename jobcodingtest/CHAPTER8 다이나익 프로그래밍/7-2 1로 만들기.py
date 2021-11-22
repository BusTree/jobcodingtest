
result = []
result.append(26)

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
        print('array')
        print(array)
        if x == 1:
            break

        return array


array = search(result)
print('array', array)

# 배열로 저장하면서 백터개념으로다가 배열에 쌓아서 계산해보는걸 하고싶음
# 즉 1번 상황 [26]
# 2번 [26, [13, 25]] or [13, 25]
# 3번 [26, [13, 25], [12, 5]]or [12, 5]
