# crie um programa que leia duas notas de um aluno e calcule sua
# media, mostrando uma mensagem no final, de acordo com a média atingida:
# media abaixo de 5.0, reprovado
# media entre 5.0 e 6.9 recuperação
# média 7.0 ou mais Aprovado

primeiraNota = float(input('Digite a nota da primeira prova: '))
segundaNota = float(input('Digite a nota da segunda Prova: '))
mediaNotas = (primeiraNota + segundaNota) / 2

if mediaNotas < 5:
    print('Sua media foi {}, você está Reprovado!'.format(mediaNotas) )
elif 7 > mediaNotas >= 5 :
    print('Sua media foi {}, você está de Recuperação!'.format(mediaNotas))
else:
    print('Sua media foi {}, você está Aprovado!'.format(mediaNotas))
