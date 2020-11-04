# escreva um programa que leia um Numero N inteiro qualquer e mostre os N
# primeiros elementos da sequencia gibonacci
# fibonnaci é a soma dos dois anteriores
# 0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
rangeF = int(input('Digite um numero qualquer'))
n1 = 0
n2 = 1
n3 = 1
while rangeF > 0:
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    rangeF-=1
    print(n1, end='>')