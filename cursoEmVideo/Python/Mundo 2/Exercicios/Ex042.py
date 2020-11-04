# Refaça o desafio 35 acresentando o recurso de mostrar que tipo
# de triagulo sera formado
# equilatero todos os lados iguais
# isosceles dois lados iguais
# escaleno todos os lados dif


print('--' * 20)
print('Digite 3 segmentos de de reta para ver qual tipo de triangulo da para formar.')
seg1 = float(input('1° Segmento'))
seg2 = float(input('2° Segmento'))
seg3 = float(input('3° Segmento'))
eTriangulo = bool

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Pode ser um triangulo')
    eTriangulo = True
else:
    print('Nâo pode ser um triangulo')
    eTriangulo = False

if eTriangulo == True and seg1 == seg2 == seg3:
    print('Esse triangulo é Equilatero')
elif eTriangulo == True and seg1 == seg2 or seg2 == seg3 or seg1 == seg3:
    print('Esse triangulo é Isosceles')
elif eTriangulo == True and seg1 != seg2 and seg2 != seg3 and seg1 != seg3:
    print("Esse triangulo é Escaleno")

print('--' * 20)

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima pode ser um triângulo ', end='')
    if seg1 == seg2 == seg3:
        print('Equilátero')
    elif seg1 != seg2 != seg3 != seg1:
        print('Escaleno')
    else:
        print('Isósceles')
print('--' * 20)
