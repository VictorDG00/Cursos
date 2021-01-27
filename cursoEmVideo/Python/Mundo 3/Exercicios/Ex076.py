# crie um programa que tenha uma tupla unica com nomes de produtos e sesus respectivos preços
# no final mostre uma listagem de preços organizando os dados em forma tabular

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Pendrive', 25, 'Fan', 11.25, 'Livro', 34.90)
print('~'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>8.2f}')

print('~'*40)
