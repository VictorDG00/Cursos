# cores no terminal
# padrão ANSI escape sequence
# \033[estilo;texto;fundo m
# \033[0;33;44m
# estilo: 0 sem nada, 1 negrito, 4 sublinhado, 7 inverte cor fundo letra
# texto 30Branco,31vermelho,32verde,33amarelo,34azul,35roxo,36azul claro,37cinza
# fundo 40Branco,41vermelho,42verde,43amarelo,44azul,45roxo,46azul claro,47cinza
print('\033[0;30;41m teste \033[m')
print('\033[4;33;44m teste \033[m')
print('\033[1;35;34m teste \033[m')
print('\033[42;30m teste \033[m')
print('\033[30m teste \033[m')
print('\033[7;30m teste \033[m')

nome = 'Guanabara'
print('Muit prazer em te conhece, {}{}{}'.format('\033[7;30;44m', nome, '\033[m'))
 