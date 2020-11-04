# Desenvolva um programa que leia o comprimento de
# três retas e diga ao usuario se eles podem ou não formar um triangulo
print('-='*20)
print('Digite 3 segmentos de de reta para ver se é possivel fazer um triangulo.')
seg1 = float(input('1° Segmento'))
seg2 = float(input('2° Segmento'))
seg3 = float(input('3° Segmento'))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 +seg2:
    print('PODIIII')
else:
    print('NÃO PODIIII')

print('-='*20)