s = 0
c = 0
for cont in range(1, 501):
    if cont % 2 == 1 and cont % 3 == 0:
        c = c + 1
        s = s + cont
print('A soma de todos os {} valores solicitados é {}'.format(c, s))

