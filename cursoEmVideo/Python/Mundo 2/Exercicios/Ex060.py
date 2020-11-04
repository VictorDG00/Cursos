# faça um programa que leia um numero qualquer e mostre seu fatorial
# 5!
numero = int(input('Digite um numero para ver a fatorial dele: '))
fatorial = numero
mult = 0

while fatorial != 1:
    fatorial -= 1
    if fatorial == numero - 1:
        mult = numero * fatorial
    else:
        mult = mult * fatorial
print(f'O numero {numero} fatorado fica: {mult}')

# 5! = 5.4.3.2.1 = 120
# 5! = 5.4 = 20
# 20.3 = 60
# 60.2 = 120
