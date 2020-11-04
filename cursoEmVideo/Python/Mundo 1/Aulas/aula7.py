# + soma - subtração * multiplicação /divisão
# ** Potência // divisão inteira % resto div
# precedencia: () | ** | * / // % | + -

#nome= input('Qual é seu nome? ')
#print('Prazer em te conhecer {:#^20}!'.format(nome))

num1 = int(input('Um valor: '))
num2 = int(input('Segundo valor: '))
som = num1+num2
mult = num1*num2
sub = num1-num2
div = num1/num2
divint = num1//num2
exp = num1**num2
print('A soma vale {},\nA subtração da {}, o produto é {}, e a divisão é {:.3f} '.format(som,sub,mult,div), end='')
print('Divisão inteira {}, e a potencia é {}'.format(divint,exp))


