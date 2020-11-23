# faça um programa que mostre a tabuada de varios numeros
# um de cada vez, para cada valor digitado
# o programa sera interrompido quando for solicityado um numero negativo

while True:
    multiplicado = int(input('Digite um numero para ver sua tabuada: '))
    for tab in range(1, 11):
        print(f'{multiplicado}x{tab}={multiplicado * tab}')
    continuacao = str(input('Quer ver outra tabuada? [S/N]'))
    if continuacao in 'Nn':
        break
print('cabo nego')

