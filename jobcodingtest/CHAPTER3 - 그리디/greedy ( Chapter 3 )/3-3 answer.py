# N, M을 공백을 기준으로 구분하여 입력 받기
# n, m = map(int, input().split())

n = 3
m = 3

cardList = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]
cardList2 = [[7, 3, 1, 8], [3, 3, 3, 4]]
resultList = []


result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    print('data')
    print(data)
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    print('min_value')
    print(min_value)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
    print('max')
    print(result)

print(result) # 최종 답안 출력

# 피드백
# for문 안에서 재귀함수 형태로 max나 min을 사용할수 있는것인가??
