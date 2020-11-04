# melhore o 61 perguntando até que termo o programa deve mostrar

primeiroTerm = int(input('Digite o primeiro termo para uma PA: '))
razaoPa = int(input('Digite a razão dessa mesma PA: '))
ultTermo = int(input('Até que termo você gostaria de ver? '))
calcTermo = primeiroTerm + (ultTermo - 1) * razaoPa
contador = primeiroTerm

while contador < calcTermo + razaoPa:
    print(f'{contador}', end=' > ')
    contador = contador + razaoPa
print('Fim')
