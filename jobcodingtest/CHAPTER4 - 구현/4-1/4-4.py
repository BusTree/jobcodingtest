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
count = 1

for (i, y) in enumerate(full_map):
    row_map = []
    for (j, x) in enumerate(y):
        map_status = {
            "floor": full_map[i][j],  # 육지 바다 값
            "known": 0,  # 바다 육지 여부 확인
            "tread": 0,  # 해당 픽셀 밟았는지 여부
            "x": j,
            "y": i
            }
        row_map.append(map_status)
    world.append(row_map)
print('world', world)
# map_status {'floor': 1, 'known': 0, 'tread': 0}

state = list(map(int, str(input_direction.replace(" ", ""))))
state_x = state[0]  # 서있는 x좌표
state_y = state[1]  # 서있는 y좌표
axis = state[2]  # 서있는 방향
direction_type = [0, 1, 2, 3]
rotation = 0

# 배열값 계산하거나 원형아닌형태 찾을것 원형아닌걸 찾아야 앞으로도 편하게 문제풀수있음

def check_map(single_map, axis, x, y):
    # try:
        check_result = None
        if axis == 0 and x-1 >= 0:
            check_result = single_map[y][x-1]
        elif axis == 1 and y-1 >= 0:
            check_result = single_map[y-1][x]
        elif axis == 2 and x+1 < len(single_map):
            check_result = single_map[y][x+1]
        elif axis == 3 and y+1 < len(single_map):
            check_result = single_map[y+1][x]
        return check_result
    # except:
        return None

a = 0
while True:
    # 계산먼저 - 계산식은 월드좌표
    a += 1
    check = check_map(world, axis, state_x, state_y)
    print('현재위치')
    print(world[state_y][state_x])
    axis = direction_type[axis - 1]
    if check and check['floor'] == 0 and check['tread'] == 0:
        print('왼쪽 회전후 왼쪽한칸')
        print('이동 위치 확인')
        print(check)
        check['tread'] = 1
        state_x = check['x']
        state_y = check['y']
        count += 1
        rotation = 0
    else:
        rotation += 1
        if rotation == 4:
            axis = direction_type[axis - 1]
            check = check_map(world, axis, state_x, state_y)
            if check and check['floor'] == 0:
                break
            else:
                state_x = check['x']
                state_y = check['y']
                axis = direction_type[axis + 2]

print('결과')
print(count)