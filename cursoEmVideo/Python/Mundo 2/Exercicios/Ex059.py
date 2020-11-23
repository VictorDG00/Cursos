# Crie um programa que leia 2 valores e mostre um menu na tela
# X[1] somar X[2] multiplicar X[3] maior X[4] novos numeros X[5] sair do programa

numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
opcao = 0
maior = str
while opcao != 5:
    print('-'*20)
    opcao = int(input('''Segue as opções disponiveis para você:
[1] Somar 
[2] Multiplicar
[3] Maior 
[4] Novos numeros
[5] Sair 
    '''))
    if opcao == 1:
        soma = numero1 + numero2
        print(f'A soma de {numero1} com {numero2} é igual a: {soma}')
    if opcao == 2:
        mult = numero1 * numero2
        print(f'A multiplicação dos numeros {numero1} e {numero2} é igual a: {mult}')
    if opcao == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print(f'O meio numero entre {numero1} e {numero2} é: {maior}')
    if opcao == 4:
        numero1 = int(input('Digite o primeiro valor: '))
        numero2 = int(input('Digite o segundo valor: '))
    if opcao == 5:
        print('Obrigado por usar nosso sistema :D')
    if opcao > 5:
        print('Por gentileza escolha uma opção valida')
print('Adeus!')