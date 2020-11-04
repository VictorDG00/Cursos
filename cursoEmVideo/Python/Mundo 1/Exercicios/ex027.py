# Faça um programa que leia o nome completo de uma pessoa
# Mostre em seguida o primeiro e o ultimo nome separados
# EX: ana maria de souza
# Ana
# souza

nome = str(input('Digite seu usuario: ')).split()
print('Seja bem vindo!')
print('Seu primeiro nome:', nome[0])
print('Seu ultimo nome:', nome[-1])

