# condições aninhadas
# if condicao: elif condicao: else:

nome = str(input('Qual seu nome? ')).strip()
if nome == 'Gustavo':
    print('Que nome Bonito')
elif nome == "Pedro" or nome == 'Maria':
    print('Seu nome é bem comum no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome Feminino')
else:
    print("Seu nome é normal")

print('Tenha um bom dia {}'.format(nome))


