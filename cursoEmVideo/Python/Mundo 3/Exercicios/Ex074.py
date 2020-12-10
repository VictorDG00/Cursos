# crie um programa que vai gerar 5 numeros aleatorios e colocar em uma tupla
# depois disso mostre a listagem de numeros gerados e tb indique o menor e o maior valor da tupla
# 0 ~ 10
from random import randint

num1 = randint(0, 10)
num2 = randint(0, 10)
num3 = randint(0, 10)
num4 = randint(0, 10)
num5 = randint(0, 10)
listadenum = (num1, num2, num3, num4, num5)
print('<>' * 20)
print(listadenum)
maior = 0
menor = 0
for c in listadenum:
    if c > maior:
        maior = c
    if menor == 0:
        menor = c
    elif c < menor:
        menor = c
print(f'O menor número é: {menor}')
print(f'O maior número é: {maior}')
print('<>' * 20)
