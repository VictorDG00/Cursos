# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem 'SILVA' no nome

nome = str(input('Digite seu nome e vamos ver se ele tem silva')).title().strip()
print('Seu nome tem Silva?', ('Silva' in nome))
