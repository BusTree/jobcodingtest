# 게임 개발
input_map_size = '4 4'
input_map_size = list(map(int, str(input_map_size.replace(" ", ""))))

input_direction = '1 1 0'

input_map_1 = '1 1 1 1'
input_map_2 = '1 0 0 1'
input_map_3 = '1 1 0 1'
input_map_4 = '1 1 1 1'

full_map = []
full_map.append(list(map(int,str(input_map_1.replace(" ", "")))))
full_map.append(list(map(int,str(input_map_2.replace(" ", "")))))
full_map.append(list(map(int,str(input_map_3.replace(" ", "")))))
full_map.append(list(map(int,str(input_map_4.replace(" ", "")))))

row_map = []
world = []

for (i, x) in enumerate(full_map):
    row_map = []
    for (j, y) in enumerate(x):
        map_status = {
            "floor": full_map[i][j],  # 육지 바다 값
            "known": 0,  # 바다 육지 여부 확인
            "tread": 0,  # 해당 픽셀 밟았는지 여부
            "x": i,
            "y": j
            }
        row_map.append(map_status)
    world.append(row_map)
# print('world', world)
# map_status {'floor': 1, 'known': 0, 'tread': 0}

state = list(map(int, str(input_direction.replace(" ", ""))))
state_x = state[0] -1  # 서있는 x좌표
state_y = state[1] -1  # 서있는 y좌표
axis = state[2]  # 서있는 방향
direction_type = [0, 1, 2, 3]

# 배열값 계산하거나 원형아닌형태 찾을것 원형아닌걸 찾아야 앞으로도 편하게 문제풀수있음

def check_map(single_map, axis, x, y):
    # try:
        check_result = None
        if axis == 0:
            print(single_map[100:x])
            print('22222222222222222')
            print('123', single_map[x:x+1])
            check_result = single_map[x-1][y]
        elif axis == 1:
            check_result = single_map[x][y-1]
        elif axis == 2:
            check_result = single_map[x+1][y]
        elif axis == 3:
            print('3333333333333333333')
            check_result = single_map[x][y+1]
        return check_result
    # except:
        return None

a = 0
while a < 4:
    # 계산먼저 - 계산식은 월드좌표
    a += 1
    check = check_map(world, axis, state_x, state_y)
    print('check')
    print(check)
    if check:
        print('왼쪽 회전후 왼쪽한칸 구현')
    else:
        axis = direction_type[axis - 1]
        print('왼쪽 회전만 진행')
        print(axis)
        continue
    break
    # if # 칸이 존재하고 known이 false 경우
    #
    # state_direction = direction_type[state_direction - 1]