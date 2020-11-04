# faça um programa que leia uma frase pelo teclado e mostre
# quantas vezes a letra "a" aparece
# em que posição ela aparece a primeira vez
# em que posição ela aparece a última vez

frase = str(input('Digite um frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A', 0, -1)))
print('A primeira Letra A aparace na posição {}'.format(frase.find('A')+1))
print('a última letra A apareceu na posição {}'.format(frase.rfind('A')+1))