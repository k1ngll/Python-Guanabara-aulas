# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

sum = 0
contador = 0
for cont in range(0,6):
    num = int(input(f'Digite o {cont} valor: '))
    if num % 2 == 0:
        sum = sum + num # sum += num
        contador += 1

print(f'A soma dos {contador} numéros pares deu : {sum}')    
    