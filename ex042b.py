from termcolor import colored
print(colored('Analisador de triângulos', 'magenta'))
print(colored('-=' * 20, 'blue'))
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r3 < r1 + r2 and r1 < r2 + r3 and r2 < r1 + r3:
    print(colored('Os segmentos acima podem formar um triângulo ', 'green'), end='')
    if r1 == r2 == r3:
        print(colored('EQUILÁTERO!', 'green'))
    elif r1 != r2 != r3 != r1:
        print(colored('ESCALENO!', 'green'))
    else:
        print(colored('ISÓSCELES!', 'green'))
else:
    print(colored('Os segmentos acima NÃO PODEM FORMAR um triângulo!', 'red'))
