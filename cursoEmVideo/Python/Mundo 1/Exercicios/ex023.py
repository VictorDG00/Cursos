#  faça um programa que leia um numero de 0 9999
# e mostre na tela cad aum dos digitos separado
# ex: Digite um numero: 1835
# unidade: 5 dezena 3
# centena: 8 milhar: 1

numero = int(input('Digite um numero de 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 100 % 10
print('Unidade: {}'.format(u), 'Dezena: {}'.format(d))
print('Centena: {}'.format(c), 'Milhar: {}'.format(m))


