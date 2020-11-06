# crie um programa que leia varios numeros int
# o  programa vai parar quando digitar 999
# no final vai mostrar quantas numeros foram digitados
# e qual foi a soma deles
# tem que fazer uso breack
count = soma = 0

while True:
    num = int(input('Digite um numero [digite 999 para parar]: '))
    if num == 999:
        break
    soma += num
    count += 1
print(f'Você digitou {count} números, a soma de todos eles é: {soma}')

