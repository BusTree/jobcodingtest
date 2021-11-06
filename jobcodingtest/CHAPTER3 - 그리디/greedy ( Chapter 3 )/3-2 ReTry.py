# 큰 수의 법칙
# 첫째 줄에 N, M K의 자연수가 주어지며, 각자연수는 공백으로 구분한다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.

n = 6 # 배열의 크기
m = 150 # m번 더해서 최종적으로 가장큰 수를 구한다.
k = 9 # 하나의 인덱스 반복수

array = [2, 4, 5, 4, 6, 7]
array.sort()
result = 0
(a, b) = (array[n-1], array[n-2])
(c, d) = divmod(m, k + 1)

aa = k * c * a
bb = c * b
cc = a * d

result = aa + bb + cc
print('result')
print(result)
