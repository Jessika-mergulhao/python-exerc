num = int(input('Digite um número: '))
conts = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        conts = conts + 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'. format(num, conts))
if conts == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')



