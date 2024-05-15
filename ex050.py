soma = 0
cont = 0
for c in range(0, 6):
    n = int(input('informe um número: '))
    if n % 2 == 0:
        soma += n
        cont = cont +1
print('Você informou {} números par e a soma foi {}'.format(cont, soma))
