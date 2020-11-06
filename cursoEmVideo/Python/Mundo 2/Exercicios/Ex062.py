# melhore o 61 perguntando até que termo o programa deve mostrar
#primeiroTerm = int(input('Digite o primeiro termo para uma PA: '))
#razaoPa = int(input('Digite a razão dessa mesma PA: '))
#ultTermo = int(input('Até que termo você gostaria de ver? '))
#calcTermo = primeiroTerm + (ultTermo - 1) * razaoPa
#contador = primeiroTerm
#while contador < calcTermo + razaoPa:
    #print(f'{contador}', end=' > ')
    #contador = contador + razaoPa
#print('Fim')
primeiroTerm = int(input('Digite um termo para uma PA: '))
razaoPa = int(input('Digite a razão dessa mesma PA: '))
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(primeiroTerm, end=' > ')
        primeiroTerm += razaoPa
        contador += 1
    print('Para meu irmão')
    mais = int(input('Quer ver mais quantos termos?'))
print('Cabo nego')
print(f'{total} temos solicitados')
