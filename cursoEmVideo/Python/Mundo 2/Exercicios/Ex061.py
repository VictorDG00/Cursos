# Refaça o exercicio 51, com while
# desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# no final, mostre os N termos dessa progressão

primeiroTerm = int(input('Digite um termo para uma PA: '))
razaoPa = int(input('Digite a razão dessa mesma PA: '))
contador = 1
while contador <= 10:
    print(primeiroTerm, end=' > ')
    primeiroTerm += razaoPa
    contador += 1
print('fim')

