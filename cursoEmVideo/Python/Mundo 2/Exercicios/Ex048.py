# faça um programa que calcule a soma entre todos os numeros impares que são
# multiplos de 3
# que se encontram no intervalo de 1 até 500
soma = 0
conta = 0
for mult in range(1, 501, 2):
    if mult % 3 == 0:
        conta = conta + 1
        soma = mult + soma
    else:
        continue
print(soma)
print(conta)
