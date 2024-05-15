# aluguel de carro
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

tdia = dia * 60
tkm = km * 0.15

total = tdia + tkm

print('O total a pagar é de R${}.\nSendo: R${} referente aos dias e R${} referente a kilometragem.'.format(total, tdia, tkm))
