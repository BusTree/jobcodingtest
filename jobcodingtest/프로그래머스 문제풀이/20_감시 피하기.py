# 감시피하기
# n x n 벽
# 학생 S 장애물 O 선생 T

from itertools import combinations
input = 5

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

world_map = [
    ['X', 'S', 'X', 'X', 'T'],
    ['T', 'X', 'S', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X'],
    ['X', 'T', 'X', 'X', 'X'],
    ['X', 'X', 'T', 'X', 'X']
]

spaces = []
mapList = []

def searchTeacher():
    for (i, row) in enumerate(world_map):
        for (j, column) in enumerate(row):
            if column == 'T':
                print('선생님 위치확인')
                print(i, j)
                searchStudent(i, j)

            if column == 'X':
                print('빈공간 확인')
                spaces.append([i, j])

def searchStudent(tRow, tColumn):
    for (i, el) in enumerate(world_map[tRow]):
        if el == 'X':
            print('학생 검거')
        if el == 'O':
            print('장애물')

    for (i, el) in enumerate(world_map):
        if el[tColumn] == 'X':
            print('학생 검거')
        if el[tColumn] == 'O':
            print('장애물')

def makeObstacle():
    for data in combinations(spaces, 1):
        for x, y in data:
            world_map[x][y] = 'O'

searchTeacher()
makeObstacle()

# 파이썬 2중포문 한번에 돌릴수있다 앞으로 활용가능