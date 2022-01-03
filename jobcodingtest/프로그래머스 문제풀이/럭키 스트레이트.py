n = '12402'
# n = '7755'

half = len(n) / 2

first = 0
second = 0

for i in range(len(n)):
    if i >= half:
        first += int(n[i])
    else:
        second += int(n[i])

if first == second:
    print('LUCKY')
else:
    print('READY')
