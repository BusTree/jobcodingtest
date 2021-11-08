import random

# 상하좌우
map_size = random.randrange(1, 101)
guide_size = random.randrange(1, 101)
print('map size')
print(map_size)
move_type = ['R', 'L', 'U', 'D']
move_guide = ''

for i in range(guide_size):
    move_guide += random.sample(move_type, 1)[0]
    move_guide += ' '

move_guide = move_guide.replace(" ", "")
move_list = list(move_guide)
print('move')
print(move_list)

x, y = 1, 1
for move in move_list:
    if move == "R" and y < map_size:
        y += 1
    elif move == "L" and y > 1:
        y -= 1
    elif move == "U" and x > 1:
        x -= 1
    elif move == "D" and x < map_size:
        x += 1

print(x, y)
