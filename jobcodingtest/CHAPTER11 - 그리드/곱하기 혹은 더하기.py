n = "6578"
array = list(map(int, n))
array.sort(reverse=True)
result = 0

for i in array:
    if result == 0:
        result = i
    else:
        if i > 1:
            result *= i
        else :
            result += i

print(result)
