p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
t = int(input('Terceiro valor: '))
# verificando quem é menor
menor = p
if s < p and s < t:
    menor = s
if t < p and t < s:
    menor = t
# verificando quem é maior
maior = p
if s > p and s > t:
    maior = s
if t > p and t > s:
    maior = t
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))