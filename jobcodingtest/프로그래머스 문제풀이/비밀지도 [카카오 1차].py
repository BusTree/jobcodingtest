n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        item1 = list(map(int, str(format(arr1[i], 'b').zfill(n))))
        item2 = list(map(int, str(format(arr2[i], 'b').zfill(n))))
        row = ''
        for j in range(n):
            if(item1[j] > 0 or item2[j] > 0):
                row += '#'
            else:
                row += ' '
        answer.append(row)
    return answer

result = solution(n, arr1, arr2)
print('result')
print(str(result))

# 배운것
# zip 함수를 통해 리스트 두개를 묶어서 for문을 사용할수 있음
# zfill, rjust 함수로 남은 자리수를 채울수있음

# 모범답압
# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer