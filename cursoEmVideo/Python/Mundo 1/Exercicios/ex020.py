# o mesmo professor do desafio anterior quer sortear a ordem de apresentação de
# trabalho dos alunos. faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada

import math
import random
a1 = str(input('Digite o nome do aluno 1: '))
a2 = str(input('Digite o nome do aluno 2: '))
a3 = str(input('Digite o nome do aluno 3: '))
a4 = str(input('Digite o nome do aluno 4: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A lista de apresentação ficou: {}'.format(lista))
