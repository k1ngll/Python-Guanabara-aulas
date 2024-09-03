#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

print('Ache fatorial de um número !!!')

'''
num = int(input('Digite um número: '))
fatorial = num

for c in range(num-1,0,-1):
    fatorial = fatorial * c

print(f'O fatorial de {num} é {fatorial}')

'''

number = int(input('Insert a number: '))
fatorial = number
contador = 1

while contador != (number - 1):
    contador += 1
    fatorial = fatorial * contador


print(f'O fatorial de {number} é {fatorial}')

    