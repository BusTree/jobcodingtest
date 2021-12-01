dp = []

map_size = 4
map = [1, 3, 1, 5]

dp.append(0)
dp.append(0)
dp += map
print(dp)

for i in range(2, map_size):
    print(dp[i])

    if dp[i - 2] + dp[i] >= dp[i - 1]:
        dp.append(dp[-2] + dp[i])
    else:
        dp.append(dp[i - 1])

print('result')
print(dp[-1])


# 굳이 DP테이블을 선언해야되는 이유가있는가?? append로 하면 안되는가??

## 답안
# 정수 N을 입력 받기
n = int(input())
# 모든 식량 정보 입력 받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1]) 
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n - 1])