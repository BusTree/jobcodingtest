# 큰 수의 법칙
# 첫째 줄에 N, M K의 자연수가 주어지며, 각자연수는 공백으로 구분한다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.

n = 6 # 배열의 크기
m = 150 # m번 더해서 최종적으로 가장큰 수를 구한다.
k = 9 # 하나의 인덱스 반복수

result = 0

array = [2, 4, 5, 4, 6, 7]
array.sort()

(a, b) = (array[n-1], array[n-2])
(c, d) = divmod(m, k + 1)

first = k * (c + d) * a  # 1번 배열 값
second = c * b  # 2번 배열 값
# cc = a * d # 1번배열값 나머지

result = first + second
print('result')
print(result)

# 피드백
# 처음부터 첫뻔째 베열의 개수를 세는것을 사용한다.
# count = int(m / k + 1 )) * k
# count += m % ( k + 1 )
# result = 0
# result += (count) * first # 가장큰수 더하기
# result += (m - count) * second # 두번째로 큰 수 더하기
# print(result)
