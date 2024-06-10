# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lista_peso = []
for cont in range (0,5):
    peso = float(input('Digite seu peso: '))
    lista_peso.append(peso)

print(lista_peso)

maior_peso = max(lista_peso)
menor_peso = min(lista_peso)

print(f'''
O maior peso é {maior_peso:.1f} Kg
O menor peso é {menor_peso:.1f} Kg
''')
