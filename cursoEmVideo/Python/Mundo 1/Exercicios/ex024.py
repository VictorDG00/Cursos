# crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com nome "santo".

cidade = str(input('Digite o nome da sua cidade: ')).title().strip()
print('Sua cidade começa com santos? {}'.format(cidade[:5] == 'Santo'))

