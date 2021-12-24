# 문자열 뒤집기
# 연속된 숫자만 뒤집을수있고
# 한방향이 되는데 최소한의수를 구할것

s = '0001100'
array = list(map(int, s))

count0 = 0
count1 = 0

if array[0] == 0:
    count0 += 1
else:
    count1 += 1

for i in range(1, len(array)):
    if array[i-1] != array[i]:
        if array[i] == 0:
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))
