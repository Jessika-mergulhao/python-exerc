from termcolor import colored
print(colored('Analisador de triângulos', 'magenta'))
print(colored('-=' * 20, 'blue'))
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    if a == b and a == c:
        print(colored('Os segmentos acima podem formar um triângulo EQUILÁTERO!', 'green'))
    elif a != b and a != c:
        print(colored('Os segmentos acima podem formar um triângulo ESCALENO!', 'green'))
    elif a == b or a == c:
        print(colored('Os segmentos acima podem formar um triângulo ISÓSCELES!', 'green'))
else:
    print(colored('Os segmentos acima NÃO PODEM FORMAR um triângulo!', 'red'))
