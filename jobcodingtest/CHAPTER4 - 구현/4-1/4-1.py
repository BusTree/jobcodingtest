import random

# 상하좌우
map_size = random.randrange(1, 100)
guide_size = random.randrange(1, 100)
move_type = ['R', 'L', 'U', 'D']
move_guide = []

for i in range(guide_size):
    move_guide.append(random.sample(move_type, 1)[0])

print('map_size')
print(map_size)
print('move_guide')
print(move_guide)

x, y = 1, 1
for move in move_guide:
    if move == "R" and y < map_size:
        y += 1
    elif move == "L" and y > 1:
        y -= 1
    elif move == "U" and x > 1:
        x -= 1
    elif move == "D" and x < map_size:
        x += 1

print('result')
print(x, y)
