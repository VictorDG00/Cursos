# Manipular cadeira de texto

frase = '  Curso em Vídeo python'

# [9] Seleciona o 10° caracter
# [9:14] Seleciona do caracter 9 ao 13
# [9:21:2] Seleciona do 9 ao 20 pulando 2 caracter a cada caracter impresso
# [:5] vai do 0 ao 4 caracter
# [15:] vai do caracter 15 ao final
# [9::3] seleciona o caracter 9 e vai até o final, pulando de 3 em 3
frase[9]
# comprimento len
len(frase)
print(frase.count('o', 0, 14))
# conta um caracter especifico
print(frase.find('deo'))
print(frase.find('gameboy'))
print('Curso' in frase)
# procura uma palavra especifica na str

# transformação
print(frase.replace('python', 'gameboy'))
# troca o primeiro termo pelo termo após a virgula
print(frase.upper())
# lower
print(frase.capitalize())
# deixa somente a primeira letra da str em maiusculo
print(frase.title())
# deixa todas as letras após o espaço em maiusculo
print(frase.strip())
# tira os espaços do inicio e do final
print(frase.rstrip())
# R para tira o espaço da direita L o da esquerda

# divisão
print(frase.split())
# separa entre os espaços
print('*'.join(frase))
# troca espaço por um caracter escolhido entre ''
print(len(frase))




