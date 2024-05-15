po = float(input('Qual é o preço do produto? R$'))
d = float(input('Qual é o percentual de desconto? '))
pc = (po * d) / 100
nv = po - pc

print('O produto que custava R${}, na promoção com descontode 5% vai custar R${}'.format(po, nv))