# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
# para salario superiores a 1250 calcule um aumento de 10%
# Para os inferiores ou igual o aumento é de 15%

salario = float(input('Digite seu salario para calcularmos seu aumento: '))
dez = salario * 0.10
quinze = salario * 0.15
if salario >= 1250:
    salario = salario + dez
    print('Seu salario agora é {}'.format(salario))
else:
    salario = salario + quinze
    print('Seu salario agora é {}'.format(salario))
print('¬-'*20)