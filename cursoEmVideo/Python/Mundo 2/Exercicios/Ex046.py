# Faça um programa que mostre na tela uma contagem regresiva para o estouro de
# fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
for anonovo in range(10, -1, -1):
    print(anonovo)
    sleep(1)
print('Feliz ano NOVO BIRRRR')
