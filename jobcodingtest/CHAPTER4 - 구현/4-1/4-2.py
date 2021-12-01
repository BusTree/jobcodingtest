# 시각
n = 5 # user Input
mm = 60
ss = 60
result = 0

for h in range(n+1):
    for m in range(mm):
        for s in range(ss):
            check_time = str(h) + str(m) + str(s)
            if '3' in str(check_time):
                result += 1

print('result')
print(result)
