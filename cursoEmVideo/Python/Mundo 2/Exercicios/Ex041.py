#a confederação nacional de natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria de
# acordo com sua idede
# 0 até 9 mirim
# 9 até 14 Infantil
# 14 até 19 Junior
# 19 até 25 Sênior
# 25 em diante master
from datetime import date

print('Vamo ver qual sua categoria de atleta')
anoNascimento = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - anoNascimento

if idade < 9:
    print('O atleta tem {} anos'.format(idade))
    print('Sua categoria é: Mirim')
elif idade < 14:
    print('O atleta tem {} anos'.format(idade))
    print('Sua categoria é: Infantil')
elif idade < 19:
    print('O atleta tem {} anos'.format(idade))
    print('Sua categoria é: Junior')
elif idade < 25:
    print('O atleta tem {} anos'.format(idade))
    print('Sua categoria é: Sênior')
else:
    print('O atleta tem {} anos'.format(idade))
    print('Sua categoria é: Master')
