# faça um programa que leia um ângulo qualquer e mostre na tela o valor de
# Seno
# Cosseno
# Tangente desse angulo
import math
ang = float(input('Digite um ângulo para receber o seno cosseno e tangente dele: '))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
cos = math.cos(math.radians(ang))

print('Resultado de seno: {:.2f} Resultado do cosseno: {:.2} Resultado da tangente: {:.2f}'. format(sen, cos, tan))