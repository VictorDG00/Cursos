# crie um programa que leia o ano de nascimento de sete pessoas
# no final mostre quantas pessoas tem mais de 21 e quantas são menores de 21
# 1999>= 21  2000<
from datetime import date
maiordeidade = 0
menordeidade = 0
anoAatual = date.today().year
# 2020 - 1999 ><=
for c in range(1, 8):
    anoNasc = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    if anoAatual - anoNasc >= 21:
        maiordeidade += 1
    elif anoAatual - anoNasc <= 20:
        menordeidade += 1
print(f'Temos {maiordeidade} pessoas com mais de 21 anos')
print(f'Temos {menordeidade} pessoas com menos de 21 anos')