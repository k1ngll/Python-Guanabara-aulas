'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

'''
lista_nome = []
lista_idade = []
lista_sexo = []

for cont in range(0,4):
    nome = str(input('Digite seu Nome: '))
    lista_nome.append(nome)
    idade = int(input('Digite sua idade: '))
    lista_idade.append(idade)
    sexo = str(input('Digite seu sexo: '))
    lista_sexo.append(sexo)

media = (lista_idade[0] + lista_idade[1] + lista_idade[2] + lista_idade[3]) / 4

print(f'A media de idade é {media}')

maior_idade = max(lista_idade)
fem_cont = 0

#if maior_idade == lista_idade[0]:
    #print(f'O homem mais velho é {lista_nome[0]} com {maior_idade} anos')

for c in range (0,4):
    if lista_idade[c] == maior_idade and lista_sexo[c] == 'm':
        print(f'O homem mais velho é {lista_nome[c]} com {maior_idade} anos')
    if lista_sexo[c] == 'f' and lista_idade[c] < 20:
        fem_cont += 1

print(f'existem {fem_cont} mulheres com menos de 20 anos')