# Refaça o exercicio 51, com while
# desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# no final, mostre os N termos dessa progressão

primeiroTerm = int(input('Digite um termo para uma PA: '))
razaoPa = int(input('Digite a razão dessa mesma PA: '))
decimo = primeiroTerm + (10 - 1 * razaoPa)
contador = 0
while contador < decimo + razaoPa:
    print(contador, end=' > ')
    contador = contador + razaoPa
print('fim')

