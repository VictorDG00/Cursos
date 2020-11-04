# Escreva um programa que faça um computador "pensar" em um numero inteiro entre 0 e 5
# peça para o usuario tentar descobrir o numero ecolhido pelo computador
# o programa devera escrever na tela se o usuario vencer ou perdeu
from time import sleep
from random import randint
mqnNum = int(randint(0, 5))
print('-==-'*10)
sleep(1)
print('Vou pensar em um número entre 0 e 5....... Tente adivinhar')
sleep(1)
print('-==-'*10)
usrNum = int(input('Escolha um numero entre 0 e 5: '))
print('Processando...')
sleep(3)
if mqnNum == usrNum:
    print('Parabéns você acertou o numero que o computador escolheu')
else:
    print('Infelizmente você errou, tente novamente!')
print('--Fim--')
