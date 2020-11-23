# faça um programa que leia um numero qualquer e mostre seu fatorial
from math import factorial

numero = int(input('Digite um numero para ver a fatorial dele: '))
fatorial = factorial(numero)
#mult = 0
print(f'A fatoração do numero {numero} é igual a : {fatorial}')
#while fatorial != 1:
    #fatorial -= 1
    #if fatorial == numero - 1:
        #mult = numero * fatorial
    #else:
        #mult = mult * fatorial
#print(f'O número {numero} fatorado fica: {mult}')


