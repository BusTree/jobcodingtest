# 왕실의 나이트

user_input = 'a1'

x_input = user_input[0:1]
y_input = user_input[1:2]

full_map = []
result = []
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y = ['1', '2', '3', '4', '5', '6', '7', '8']
rule = []

for i in x:
    map = []
    for j in y:
        map.append(i+j)
    full_map.append(map)

for i, x_value in enumerate(x):
    for j, y_value in enumerate(y):
        if x_input == x_value and y_input == y_value:

            if x.index(x[i - 2]) < x.index(x[i]) or x.index(x[i]) < x.index(x[i + 2]):
                if y.index(y[j - 1]) < y.index(y[j]) or y.index(y[j]) < y.index(y[j + 1]):
                    print('i', i)
                    result.append(full_map[i - 2][j - 1])
                    result.append(full_map[i - 2][j + 1])
                    result.append(full_map[i + 2][j - 1])
                    result.append(full_map[i + 2][j + 1])

            # if 0 <= j - 2 or j + 2 < len(y):
            #     if 0 <= i - 1 or i + 1 < len(x):
            #         result.append(full_map[i - 1][j - 2])
            #         result.append(full_map[i - 1][j + 2])
            #         result.append(full_map[i + 1][j - 2])
            #         result.append(full_map[i + 1][j + 2])


print('result')
print(result)
print(len(result))
print('다시풀것 ㅈㅈ')