from datetime import date
ano = date.today().year    # descobrir o ano atual
nasc = int(input('Ano de Nascimento: '))
idade = ano - nasc   # descobrir a idade
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
