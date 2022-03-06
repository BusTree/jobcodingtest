# 안테나
# import statistics
n = int(input())
# n = 4
#
# house = []
# # for _ in range(n):
# #     house.append(int(input().split()))
#
# house = [5, 1, 7, 9]
#
# print(int(statistics.median(house)))
# print(house)

data = list(map(int, input().split()))
print('data1')
print(data)
data.sort()
print('data2')
print(data)
print(data[(n - 1) // 2])
