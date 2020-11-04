# escreve um programa que leia a velocidade de um carro
# se ele ultrapassar 80 KM/h mostre uma mensagem dizendo que ele foi multado
# a mul vai custar R$7,00 por cada km acima do limite
from time import sleep
print('><'*20)
carroVel = float(input('Qual velocidade você estava? '))
multa = (carroVel-80) * 7

if carroVel <= 80:
    print('Você estava abaixo de 80Km/h')
else:
    print('Você estava acima da velocidade permitida')
    print('Calculando sua multa...')
    sleep(2)
    print('Sua multa deu: {}'.format(multa))
print('><'*20)