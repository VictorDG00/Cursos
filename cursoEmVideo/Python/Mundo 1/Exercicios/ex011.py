#faça um programa que leia a altura e largura de uma parede
#calcule sua area
#defina a quantidade de tinta necessaria para pinta-lo sabendo que
#cada litro de tinta pinta 2m²

paredel = float(input('Largura da parede: '))
paredea = float(input('Altura da parede: '))
paredeArea = paredea * paredel
tinta = paredeArea / 2
print('Sua parede tem {}x{} e sua área é de {}m²'.format(paredea, paredel, paredeArea))
print('O tanto necessario de tinta é {}L'.format(tinta))
