import time
import math
math.factorial(100000)
# 1이 될 때까지
start_time = time.time()

n = 17
k = 4
count = 0

while n != 1:
    (a, b) = divmod(n, k)
    if b == 0:
        n = a
    else:
        n -= 1
    count += 1
end_time = time.time()

print('result')
print(count)
print('결과시간')
print(f"{end_time - start_time:.5f} sec")

# 피드백
# n < 1 보다 n != 1로 비교하는게 연산속도가 더 빠르다. 숫자연산 < 논리연산