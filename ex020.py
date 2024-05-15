import random
p = input("Primeiro Aluno: ")
s = input("Segundo Aluno: ")
t = input("Terceiro Aluno: ")
q = input('Quarto Aluno: ')
lista = [p, s, t, q]
random.shuffle(lista) # shuffles = embaralhar
print("A ordem de apresentação sera:{}".format(lista))