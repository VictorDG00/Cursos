# desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# no final, mostre os 10 primeiros termos dessa progressão

primeiroTerm = int(input('Digite um termo para uma PA: '))
razaoPa = int(input('Digite a razão dessa mesma PA: '))
decimo = primeiroTerm + (10 - 1) * razaoPa
for razao in range(primeiroTerm, decimo+razaoPa, razaoPa):
    print(razao, end=' -> ')
print('fim')