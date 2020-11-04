#faça um programa que lia um valor em metros e o exiba
#convertido em centimetros e milímetros

metros = float(input('Digite uma metragem: '))
cm = metros * 100
mm = metros * 1000
print('A medida informada em CM: {}'.format(cm))
print('A medida informada em MM: {}'.format(mm))
