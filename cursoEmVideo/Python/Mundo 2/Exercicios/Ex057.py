# Faça um programa que lai o sexo de uma pessoa
# mas só aceitei M ou F
# caso esteja errado, paça que digite novamente até acertar F ou M

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'FM':
        sexo = str(input('Digite novamente com M ou F para definir seu sexo:'))
print(f'Sexo {sexo} registrado, Obrigado :D')