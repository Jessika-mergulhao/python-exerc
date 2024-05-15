casa = float(input('Valor da casa: R$ '))
salario = float(input('Qual o valor do salario? R$ '))
ano = int(input('Em quantos anos deseja financiar? '))
prestação = casa / (ano * 12)
mínimo = salario * (30/100)   # Para saber p valor de 30% do salario
print('Para pagar uma casa de {} em {} anos a prestação sera de R${:.2f}.'.format(casa, ano, prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')