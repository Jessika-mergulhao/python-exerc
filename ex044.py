print('=' * 12, 'LOJAS GUANABARA', '=' * 12)
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    nvalor = preco - (preco * 10/100)
    print('Sua compra de R${:.2f} vai custa R${:.2f} no final'.format(preco, nvalor))
elif opcao == 2:
    nvalor = preco - (preco * 5/100)
    print('Sua compra de R${:.2f} vai custa R${:.2f} no final'.format(preco, nvalor))
elif opcao == 3:
    print('Sua compra de R${:.2f}, sera parcelada em 2x de R${:.2f} SEM JUROS'.format(preco, preco/2))
elif opcao == 4:
    nvalor = preco + (preco * 20/100)
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, nvalor/parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, nvalor))
else:
    print('OPÇÃO INVALIDA de pagamento. Tente novamente!')
