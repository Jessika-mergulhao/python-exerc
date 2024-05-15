from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador Vence!')
    elif jogador == 2:
        print('Computador Vence!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:  # computador jogou PAPEL
    if jogador == 0:
        print('Computador Vence!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador Vence!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('Jogador Vence!')
    elif jogador == 1:
        print('Computador Vence!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('JOGADA INVÁLIDA!')
