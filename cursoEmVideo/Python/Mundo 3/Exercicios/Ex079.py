contagem = []

while True:
    contagem.append(int(input('Digite um valor: ')))
    resposta = (str(input('Quer continuar? (S/N)')))
    if resposta not in 'SsNnSimNãosimnão':
        resposta = (str(input('Quer continuar? (S/N)')))
    if resposta in 'Nn':
        break
print(sorted(set(contagem)))


