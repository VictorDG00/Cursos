# Escreva um programa para aprovar um emprestimo, o programa vai perguntar
# Valor da casa
# Salario do comprador
# quantos anos ela vai pagar
# Calcule o valor da prestação mensal
# Sabendo que ela não pode exceder 30% salario OU
# então o emprestimo sera negado
import math
print('Bem vindo ao cálculo de emprestimo vamos pedir algumas informações a seguir.')
casa = float(input('Digite o valor total da casa em reais: '))
salario = float(input('Digite a renda bruta da sua casa: '))
prestacao = int(input('Digite em quantos anos você quer para pagar o emprestimo: '))
emprestimo = casa / (prestacao * 12)
salario30 = salario * 30 / 100
if emprestimo >= salario30:
    print('Cada prestação fica no valor de: \033[0;30;41m{:0.2f}\033[m'.format(emprestimo))
    print('Infelizmente seu salario é baixo para fazer o emprestimo')
else:
    print('Cada prestação fica no valor de: \033[0;30;41m{:0.2f}\033[m'.format(emprestimo))
    print('Parabéns, você pode pedir o emprestimo')


