# n개 부품
n = 5
n_list = [8, 3, 7, 9, 2, 2, 2]

m = 3
m_list = [5, 7, 9]
#  부품종류 m개

n_list = sorted(set(n_list))

for i in m_list:
    if i in n_list:
        print('yes', end=' ')
    else:
        print('no', end=' ')