#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

cont = 1

while cont != 0:
    sexo = str(input('Digite seu Sexo [M/F]: '))
    if sexo in 'MmFf':
        cont = 0
    else:
        print("Sexo incorreto digite novamente")

if sexo in 'mM':
    print('\nSexo masculino')
else:
    print('\nSexo feminino')