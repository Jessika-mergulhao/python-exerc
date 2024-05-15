sal = float(input('Informe o salário do funcionário: '))
aum = float(input('Quantos porcentos esse funcionário ganhará de aumento? '))
perc = (aum / 100) * sal
ns = sal + perc

print('Um funcionário que ganhava {}, com {}% de aumento, passa a receber R${}.'.format(sal, aum, ns))