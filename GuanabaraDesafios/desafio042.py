'''
 Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''
r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))


if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Pode formar um tringulo')
    if r1 == r2 == r3:
        print('Triangulo Equilátero')
    elif r1 == r2 and r2 != r3 or r1 == r3 and r3 != r2 or r2 == r3 and r3 != r1:
        print('Triangulo Isósceles')
    elif r1 != r2 and r1 != r3:
        print('Triangulo Escaleno')
else:
    print('Não pode formar um triangulo')