#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

number = int(input('Digite um número: '))

#Todo numero par divido por 2 terá resto 0
if number % 2 == 0:
    print(f'o número {number} é par')
else:
    print(f'o número {number} é impar')