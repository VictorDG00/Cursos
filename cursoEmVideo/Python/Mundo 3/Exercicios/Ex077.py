# uma tupla com varias palavras não use acentos
# depois disso vc deve mostrar para cada palavra quais são as saus vogais

palavra = ('Coletar', 'Varinha', 'Marciano', 'Piedade', 'Anestesia', 'Julgamento', 'Italiano', 'Transporte')
for p in palavra:
    print(F'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
