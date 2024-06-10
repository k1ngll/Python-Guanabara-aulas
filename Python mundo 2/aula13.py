'''
for cont in range (10,0, -1):
    print(cont)

print('\n')

for cont2 in range (1,11):
    print(cont2)


print('\n')

for cont3 in range (2,101,2):
    print(cont3)
    
print('\n')


num = int(input('Digite um número: '))
for cont4 in range(0,num+1):
    print(cont4)

print('\n')
i = int(input('Inicio: '))
f = int(input('fim: '))
p = int(input('Passo: '))

for cont5 in range (i, f+1 , p):
    print(cont5)
print('fim')
'''
sum = 0
for c in range (0,4):
    n = int(input('Digite um valor: '))
    sum = sum + n
    #sum += n
print(f'O valor da soma dos valores é {sum}')  