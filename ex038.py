prim = int(input('Primeiro número: '))
seg = int(input('Segundo número: '))
if prim == seg:
    print('Não existe maior. Os dois valores são iguais!')
elif prim > seg:
    print('O PRIMEIRO valor é maior.')
elif prim < seg:
    print('O SEGUNDO valor é maior')
