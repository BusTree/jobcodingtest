# word = 'aabbaccc  답 7'
word = 'abcabcdede'  # 답 8

# 완전탐색으로 문제풀것 각 문자열단위로 잘라서 대입해보고 크기비교

# 답 7
word = list(word)
result = len(word)
count = 0
print(result)
array = []
for i in range(1, len(word)):
    if word[i] == word[i - 1]:
        count += 1
        print('같은 문자열 반복')
        print(word[:i])
    elif ord(word[i]) == ord(word[i - 1]) + 1:
        count += 1
        print('연속된 문자열')
        print(word[:i])
    elif count > 1:
        print('문자열 끊김')
        word[i]
        array.append(count+1)
        count = 0

print(array)

