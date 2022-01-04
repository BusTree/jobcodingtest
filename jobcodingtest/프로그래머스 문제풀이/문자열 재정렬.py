word = 'K1KA5CB7'
lst = list(word)
lst.sort()
n = 0
point = 0

for i, value in enumerate(lst):
    try:
        n += int(value)
        point = i
    except ValueError:
        pass

print(''.join(lst[point + 1:]) + str(n))
