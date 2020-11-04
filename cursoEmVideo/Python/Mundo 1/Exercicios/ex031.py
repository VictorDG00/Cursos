# desenvolva um programa que pergunte a distancia de uma viagem em KM hora
# Calcule o preço da passagem Cobrando 0,50 por KM até 200 km
# e acima de 200km cobre 0,45

from time import sleep
print("_-'-_"*20)
distancia = float(input('Digite a distancia do seu ponto ao seu destino: '))
valor200 = distancia * 0.5
valor201 = distancia * 0.45
print('Calculando o valor...'), sleep(2)
if distancia <= 200:
    print('O valor da viagem é igual á:R$ {} reais'.format(valor200))
else:
    print('O valor da viagem é igual á:R$ {} reais'.format(valor201))
print("_-'-_"*20)

preco = distancia * 0.5 if distancia <= 200 else distancia * 0.50
print('Digite a distancia do seu ponto ao seu destino: ')
print('O valor da viagem é igual á: RS{} Reais'.format(preco))