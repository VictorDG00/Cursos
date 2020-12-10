colunaUp = [4, 3, 2, 1]
colunaDown = [1, 2, 2, 2]
linhaLeft = [4, 3, 2, 1]
linhaRigth = [1, 2, 2, 2]

contador1 = 0
contador2 = 0


while contador1 >= 4:
    if colunaUp[0] == 4 and colunaDown[0] == 1:
        print('1 2 3 4')
        contador1+=1
    elif colunaUp[0] != 4:
        print('teste')
        contador1+=1



