import time

# 거스름돈
# 당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원 10원짜리 동전히 무한히 존재한다고 가정한다.
# 손님에게 거슬러 줘야할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야할 돈 N은 항상 10의 배수이다.


Units = [500, 100, 50 ,10]
repaidMoney = 5680
coinType = 0
coinCount = 0

start_time = time.time()

while repaidMoney >= 9 :
    if repaidMoney < Units[coinType] :
        coinType += 1
    else :
        repaidMoney = repaidMoney - Units[coinType]
        coinCount += 1

end_time = time.time()

print("time :", end_time - start_time)
## 1.049
print('결과 - 거슬러 줘야하는 최소개수의 동전')
print(coinCount)