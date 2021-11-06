import time

# 숫자 카드 게임
# 첫째 줄에 N, M K의 자연수가 주어지며, 각자연수는 공백으로 구분한다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.

inputN = 3
inputM = 3

cardList = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]
cardList2 = [[7, 3, 1, 8], [3, 3, 3, 4]]
resultList = []

for i, n in enumerate(cardList2):
    n.sort()
    resultList.append(n[0])

resultList.sort()

print('정답')
print(resultList[-1])


## min, max 함수 이해하기
