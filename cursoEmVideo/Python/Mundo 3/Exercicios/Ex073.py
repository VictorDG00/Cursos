# Crie uma tupla preenchida com os 20 primeiros colocados
# da tabela do Campeonato brasileiro de futebol na ordem de colocação
# depois mostre
# apeas os 5 primeiros
# os 4 ultimos
# uma lista com os times em ordem alfabetica
# em que posição na tabela está o time da Grêmio

top20 = ('São Paulo', 'Atlético-MG', 'Flamengo', 'Grêmio', 'Fluminense', 'Internacional', 'Palmeiras', 'Santos',
         'Ceará', 'Fortaleza', 'Corinthians', 'Athletico-PR', 'Bahia', 'Bragantino', 'Atlético-GO', 'Sport', 'Vasco',
         'Coritiba', 'Botafogo', 'Goiás')
print('=-'*50)
print(f'Os 5 Primeiros são: {top20[0:5]}')
print('=-'*50)
print(f'Os 4 Ultimos são: {top20[-4:]}')
print('=-'*50)
print(f'Times em ordem alfabética: {sorted(top20)}')
print('=-'*50)
print(f'O Grêmio está na posição {top20.index("Grêmio")+1}')
#for pos, c in enumerate(top20):
#    gremio = c == 'Grêmio'
#    if gremio:
#        print(f'O Grêmio está na posição °{pos+1}')
