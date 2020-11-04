#crie um programa que leia quanto dinheiro ela tem na carteira
# e mostra quanto teria em doll, considerando doll a 3,27

real= float(input('Digite a quantidade de Reais que você tem: '))
doll= (real/ 3.27)

print('a quantidade de dollar que você pode ter é: {:.2f}'.format(doll))
