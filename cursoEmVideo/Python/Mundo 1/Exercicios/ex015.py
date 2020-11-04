periodo = int(input('Quantos dia você ficou com o carro: '))
distancia = float(input('Quantos Km rodados: '))
total = (periodo * 60) + (distancia * 0.15)

print('Você vai Pagar {} pelo aluguel do carro'.format(total))