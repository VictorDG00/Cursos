# Desenvolva um programa que leia seis numeros inteiros e mostre
# a soma apenas daq ueles que forem pares. se o valor digitado for impar
# Desconsidere-o
soma = 0
for num in range(1, 7):
    numero = int(input(f'Digite o {num}° numero: '))
    if numero % 2 == 0:
        soma += numero
print(soma)
