# faça um programa que leia um ano e fale se é ano bixesto ou não
from datetime import date
anoAtual = int(input('Qual ano quer analisar? se quiser usar seu ano atual digite 0: '))
if anoAtual == 0:
    ano = date.today().year
if anoAtual % 4 == 0 and anoAtual % 100 !=0 or anoAtual % 400 == 0:
    print('O ano é bissexto :D')
else:    
    print('Esse ano não é bissexto')
