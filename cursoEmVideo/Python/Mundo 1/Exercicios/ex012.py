#faça um algoritimo que leia o preço de um produto
#depois mostre o preço com 5% de desconto

valor = float(input('Digite o valor da compra: R$'))
desc5 = valor - (valor*0.05)
print('sua compra com desconto fica {:.2f}'.format(desc5))
