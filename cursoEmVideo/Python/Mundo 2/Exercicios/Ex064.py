# crie um progrmaa que leia varios numeros inteiros pelo teclado
# o programa vai parar quando digitar 999
# no final mostrar quantos numeros foram, e a soma entre eles
# desconsiderando o 999

n = cN = sM = 0
while n != 999:
    n = int(input('Digite qualquer numero de até 3 casa: '))
    cN += 1
    if n != 999:
        sM = n + sM

print(f'foram {cN}, dando a soma total de {sM}')
print('Fim')