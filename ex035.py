from termcolor import colored
print(colored('Analisador de triângulos', 'magenta'))
print(colored('-=' * 20, 'blue'))
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    print(colored('Os segmentos acima podem formar um triângulo!', 'green'))
else:
    print(colored('Os segmentos acima NÃO PODEM FORMAR um triângulo!', 'red'))






