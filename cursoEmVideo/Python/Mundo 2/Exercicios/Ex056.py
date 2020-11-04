# desenvolva um programa que leia o nome idade e sexo de 4 pessoas.
# no final do programa mostre:
# a media de idade do grupo X
# qual nome do homeme mais velho X
# quantas mulheres tem menos de 20X
somaIdade = 0
I = 0
nomeVelho = str
mulherNova = 0
for c in range(1, 5):
    nome = str(input(f'Nome da {c}° pessoa: '))
    idade = int(input(f'Idade da {c}° pessoa: '))
    sexo = str(input(f'Sexo (M/F): ')).upper()
    somaIdade = somaIdade + idade
    if idade > I and sexo == 'M':
        I = idade
        nomeVelho = nome
    if idade <= 20 and sexo == 'F':
        mulherNova += 1

print(f'A media de idade é: {somaIdade / 4}')
print(f'O nome do homem mais velho é: {nomeVelho} com {I} anos')
print(f'A quantidade de mulheres com menos de 20 anos é: {mulherNova}')
