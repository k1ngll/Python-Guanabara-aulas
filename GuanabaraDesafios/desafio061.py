#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

'''
primeiro_termo = int(input('Qual o primeiro termo da PA: '))
razao = int(input('Qual a razão da PA: '))
decimo_termo = primeiro_termo + (10-1) * razao

for cont in range(primeiro_termo,decimo_termo + razao, razao):
    print(cont, end =' -> ',)
    #primeiro_termo = primeiro_termo + razao
print('fim')
'''

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Qual a razão da PA: '))
decimo_termo = primeiro_termo + (10-1) * razao


print(decimo_termo,primeiro_termo,razao)