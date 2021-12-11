import time
import math

math.factorial(100000)
start_time = time.time()

# 큰 수의 법칙
# 첫째 줄에 N, M K의 자연수가 주어지며, 각자연수는 공백으로 구분한다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.

N = 5
M = 8
K = 3

result = 0
numbers = [2, 4, 5, 4, 6]
numbers.sort(reverse=True)
print(numbers)
for idx, val in enumerate(numbers):
    result += val * K
    if val < numbers[0]:
        idx = 0
        continue
    if M < K:
        result += M * val
        break
    M -= K

print(result)
# 페이지 92 - 다시풀기 ( while문 사용 )
## 리버스보다 n - 1 이 성능이 더좋다
## 파이썬 for문에서는 i의 값을 컨트롤할수없다.
# i를 변수로 선언하고 while문을 사용해아한다.
# idx, val를 사용하고싶으면 enumerate를 사용해야 한다.
# 문제 정답 2가지 방법있으니까 다시 풀어볼것
# 수열 문제풀이방법을 노트에 정리하면서 이해해볼것
