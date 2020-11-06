# faça um programa que jogue par ou impar com o cpu
# o jogo só sera interrompido quando o jogador perder
# mostrando o total de vitorias consecutivas que ele consquistou no jogo
c = 0

import random
print('Bora jogar par ou ímpar')
print('~~-'*20)
while True:
    escolha = str(input('Você quer Par ou Ímpar [P/I]? ')).upper()
    while escolha not in 'PI':
        escolha = str(input('Você quer Par ou Ímpar [P/I]? ')).upper()
    numMaquina = random.randint(0, 10)
    numJogador = int(input('Digite um numero'))
    soma = numJogador + numMaquina
    print('+'*20)
    print(f'você jogou {numJogador} e a maquina {numMaquina} resultou em {soma}')
    print('+'*20)
    if escolha in 'Pp' and soma % 2 == 0 or escolha in 'Ii' and soma % 2 != 0:
        print('Para bens vc ganhou da maquina boa')
        print('Bora de next')
        c += 1
    else:
        print('vc perdeu otario')
        break
print(f'Você ganhou {c} consecutivas')