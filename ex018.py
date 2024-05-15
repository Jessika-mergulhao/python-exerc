from math import radians, sin, cos, tan
a = float(input('Digite o ângulo que deseja: '))
'''foi necessario chamar a função radiante para que o valor saisse correto'''
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O ângulo de {} tem o seno de {:.2f}'.format(a, s))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(a, c))
print('O ângulo de {} tem a tangente de {:.2f}'.format(a, t))