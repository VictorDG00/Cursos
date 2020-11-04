# Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão
# 1 Binario
# 2 Octal
# 3 Hex
num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} Convertido para Octal é: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} Convertido para HEXADECIMAL é: {}'.format(num, hex(num)[2:]))

else:
    print('Digite um numero entre 1 a 3 cara.')
