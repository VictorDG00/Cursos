# desenvolva um programa que leia quatro valores pelo teclado e guarde os em uma tupla
# no final mostre
# quatas vezes apareceu o valor 9
# emque posição foi digitado o primeiro valor 3
# quais foram os numeros pares
# se não tiver não pode dar nenhum resultado

num = (int(input('Por obséquio bota um número ae')), int(input('Por obséquio bota mais um número ae')),
       int(input('Por obséquio bota mais outro número ae')),
       int(input('Por obséquio bota só mais esse número ae')),)
print(f'Você digitou os valores: {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu na posição {num.index(3)+1}°')
else:
    print('O valor 3 não foi digitado')
print(f'Os numeros pares foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end='')

