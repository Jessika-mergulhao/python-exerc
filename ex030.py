from termcolor import colored
número = int(input(colored('Informe um número qualquer: ', 'magenta')))
resultado = número % 2
if resultado == 0:
    print('O número {} é'.format(número), (colored('PAR!', 'green')))
else:
    print('O número {} é'.format(número), (colored('IMPAR!', 'yellow')))
