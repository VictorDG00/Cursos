# faça um programa que leia o peso de cinco pessoas. no final mostre qual foi o maior
# qual foi o menor

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o pesso da {c}°: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(menor)
print(maior)
