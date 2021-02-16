# array
# array tem estrutura = ['0','1','2'] | para adicionar usa "var.append('tres')" ou ".insert(possição,'0')"
# para apagar é "del var[possição]"
#num = [2, 4, 7, 6]
#num[2] = 3
#num.append(7)
#
#print(num)

#valores = []
#valordig = []
#valores.append(5)
#valores.append(9)
#valores.append(4)

#for c, v in enumerate(valores):
#    print(f'c = posição {c}, v = conteudo {v}')
#for v in valores:
#    print(f'{v}...', end='')

#print(end='\n')
#for cont in range(0, 5):
#    valordig.append(int(input('Digita um numero ae na moral')))
#for c, v in enumerate(valordig):
#    print(f'c = posição {c}, v = conteudo {v}')

#link entre vars
a = [1, 2, 3, 4]
b = a
b[2] = 86
#copia
a = [1, 2, 3, 4]
b = a[:]
b[2] = 86
