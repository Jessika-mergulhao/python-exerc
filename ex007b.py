nome = input('Informe seu nome: ')
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2

print("A média final do aluno(a) {} é: {:.1f} ".format(nome, m))

if m >= 7:
    print('Parabens {}, você foi aprovado(a)!!'.format(nome))
else:
    print('{}, Infelizmente você não foi aprovado(a).'.format(nome))
