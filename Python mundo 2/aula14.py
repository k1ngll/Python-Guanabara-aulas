'''
for c in range (1,11):
    print(c , end=' ')
print('fim')

cont = 1 

print('\n')

while cont < 11:
    print(cont , end=' ')
    cont+=1
   
   
num = 1
while num != 0:
    num = int(input('Digite um valor: '))

print('Fim')
 
resp = 'S'

while resp == 'S':
    n = int(input('Digite um valor: '))
    resp = str(input('Deseja continuar? [S/N]')).upper()
print('fim')

'''

number = 1
cont_par = cont_impar = 0

while number != 0:
    number = int(input('Digite um valor: '))
    if number != 0:
        if number % 2 == 0:
            cont_par += 1
        else:
            cont_impar += 1
print(f'{cont_par} valores foram PAR\n{cont_impar} valores foram IMPAR')