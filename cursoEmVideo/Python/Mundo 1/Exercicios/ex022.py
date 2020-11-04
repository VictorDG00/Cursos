# Crie um programa que
# Leia o nome completo da pessoa e mostre
# O nome com todas as letras maiusculas
# O nome com todos minusculas
# quantas letras ao todos (sem considerar espaços)
# quantas letras tem o primeiro nome

nomeComp = str(input('Digite seu nome completo: '))
priNome = nomeComp.split()
print(nomeComp.upper())
print(nomeComp.lower())
print('Seu nome tem {} letras'.format(len(nomeComp.replace(" ", ""))))
print('Seu nome tem {} letras'.format(len(nomeComp)-nomeComp.count(' ')))
print('Seu primeiro nome é: {} e ele tem {} letras.'.format(priNome[0], len(priNome[0])))



