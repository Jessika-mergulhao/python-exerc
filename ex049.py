n = int(input('Digite um número para ver sua tabuada: '))
tab = 0
for c in range(1, 11):
    tab = n * c
    print('{} x {} = {}'.format(n, c, tab))
