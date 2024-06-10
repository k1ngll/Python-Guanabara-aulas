'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))

if n1 > n2:
    print(f'The first number is greater')
elif n2 > n1:
    print(f'The second number is greater')
else:
    print(f"doesn't have a greater number, both numbers are equal")