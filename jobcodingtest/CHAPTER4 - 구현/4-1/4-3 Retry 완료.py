# 왕실의 나이트 ( 115P )
# 체스판 8 x 8
# 나이트 이동경로 구현
# 수평 두칸 이동뒤 수직으로 한칸이동 ( 4가지 )
# 수직으로 두칸 이동뒤 수평 한칸이동 ( 4가지 )
# 맵 밖으로 나가면 제외됨
# 나이트 위치에서 이동할수있는 이동경로 개수를 리턴

# input_data = 'a1'
input_data = input()
row = int(input_data[1]) - 1  # y축
column = int(ord(input_data[0])) - int(ord('a'))  # x축


# world_map = [list(range(0, 8))] * 8
moveType = [[-2, -1], [-2, +1], [-1, +2], [+1, +2], [+2, -1], [+2, +1], [-1, -2], [+1, -2]]

result = []

for step in moveType:
    move_y = row - step[1]
    move_x = column - step[0]

    if 0 <= move_x < 8 and 0 <= move_y < 8:
        result.append([move_y, move_x])

print('result')
print(result)
print(len(result))

# list 와 range를 활용해서 편하게 배열생성할 수 있음
# 문자열 -> 숫자치환 ord로 변환후 'a' (97) 에서 빼고 +1 하는 방식으로 구현
# 에초에 맵을 구현할 필요가없음 주어진 숫자를 치환하고 음수가 나오면 경우의수에서 제외하면됨
# 문자열을 배열처럼 사용가능 ex) foo = input[0]
# if문 숫자 between의 경우 변수와 and를 스킵하고 사용할수있다. ex 24_Line
