# Escreva um programa que leia 2 numeros inteiros e os compare
# definir se o n1 é maior
# Definir se n2 é maior
# definir se são iguais

num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite o segundo numero inteiro: '))
if num1 > num2:
    print('O primeiro é maior')
    #print('{} é maior que {}'.format(num1, num2))
elif num2 > num1:
    print('O segundo é maior')
    #print('{} é maior que {}'.format(num2, num1))
else:
    print('Os numeros são iguais')
    #print('{} é igual a {}'.format(num1, num2))

