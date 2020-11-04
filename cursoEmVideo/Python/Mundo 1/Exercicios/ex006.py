#crie um algoritimo que leia um numero que mostre
#seu dobro
#seu triplo
#sua raiz quadrada
num= int(input('Escreva um número:'))
dobro= num * 2
triplo= num * 3
raiz= (num ** (1/2))

print('Esse é o dobro: {}; \nEsse é o triplo: {}; \nesse é a Raiz: {:.2f}.'.format(dobro, triplo, raiz))