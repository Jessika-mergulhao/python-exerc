casa = float(input('Valor da casa: R$ '))
salario = float(input('Qual o valor do salario? R$ '))
ano = float(input('Em quantos anos deseja financiar? '))
temp = ano * 12   # para descobrir a quantidade de meses ao todo
mensal = casa / temp      # para saber a parcela por mes
perc = salario * (30/100)   # Para saber p valor de 30% do salario
if mensal <= perc:
    print('Para pagar uma casa de {} em {} anos a prestação sera de R${:.2f}.'.format(casa, ano, mensal))
    print('Empréstimo pode ser \033[1:32mCONCEDIDO!\033[M')
else:
    print('Para pagar uma casa de {} em {} anos a prestação sera de R${:.2f}.'.format(casa, ano, mensal))
    print('Empréstimo \033[1:31mNEGADO!\033[M')
