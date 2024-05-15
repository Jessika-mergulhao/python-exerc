from random import randint
from time import sleep
from termcolor import colored
computador = randint(0, 5)   # Faz o computador "PENSAR"
print(colored('-==-' * 20, 'yellow' ))
print(colored('Vou pensar em um número entre 0 e 5. tente advinhar...', 'blue'))
print(colored('-==-' * 20, 'yellow'))
jogador = int(input('Em que número eu pensei? '))   # Jogador tenta advinhar
print(colored('PROCESSANDO...', 'magenta'))
sleep(3)
if jogador == computador:
    print(colored('PARABÉNS! Você conseguiu me vencer!', 'yellow'))
else:
    print(colored('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador), 'red'))