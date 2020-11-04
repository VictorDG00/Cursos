# Refaça o Desafio 9 mostrando a tabuada de um numero que o usuario escolher,
# só que agora utilizando laço for

num = int(input('Digite um número para ver sua tabuada até o 10: '))
for tab in range(1, 11):
    print(f'{num}x{tab}={num*tab}')
