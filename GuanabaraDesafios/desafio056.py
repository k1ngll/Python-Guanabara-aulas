'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

'''

lista_nome = []
lista_idade = []
lista_sexo = []

for cont in range(1,5):
    print(f'--------- {cont}ª PESSOA --------- ')
    nome = str(input(f'Nome: ')).strip()
    lista_nome.append(nome)
    idade = int(input(f'Idade: '))
    lista_idade.append(idade)
    sexo = str(input(f'Sexo [M/F]: ')).lower().strip()
    lista_sexo.append(sexo)

media = (lista_idade[0] + lista_idade[1] + lista_idade[2] + lista_idade[3]) / 4

print(f'\nA media de idade do grupo é {media}')

maior_idade = max(lista_idade)
fem_cont = 0

for c in range (0,4):
    if lista_idade[c] == maior_idade and lista_sexo[c] == 'm':
        print(f'O homem mais velho é {lista_nome[c]} com {maior_idade} anos')
    if lista_sexo[c] == 'f' and lista_idade[c] < 20:
        fem_cont += 1

print(f'existem {fem_cont} mulheres com menos de 20 anos')


'''
print('=========== ENGLISH VERSION ===========')

sum_age = 0
media_age = 0
man_major_age = 0
older_man_name = ''
tot_woman_20 = 0
for c in range(1,5):
    print(f'---------- {c}ª Person ----------')
    name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    gender = str(input('Gender [M/F]: ')).strip() # não precisa do upper por causa do in
    sum_age += age
    if c == 1 and gender in 'Mm': # in = Aceita M ou m 
        man_major_age = age
        older_man_name = name
    if gender in 'Mm' and age > man_major_age:
        man_major_age = age
        older_man_name = name
    if gender in 'Ff' and age > 20:
        tot_woman_20 +=1
        

media_age = sum_age / 4
print(f'The media age of the groupe is {media_age} years')
print(f'The olddest man have {man_major_age} years old and his name is {older_man_name}')
print(f'In the total the group have {tot_woman_20} under 20 years old')       
'''