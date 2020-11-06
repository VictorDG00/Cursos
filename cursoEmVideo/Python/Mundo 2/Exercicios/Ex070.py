# crie um programa que leia o nome e o preço de varios produtos
# o programa deve perguntar se o usuario quer algo mais
# no final deve ter um output de
# qual é o total de gastos na compraX
# quantos produtos custam mais de 1kX
# qual foi o produto mais barato e o preço dele

cpreco = 0
maisde1k = 0
nomebarato = str
precobarato = 0
print('-'*10, 'Haskeando a loja', '-'*10)

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    cpreco += preco
    if precobarato == 0:
        precobarato = preco
        nomebarato = nome
    elif precobarato > preco:
        precobarato = preco
        nomebarato = nome
    if preco >= 1000:
        maisde1k += 1
    continuar = str(input('Deseja comprar algo mais? [S/N]'))
    if continuar in 'Nn':
        break
print(f'''
O valor total da compra R${cpreco}
{maisde1k} Produtos custam mais de 1k
O produto mais barato foi {nomebarato} por R$ {precobarato}
''')
print('FIM')
