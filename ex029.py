from termcolor import colored
veloc = int(input(colored('Qual é a velocidade atual do carro? ', 'blue')))
multa = (veloc - 80) * 7
if veloc <= 80:
    print(colored('Tenha um bom dia! Dirija com segurança!', 'yellow'))
else:
    print(colored('MULTADO! Você exedeu o limite permitido que é de 80km/h', 'red'))
    print(colored('Você deve pagar uma multa de', 'red'), (colored('R${}!'.format(multa), 'yellow')))
    print(colored('tenha um bom dia! Dirija com segurança!', 'yellow'))
