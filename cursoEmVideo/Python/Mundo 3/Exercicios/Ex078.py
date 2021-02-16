# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e
# o menor valor digitado e as suas respectivas posições na lista.

quinteto = []
maior = menor = 0
for c in range(0, 5):
    quinteto.append(int(input(f'Digite o {c}° valor da lista:')))
    if c == 0:
        maior = menor = quinteto[c]
    else:
        if quinteto[c] > maior:
            maior = quinteto[c]
        if quinteto[c] < menor:
            menor = quinteto[c]
print(f'Os numeros digitados foram: {quinteto}')
print(f'O maior numero foi: {maior} ele apareceu nas posições:', end='')
for i, v in enumerate(quinteto):
    if v == maior:
        print(f'→{i}', end='')
print()
print(f'O maior numero foi: {menor} ele apareceu nas posições:', end='')
for i, v in enumerate(quinteto):
    if v == menor:
        print(f'→{i}', end='')
