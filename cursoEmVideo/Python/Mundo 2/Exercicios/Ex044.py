# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento
# a vista dinheiro/cheque  10% desc
# a vista cartão 5% desc
# 2 x no cartão mesmo preço
# 3x ou + no cartão 20% de juros

print('='*10, 'Loja dos Dias', '='*10)
total = float(input('Preço da compra: R$'))
# print('No pagamento à vista você ganha um desconto \n Sua compra ficou no valor de {}'.format())
print('''[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
tipoPagamento = int(input('Escolha uma opção de pagamento: '))
if tipoPagamento == 1:
    totalReal = total - (total * 0.1)
elif tipoPagamento == 2:
    totalReal = total - (total * 0.05)
elif tipoPagamento == 3:
    totalReal = total
    parcelas = totalReal / 2
    print('Sua compra ficou em 2x com parcelas de R${:.2f}'.format(parcelas))
elif tipoPagamento == 4:
    totalReal = total + (total * 0.20)
    parcelas = int(input('Quantas parcelas?: '))
    totalRealParcelado = totalReal / parcelas
    print('Sua compra de sera parcelada em {}x de R${:.2f} com JUROS'.format(parcelas, totalRealParcelado))
else:
    print('Selecione uma das opções de pagamento validas')

print('Sua compra de {:.2f} ficou no valor de {:.2f} '.format(total, totalReal))

