# 경쟁적 전염
from copy import deepcopy

n = 3
m = 3

virusType = 3

temp = [
    [1, 0, 2],
    [0, 0, 0],
    [3, 0, 0],
]

s = 2

y = 3
x = 2

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

array = []
array.append(temp)

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def covid_19(x, y, virusType, list):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if list[nx][ny] == 0:
                list[nx][ny] = virusType
    array.append(list)
    print(list)
    return list

def virusLevelseach(virusType, list):
    for (i, val_y) in enumerate(list):
        for (j, val_x) in enumerate(val_y):
            if val_x == virusType:
                covid_19(i, j, virusType, deepcopy(list))


for i in range(s):
    for j in range(1, virusType + 1):
        virusLevelseach(j, array[-1])

print('결과')
print(array[-1][y - 1][x - 1])

