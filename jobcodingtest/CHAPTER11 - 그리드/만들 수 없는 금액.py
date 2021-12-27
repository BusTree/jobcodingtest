n = [2, 1, 9, 5, 4]
# 답
array = [] + n
for i in range(len(n)):
    for j in range(len(n)):
        array.append(n[i] + n[j])

print(array)
result = list(set(array))
print(result)
count = 1
aa = min(array, key=lambda x: array[x+1] - x != 1)


print(aa)
# 답 틀렸음 다시풀 것
# 답은 간단하나 수학적인 이해가 필요
# 완전탐색 하는방법 공부할 것
# 민우에게 509P 수학적으로 설명해달라고 부탁할 것