# faça um programa que leia um numero int
# e diga se ele é ou não primo

numero = int(input('Digite um numero: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end=' ',)
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {numero} foi divisivel {total} vezes')
if total == 2:
    print(f'O número {numero} é um número primo')
else:
    print(f'O número {numero} não é um numero primo')
