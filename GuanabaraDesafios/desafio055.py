# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

#lista_peso = []
for cont in range (1,6):
    peso = float(input(f'Digite o peso da {cont}ª pessoa: '))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso 
    #lista_peso.append(peso)

#print(lista_peso)

#maior_peso = max(lista_peso)
#menor_peso = min(lista_peso)

#print(f'''
#O maior peso é {maior_peso:.1f} Kg
#O menor peso é {menor_peso:.1f} Kg
#''')

print(f'''
O maior peso é {maior:.1f} Kg
O menor peso é {menor:.1f} Kg
''')
