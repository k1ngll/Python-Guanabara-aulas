#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite o numero 1: '))
n2 = float(input('Digite o numero 2: '))
n3 = float(input('Digite o numero 3: '))


if n1 == n2 == n3:
    print('Todos os números são iguais.')
else:
    maior = n1
    menor = n1


    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3

    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3

    print(f"""
    o maior número é {maior}
    o menor número é {menor}
    """)



