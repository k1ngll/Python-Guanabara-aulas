'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
a + b > c
a + c > b
b + c > a
"a soma de dois lados é sempre menor que o terceiro lado."

'''


r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

'''if r1 + r2 > r3:
    if r1 + r3 > r2:
        if r2 + r3 > r1:
            print('pode formar um triangulo')
        else:
            print('não se pode formar um triangulo')
    else:
        print('não se pode formar um triangulo')
else:
    print('não se pode formar um triangulo')
'''
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Pode formar um tringulo')
else:
    print('Não pode formar um triangulo')