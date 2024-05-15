from random import randint
from time import sleep
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] tesoura''')
jogador = int(input('Qual a sua jogada? '))
if jogador == 0:
    jogador = 'Pedra'
elif jogador == 1:
    jogador = 'Papel'
elif jogador == 2:
    jogador = 'Tesoura'
pc = randint(0, 2)
if pc == 0:
    pc = 'Pedra'
elif pc == 1:
    pc = 'Papel'
elif pc == 2:
    pc = 'Tesoura'
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador jogou {}'.format(pc))
print('Jogador jogou {}'.format(jogador))
print('-='*11)
if jogador == 'Pedra' and pc == 'Tesoura':
    print('Jogador Venceu!')
elif jogador == 'Pedra' and pc == 'Papel':
    print('Computador Venceu!')
elif jogador == 'Papel' and pc == 'Tesoura':
    print('Computador Venceu!')
elif jogador == 'Papel' and pc == 'Pedra':
    print('Jogador Venceu!')
elif jogador == 'Tesoura' and pc == 'Pedra':
    print('Computador Venceu!')
elif jogador == 'Tesoura' and pc == 'Papel':
    print('Jogador Venceu!')
elif jogador == pc:
    print('Empate!')
else:
    print('Alternativa errada. Tente novamente')
