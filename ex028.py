from termcolor import colored
from random import choice
print(colored('--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=', 'yellow'))
print(colored('Vou pensar em um número entre 0 e 5. tente advinhar...', 'blue'))
print(colored('--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=', 'yellow'))
n = int(input('Em que número eu pensei? '))
print(colored('PROCESSANDO...', 'magenta'))
lista = [0, 1, 2, 3, 4, 5]
escolhido = choice(lista)
if escolhido != n:
    print(colored('GANHEI! Eu pensei no número {} e não no {}'.format(escolhido, n), 'red'))
else:
    print(colored('PARABÉNS! Você conseguiu me vencer!', 'yellow'))
