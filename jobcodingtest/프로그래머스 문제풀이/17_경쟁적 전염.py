from copy import deepcopy

# 경쟁적 전염

n = 3  # 시험관 사이즈
virusType = 3  # 바이러스 종류

# 시험관 배열
temp = [
    [1, 0, 2],
    [0, 0, 0],
    [3, 0, 0],
]

s = 2  # 출력 시간
x = 2  # 출력 x 위치
y = 3  # 출력 Y 위치 

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

array = [temp]  # 바이러스 전염기록 배열

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def covid_19(x, y, virusType, list):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny <n:
            if list[nx][ny] == 0:
                list[nx][ny] = virusType
    array.append(list)
    print(list)
    return list


# 바이러스 우선순위별 증식
def virusLevelSeach(virusType, list):
    for (i, val_y) in enumerate(list):
        for (j, val_x) in enumerate(val_y):
            if val_x == virusType:
                covid_19(i, j, virusType, deepcopy(list))

# 시간별 증식
for i in range(s):
    for j in range(1, virusType + 1):
        virusLevelSeach(j, array[-1])

print('결과')
print(array[-1][y - 1][x - 1])

