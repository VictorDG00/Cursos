# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extenso, de zero até vinte
# seu programa devera ler um numero pelo teclado e imprimir o numero correspondente
# só aceitar numeros entre 0 e 20
#
zeroaovinte = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
               'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
escolha = int(input('Digite um número de 0 a 20: '))
while not False:
    if 0 <= escolha <= 20:
        print(zeroaovinte[escolha])
        break
    else:
        escolha = int(input('Opa meu anjo, é para escolher de 0 a 20: '))
