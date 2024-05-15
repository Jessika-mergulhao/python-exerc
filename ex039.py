from datetime import date
nasc = int(input('Ano de nascimento: '))
ano = date.today().year
print('Quem nasceu em {} tem {} em {}'.format(nasc, ano - nasc, ano ))
if ano - nasc == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif ano - nasc < 18:
    print('ainda faltam {} ano(s) para o alistamento'.format(18 - (ano - nasc),))
    print('Seu alistamento sera em {}'.format(nasc + 18))
else:
    print('Você ja deveria ter se alistado há {} ano(s)'.format((ano - nasc) - 18))
    print('Seu alistamento foi em {}.'.format(nasc + 18))


