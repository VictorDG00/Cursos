# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, segue tabela:
# abaixo de 18.5 Abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 até 30 sobrepeso
# 30 até 40 obesidade
# 40 em diante obesidade morbida

peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em M : '))
imc = peso / (altura * altura)

print('Seu IMC é: {:2f}'.format(imc))
if imc <= 18.5:
    print('Você está com o peso a baixo do ideal de acordo com seu IMC')
elif imc <= 25:
    print('Seu peso está na medida ideal de acordo com seu IMC :D')
elif imc <= 30:
    print('Você está sobre peso de acordo com seu IMC')
elif imc <= 40:
    print('Você está obeso de acordo com seu IMC')
else:
    print('Você está com obesidade morbida de acordo com seu IMC \nIndicamos procurar um nutricionista')
