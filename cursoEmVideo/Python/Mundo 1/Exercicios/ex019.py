# um professor quer sortear um dos seus quatros alunos para apagar o quadro
# faça um programa que ajude ele, lendo o nome dos alunos e escreva o escolhido

import math
import random
aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))
lista = [aluno1, aluno2, aluno3, aluno4]
print(random.choice(lista))

