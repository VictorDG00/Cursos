# faça um programa que leia 3 numeros e informe a qual é o maior e qual é o menor

n1 = int(input('Digite o número 1°: '))
n2 = int(input('Digite o número 2°: '))
n3 = int(input('Digite o número 3°: '))

#if n1 > n2 and n1 > n3:
    #print('{} é o maior numero'.format(n1))
#elif n2 > n1 and n2 > n3:
   # print('{} é o maior numero'.format(n2))
#else:
    #print('{} é o maior numero'.format(n3))
#if n1 < n2 and n1 < n3:
    #print('{} é o menor numero'.format(n1))
#elif n2 < n1 and n2 < n3:
    #print('{} é o menor numero'.format(n2))
#else:
   # print('{} é o menor numero'.format(n3))
#print('fim')

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
print('{} é o maior numero'.format(maior))
print('{} é o menor numero'.format(menor))
