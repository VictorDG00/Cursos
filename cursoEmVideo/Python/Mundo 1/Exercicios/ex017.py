# faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triangulo retangulo
# calcule e mostre o comprimento da hipotenusa
import math
x = float(input('Digite o valor do cateto oposto: '))
y = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(x,y)

print('A Hipotenusa dos catetos {}, {} é: {:.2f}'.format(x, y, math.hypot(x, y)))

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi))
