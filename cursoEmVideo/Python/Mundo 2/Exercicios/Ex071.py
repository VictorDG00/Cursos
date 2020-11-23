# crie um programa que simule o funcionamento de um caixa eletronico
# no inicio perguntar ao usuario qual sera o valor a ser sacado int
# o programa deve informar quantas cedulas de cada valor serão entregues
# obs considere que o caixa possui cedulas de 50 20 10 1

print('='*26)
print('-'*9, 'Nubank', '-'*9)
print('='*26)

valor = int(input('Digite o valor que sera sacado: '))
nota50 = valor // 50
resto50 = valor % 50
nota20 = resto50 // 20
resto20 = resto50 % 20
nota10 = resto20 // 10
resto10 = resto20 % 10
nota1 = valor // 1 % 10

print(f'''Foram: 
{nota50} notas de 50, 
{nota20} notas de 20, 
{nota10} notas de 10, 
{nota1} notas de 1''')
#valor2 = int(valor / 50)
#valor3 = (valor - (valor2*50))
#print(valor2)