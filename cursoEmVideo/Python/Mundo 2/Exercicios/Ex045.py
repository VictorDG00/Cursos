# crie um programa que faça o computador jogar jokenpô com você

from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
print('*-'*20), sleep(2)
print('Bem vindo ao Jo Ken Pô'), sleep(1)
print('-*'*20), sleep(2)
print('Escolha entre \n(0) Pedra \n(1) Papel \n(2) Tesoura')
escolha = int(input('Escolha uma das opções acima: '))
escolhamaquina = randint(0, 2)

print('''JO
KEN
PÔ''')
print('A maquina escolheu; {} \nVocê escolheu; {}'.format(itens[escolhamaquina], itens[escolha]))

if escolhamaquina == escolha:
    print('Deu empate, tente novamente.')
elif escolhamaquina == 0 and escolha == 2 \
        or escolhamaquina == 1 and escolha == 0 \
        or escolhamaquina == 2 and escolha == 1:
    print('Máquina ganhou!')
elif escolha == 0 and escolhamaquina == 2 \
        or escolha == 1 and escolhamaquina == 0 \
        or escolha == 2 and escolhamaquina == 1:
    print('Você ganhou!')