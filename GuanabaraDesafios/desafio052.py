#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um numero: '))

if num % 2 == 0 and num != 2:
    print(f'O numero {num} não é primo')
elif num % 3 == 0 and num != 3:
    print(f'O número {num} não é primo')
elif num % 5 == 0 and num != 5:
    print(f'O número {num} não é primo')
elif num % 7 == 0 and num != 7:
    print(f'O número {num} não é primo')
else:
    print(f'O número {num} é primo')

qntd_num_div = 0
for c in range(1,num + 1):
    
    if num % c == 0:
        print('\033[33m', end='')
        qntd_num_div +=1
    else:
        print('\033[31m', end='')    
        
    print(f'{c} ', end='')
print(f'\nO numéro {num} foi divisivel {qntd_num_div} vezes')
if qntd_num_div == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')