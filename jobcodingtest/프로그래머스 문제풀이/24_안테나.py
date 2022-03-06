# 안테나
import statistics
n = 4
house = [1, 5, 6, 7, 9]

print(house)
print(statistics.median(house))
# 중간값 6
# 문제의 요구상에서 5, 7 중간값이 여러게일때 작은 5를 선택해야함

# ===========================
# n = 4
# data = list(map(int, input().split()))
# data.sort()
# print('답')
# print(data[(n - 1) // 2])