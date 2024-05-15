from random import choice

p = input('Primeiro aluno: ')
s = input('Segundo aluno: ')
t = input('Terceiro aluno: ')
q = input('Quarto aluno: ')
lista = [p, s, t, q]
escolhido = choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))