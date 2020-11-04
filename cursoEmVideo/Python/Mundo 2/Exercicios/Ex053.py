# crie um programa que leia uma frase qualquer e diga se ela é um PALINDROMO
# desconsiderando os espaços
frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
esarf = frase[::-1]
for letra in range(0, 1):
    print(f'A frase {frase} invertida fica {esarf} ')
    if frase == esarf:
        print('Essa frase é um Palindromo!')
    else:
        print('Essa frase não é um palindromo!')

