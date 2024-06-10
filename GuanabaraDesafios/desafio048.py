#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

sum = 0 #acumulador
contador = 0 #contador

for cont in range (1,501,2):  
    if cont % 3 == 0:
        contador += 1
        sum += cont
        print(cont, end=' ')
    
print(f'\nA soma entre os {contador} números que são múltiplos de três e impar entre 1 a 500 é: {sum}')