'''sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250.00:
    psal = sal * (15/100)
else:
    psal = sal * (10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, (psal + sal)))'''
sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250.00:
    novo = sal + (sal * (15/100))
else:
    novo = sal + (sal * (10/100))
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, novo))
