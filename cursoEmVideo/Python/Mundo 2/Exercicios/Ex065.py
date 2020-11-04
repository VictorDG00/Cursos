# crie um programa que leia varios numeros inteiros pelo teclado
# no final da execução mostre a mediaX entre todos os valores e qual foi o maior e o menor
# o programa deve perguntar ao user se quer continuar escrevendo ou não

n = media = maior = menor = c = 0
escolha = False
while not escolha:
    n = int(input('Digite numeros inteiros'))
    c += 1
    media = n + media
    if n > maior:
        maior = n
    if c == 1:
        menor = n
    else:
        menor = n
    escolhacerta = str(input('Quer adicionar mais algum numero?: ')).strip().upper()
    if escolhacerta in 'SIMsims':
        escolha = False
    elif escolhacerta in 'NAOnaon':
        escolha = True

print(f'Essa é a Media dos numeros: {media/c:.2f}')
print(f'Esse foi o maior numero {maior}')
print(f'Esse foi o menor numero {menor}')
print('fim')
print('teste')