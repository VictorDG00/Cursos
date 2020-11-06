# faça um programa que leia idade e o sexo de varias pessoas
# a cada pessoas o programa deve perguntar se quer continuar
# retornando 3 infos
# quantas pessoas tem mais de 18
# quantos homens foram cadastrados
# quantas mulheres tem menos de 20
dezoito = mulhermenos20 = homens = 0

while True:
    idade = int(input('Digite a idade da pessoa: '))
    if idade >= 18:
        dezoito += 1
    while True:
        sexo = str(input('Digite o sexo da pessoa M/F: ')).upper()
        if sexo in 'MF':
            break
    if sexo == 'M':
        homens += 1
    if idade <= 20 and sexo == 'F':
        mulhermenos20 += 1
    continuar = str(input('Deseja continuar cadastrnado pessoas? S/N')).upper()
    if continuar in 'N':
        break
print(f'''Foram cadastrados: 
{dezoito} Pessoas com mais de 18 anos
{homens} Homens 
{mulhermenos20} Mulheres com Menos de 20 anos
''')
