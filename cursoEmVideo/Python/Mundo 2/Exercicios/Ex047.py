# crie um programa que mostre na tela todos o numeros pares que estáo no intervalo de
# 1 e 50

for contador in range(2, 51, 2):
    if contador % 2 == 0:
        print(contador, end=' ')
print('FIM')
