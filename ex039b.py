from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('''Informe o seu sexo:
[ M ] MASCULINO
[ F ] FEMININO ''')
opcao = str(input('Sua opção: ')).upper()
if opcao == 'M':
    print('Quem nasceu em {} tem {} em {}'.format(nasc, idade, atual))
    if idade == 18:
        print('Voce tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('ainda faltam {} ano(s) para o alistamento'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento sera em {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você ja deveria ter se alistado há {} ano(s)'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
else:
    print('Voce não precisa fazer alistamento obrigatório')
