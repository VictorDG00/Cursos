# Melhores o jogo 028 onde o computador vai "pensar" em um numero de 0-10
# só que agora a pessoa vai chutar até acertar
# declarando quantas tentativas foram

from random import randint
mqnNum = int(randint(0, 10))
c = 1
print('Acabei de pensar em um numero tenta adivinhar qual é!')
playerNum = int(input('Escolha um numero entre 0 e 10: '))
while playerNum != mqnNum:
    c += 1
    if playerNum < mqnNum:
        playerNum = int(input('Um pouco mais, tenta novamente:'))
    else:
        playerNum = int(input('Um pouco menos, tenta novamente:'))

print(f'você tentou {c} e acertou na ultima com: {playerNum}  :D')