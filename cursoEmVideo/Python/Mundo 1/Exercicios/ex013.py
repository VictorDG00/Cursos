#Faça um algoritimo que leia o salário de um funcionario e mostre
#seu novo salário, com 15% de aumento

salario = float(input('Digite seu salario atual: R$'))
aumento = salario * 0.15
salcomaum = salario + aumento
print('Seu salario atual é: {}; \nseu aumento é de: {:.2f}; \nseu salario na promoção vai ser: {:.2f}'.format(salario, aumento, salcomaum))